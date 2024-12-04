from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Unicode)
    def say_hello(ctx, name, times):
        return f"Hello {name * times}"

app = Application([HelloWorldService], 'spyne.examples.hello.soap',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())
wsgi_app = WsgiApplication(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()
