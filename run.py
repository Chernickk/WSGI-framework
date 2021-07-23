from wsgiref.simple_server import make_server
from framework.main import Framework
from urls import routes

app = Framework(routes)

with make_server('', 8080, app) as httpd:
    print(f'Run on port {httpd.server_port}...')
    httpd.serve_forever()
