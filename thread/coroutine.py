import asyncio


async def cor1():
    print("COR1 start")
    await cor2()
    print("COR1 end")


async def cor2():
    print("COR2")


loop = asyncio.get_event_loop()
loop.run_until_complete(cor1())
loop.close()

'''
    最后三行是重点。
    asyncio.get_event_loop()  : asyncio启动默认的event loop 
    run_until_complete()  :  这个函数是阻塞执行的，知道所有的异步函数执行完成
    close()  :  关闭event loop
'''

import gevent


def fun1():
    print("www.baidu.com")  # 第一步
    gevent.sleep(0)
    print("end the baidu.com")  # 第三步


def fun2():
    print("www.zhihu.com")  # 第二步
    gevent.sleep(0)
    print("end th zhihu.com")  # 第四步


gevent.joinall([
    gevent.spawn(fun1),
    gevent.spawn(fun2),
])
