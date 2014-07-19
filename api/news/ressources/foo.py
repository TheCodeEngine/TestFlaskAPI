from flask.ext import restful


class FooList(restful.Resource):
    def get(self):
        pass


class FooDetail(restful.Resource):
    def get(self, id):
        pass

    def post(self):
        pass


class FooActions(restful.Resource):
    def get(self, id):
        pass