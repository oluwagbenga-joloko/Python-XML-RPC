import datetime
from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC')


class Math:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def divide(self, x, y):
        return x / y

    def multiply(self, x, y):
        return x * y


def getCurrentTime():
    return datetime.datetime.now()


with SimpleXMLRPCServer(('localhost',8000), requestHandler=RequestHandler) as server:
    server.register_instance(Math())
    server.register_function(getCurrentTime)
    server.register_introspection_functions()
    server.register_multicall_functions()
    print("running XML-RPC server")
    server.serve_forever()


