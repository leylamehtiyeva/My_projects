class GenericView:
    methods = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):

#def __init__(self, methods=('GET',)):
#        super().__init__()

    def render_request(self, request, method):
        if method in self.methods:
            func = getattr(self, method.lower())
            return func(request)
        else:
            raise TypeError('данный запрос не может быть выполнен')

    def get(self, request):
        if not isinstance(request, dict):
            raise TypeError('request is not a dictionary')
        if 'url' not in request:
                raise TypeError('request does not contain the required url key')

        return f"url: {request['url']}"


dv1 = DetailView(methods=('GET', 'PUT'))
html = dv1.render_request({'url': 'https://prop.ru/home'}, 'GET')
print(html)