
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



class TestY(unittest.TestCase):
    def test1(self):
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