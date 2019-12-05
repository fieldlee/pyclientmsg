from proto import midmsg_pb2_grpc,midmsg_pb2



class ClientService(midmsg_pb2_grpc.ClientServiceServicer):
    def Call(self,request,context):
        print(request)
        netRsp = bytes("python client return info", encoding="utf8")
        return midmsg_pb2.CallRspInfo(m_Net_Rsp=netRsp)

    def AsyncCall(self, request, context):
        print("%d"%request.AskSequence)
        res = str(request.AskSequence) + "client return info"
        netRsp = bytes(res, encoding="utf8")
        return midmsg_pb2.CallRspInfo(m_Net_Rsp=netRsp)