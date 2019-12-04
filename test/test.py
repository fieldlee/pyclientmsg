
import unittest
from call import call

_FileName = "./1.txt"

def getbody():
    f = open(_FileName, 'rb')
    buf = f.read(110)
    f.close()
    return buf

class CallTest(unittest.TestCase):
    def testCallSync(self):
        body = getbody()
        for i in range(100):
            call.callSync(body=body,service="")

    def testCallAsync(self):
        body = getbody()
        for i in range(1000):
            call.callAsync(body=body, service="")

    def testcallRegister(self):
        call.callRegister("10001","127.0.0.1:8989")

    def testcallPublish(self):
        call.callPublish("test.service1")

    def testcallSubscribe(self):
        call.callSubscribe("test.service1","127.0.0.1:8989")