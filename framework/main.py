class Framework:

    def __init__(self, routes_obj):
        self.routes_lst = routes_obj

    def __call__(self, environ, start_response):
        # get address
        path = environ['PATH_INFO']

        # add slash in the end
        if not path.endswith('/'):
            path = f'{path}/'

        # search for controller
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        # run controller
        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


class PageNotFound404:
    def __call__(self):
        return '404 WHAT', '404 Page not found'
