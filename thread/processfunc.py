'''
Process 进程
'''
from multiprocessing import Value,Process,Array

def func(name):
    print('hello', name)

def callProcess():
    p = Process(target=func, args=('zhangyanlin',))
    p.start()
    p.join()  # 等待进程执行完毕


if __name__=="__main__":
    callProcess()

'''
multiprocessing，Array,Value
数据可以用Value或Array存储在一个共享内存地图
创建num和arr时，“d”和“i”参数由Array模块使用的typecodes创建：“d”表示一个双精度的浮点数，“i”表示一个有符号的整数，这些共享对象将被线程安全的处理。

‘c’: ctypes.c_char　　　　 ‘u’: ctypes.c_wchar　　　　‘b’: ctypes.c_byte　　　　 ‘B’: ctypes.c_ubyte
‘h’: ctypes.c_short　　　  ‘H’: ctypes.c_ushort　　  ‘i’: ctypes.c_int　　　　　 ‘I’: ctypes.c_uint
‘l’: ctypes.c_long,　　　　‘L’: ctypes.c_ulong　　　　‘f’: ctypes.c_float　　　　‘d’: ctypes.c_double
'''
def func(a, b):
    a.value = 3.333333333333333
    for i in range(len(b)):
        b[i] = -b[i]

if __name__ == "__main__":
    num = Value('d', 0.0)
    arr = Array('i', range(11))

    c = Process(target=func, args=(num, arr))
    d = Process(target=func, args=(num, arr))
    c.start()
    d.start()
    c.join()
    d.join()

    print(num.value)
    for i in arr:
        print(i)


'''
（2）multiprocessing，Manager

由Manager()返回的manager提供list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array类型的支持。


'''