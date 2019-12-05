import grpc
import time
from concurrent import futures
from proto import midmsg_pb2_grpc
from handle import  handle
import threading
from test import test
from call import  call
from config import config

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = config.get("address")
_PORT = str(config.get("port"))


def runGrpc():
    grpcServe = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    midmsg_pb2_grpc.add_ClientServiceServicer_to_server(handle.ClientService(), grpcServe)
    grpcServe.add_insecure_port(_HOST + ":" + _PORT)
    grpcServe.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServe.stop(0)

class Rpc(threading.Thread):
    def __init__(self,args):
        super(Rpc, self).__init__()
        self.args = args
    def run(self) -> None:
        runGrpc()


def testcall():
    body = test.getbody()
    g = (x for x in range(10000))
    while True:
        try:
            next(g)
            call.callSync(body=body,service="")
        except StopIteration:
            break


class TestCall(threading.Thread):
    def __init__(self,args):
        super(TestCall, self).__init__()
        self.args = args
    def run(self) -> None:
        testcall()

''''''
'''通过线程Thread Target 方法调用方法'''
# t.start() : 激活线程，
#
# t.getName() : 获取线程的名称
#
# t.setName() ： 设置线程的名称
#
# t.name : 获取或设置线程的名称
#
# t.is_alive() ： 判断线程是否为激活状态
#
# t.isAlive() ：判断线程是否为激活状态
#
# t.setDaemon() 设置为后台线程或前台线程（默认：False）;通过一个布尔值设置线程是否为守护线程，必须在执行start()方法之后才可以使用。如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止；如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
#
# t.isDaemon() ： 判断是否为守护线程
#
# t.ident ：获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None。
#
# t.join() ：逐个执行每个线程，执行完毕后继续往下执行，该方法使得多线程变得无意义
#
# t.run() ：线程被cpu调度后自动执行线程对象的run方法
''''''
def runTestCall():
    t = threading.Thread(target=testcall,args=(1,),name="test1")
    t.start()

'''
threading.RLock 和 threading。Lock的区别
RLock允许在同一个线程中被多次acquire。 而lock不允许
如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐
'''
def lock():
    rlock = threading.RLock()
    rlock.acquire()
    rlock.acquire()
    rlock.release()
    rlock.release()
    lock = threading.Lock()
    lock.acquire()
    lock.release()


'''
threading.Event
事件主要提供了三个方法 set、wait、clear
全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞
    clear：将“Flag”设置为False
    set：将“Flag”设置为True
    Event.isSet() ：判断标识位是否为Ture。

'''
def do(event):
    print("start")
    event.wait()    #等待线程执行
    print("execute")
def event():
    event_obj = threading.Event()
    t = threading.Thread(target=do,args=(event_obj,))
    t.start()
    event_obj.clear()  # 将event flag设置为false
    time.sleep(10.0)
    event_obj.set()    # 将event flag设置为true


'''
threading.Condition

'''
def consumer(cond:threading.Condition):
    with cond:
        print("consumer 之前")
        cond.wait()
        print("consumer 开始消费")

def produce(cond:threading.Condition):
    with cond:
        print("produce 之前")
        cond.notifyAll()
        print("produce notify 之后")

def conmain():
    condition = threading.Condition

    c1 = threading.Thread(target=consumer,args=(condition,),name="c1")
    c2 = threading.Thread(target=consumer,args=(condition,),name="c2")

    p1 = threading.Thread(target=produce,args=(condition,),name="p1")

    c1.start()
    time.sleep(2)
    c2.start()
    time.sleep(2)
    p1.start()



