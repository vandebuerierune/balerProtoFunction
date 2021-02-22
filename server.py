from concurrent import futures
import logging

import grpc

import test_pb2 as helloworld_pb2
import test_pb2_grpc as helloworld_pb2_grpc

import pandas as pd

class Greeter(helloworld_pb2_grpc.GreeterServicer):

  def SayHello(self, request, context):
    print(request)
    req = repr(request)
    req = req.split('"')[1]
    print(req)
    collumname = req.split("/")[0]
    val = req.split("/")[-1]
    print(collumname)
    print(val)
    dta = {'sensor': [collumname],'data': [val] }
    df = pd.DataFrame(dta, columns=['sensor','data'])
    df.to_csv('./data.csv',mode = 'a', index=False, header=False)

    return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
