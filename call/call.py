import grpc
from proto import midmsg_pb2,midmsg_pb2_grpc
from config import config

_ServeHost = config.get("severaddr")
_ServePort = str(config.get("severport"))

def callSync(body:bytes,service:str):
    conn = grpc.insecure_channel(_ServeHost + ':' + _ServePort)
    client = midmsg_pb2_grpc.MidServiceStub(channel=conn)
    response = client.Sync(midmsg_pb2.NetReqInfo(m_Body=body,service=service))
    print(type(response.m_Net_Rsp))
    print("%s"%response.m_Net_Rsp)

def callAsync(body:bytes,service:str):
    conn = grpc.insecure_channel(_ServeHost + ':' + _ServePort)
    client = midmsg_pb2_grpc.MidServiceStub(channel=conn)
    response = client.Async(midmsg_pb2.NetReqInfo(m_Body=body,service=service))
    print("%s"%response.m_Net_Rsp)


def callRegister(seq:str,address:str):
    conn = grpc.insecure_channel(_ServeHost + ':' + _ServePort)
    client = midmsg_pb2_grpc.MidServiceStub(channel=conn)
    ip = address.split(":",2)[0]
    port = address.split(":",2)[1]
    response = client.Register(midmsg_pb2.RegisterInfo(sequence=seq,ip=ip,port=port))
    print(response.success)

def callPublish(service:str):
    conn = grpc.insecure_channel(_ServeHost + ':' + _ServePort)
    client = midmsg_pb2_grpc.MidServiceStub(channel=conn)
    response = client.Publish(midmsg_pb2.PublishInfo(service=service))
    print(response.success)

def callSubscribe(sevice:str,address:str):
    conn = grpc.insecure_channel(_ServeHost + ':' + _ServePort)
    client = midmsg_pb2_grpc.MidServiceStub(channel=conn)
    ip = address.split(":", 2)[0]
    port = address.split(":", 2)[1]
    response = client.Subscribe(midmsg_pb2.SubscribeInfo(service=sevice,ip=ip,port=port))
    print(response.success)