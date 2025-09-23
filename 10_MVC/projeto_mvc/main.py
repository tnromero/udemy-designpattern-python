from tornado import ioloop
from tornado import httpserver
from tornado.web import Application

from controllers import produto_controler

class RunApp(Application):

    def __init__(self):
        handlers = [
            ('/', produto_controler.Index),
            ('/produto/novo', produto_controler.Novo),
            ('/produto/update/(\\d+)/status/(\\d+)', produto_controler.Atualiza),
            ('/produto/delete/(\\d+)', produto_controler.Deleta),
        ]

        settings = dict(
            debug = True,
            template_path = "views",
            static_path = "static"
        )

        Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    ioloop.IOLoop.instance().start()