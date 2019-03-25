from xmlrpc.client import ServerProxy, MultiCall
import xmlrpc.client 


with ServerProxy("http://localhost:8000/RPC") as server:
    serverMethods = server.system.listMethods()
    print(serverMethods)
    print(server.getCurrentTime())
    multi = MultiCall(server)
    multi.add(1,2)
    multi.subtract(9,8)
    multi.multiply(8,4)
    multi.divide(9,2)
    for res in multi():
        print(res)
    