import grpc
from random import randint
from time import sleep
# import the generated classes
import test_pb2 as helloworld_pb2
import test_pb2_grpc as helloworld_pb2_grpc

channel = grpc.insecure_channel('192.168.1.21:50051')
print('connected to server')

def run(dingske):
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name=dingske))
  print("Greeter client received: " + response.message)


while True:
  x = randint(-4,30)
  x = str(x)
  data = 'PRES' + "/" +  x
  run(data)
  x = int(x)
  sleep(2)