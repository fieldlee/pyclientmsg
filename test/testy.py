
import unittest
import asyncio
import requests
import time

def testY():
    yield from "abcd"

def testW():
    i = 0
    while True:
        i = yield i
        # i += 1
        if i > 10:
            raise StopIteration

async def downloadurl(url):
    data =  requests.get(url)
    print("get {} response complete.".format(url))

async def maindown():
    start = time.time()
    await asyncio.wait([
        downloadurl("https://www.163.com"),
        downloadurl("https://www.mi.com"),
        downloadurl("https://www.baidu.com")])
    end = time.time()
    print("Complete in {} seconds".format(end - start))

async def testawait2(i):
    r = await other_test(i)
    print(i,r)

async def other_test(url):
    start = time.time()
    r = requests.get(url)
    print(time.time()-start)
    return r

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

async def mainsub():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    dones, pendings = await asyncio.wait(tasks)

    for task in dones:
        print('Task ret: ', task.result())



def consumer():
    r = ''
    while True:
        n = yield r  # 跳出生成器，n没有定义
        print("_"*50,n)
        if not n:
            print("*"*50)
            return
        print('[CONSUMER] Consuming %s...' %n)
        r = '200 OK'
def produce(c):
    c.send(None)  # 启动生成器，从生成器函数的第一行代码开始执行
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCE] Producing %s....' %n)
        r = c.send(n) #获取yield返回值
        print('[PRODUCE] Consumer return %s....' %r)
    c.close()  # 关闭consumer，整个过程结束


class TestY(unittest.TestCase):
    def testProduct(self):
        c = consumer()  # 创建生成器对象
        produce(c)


    def testMainSub(self):
        start = now()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(mainsub())
        print('TIME: ', now() - start)


    def test1(self):
        D = {k: 8 for k in ['s', 'd']}
        f = {k:9 for k in list("helo")}
        D = {k: v for (k, v) in zip(['name', 'age'], ['tom', 12])}

        D = sorted(iter([2, 5, 8, 3, 1]))
        D.reverse()
        print(D, f)

        b = '中华人民共和国'
        b = bytes(b,encoding="utf8")
        b2 = bytearray(b)
        s = str(b,encoding="utf8")
        print(s,b2,b2[:2])

        l = list(map(lambda x : x+1,iter([1,2,3,4,5])))
        print(l)

        s = set([1,2,3,4,5,6])
        l = list(map(lambda x:x+1,s))
        print(l)
        for i in b2:
            print(i)
        a = testY()
        for i in a:
            print(i)

    def test2(self):
        b = testW()
        next(b)
        l = [x for x in range(15)]
        for i in l:
            try:
                t = b.send(i)
            except StopIteration:
                break
            print(t)
    def testdown(self):
        loop = asyncio.get_event_loop()

        loop.run_until_complete(maindown())
        loop.close()

    def testurl(self):
        url = ["https://segmentfault.com/p/1210000013564725",
               "https://www.jianshu.com/p/83badc8028bd",
               "https://www.baidu.com/"]

        loop = asyncio.get_event_loop()
        task = [asyncio.ensure_future(testawait2(i)) for i in url]
        start = time.time()
        loop.run_until_complete(asyncio.wait(task))
        endtime = time.time() - start
        print("总共使用{}时间".format(endtime))
        loop.close()