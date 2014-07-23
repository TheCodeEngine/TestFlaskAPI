from flask import Flask
from flask.ext import restful
from api.news.ressources.foo import FooDetail, FooList

app = Flask(__name__)
api = restful.Api(app)

# Foo
# http://flask-restful.readthedocs.org/en/latest/intermediate-usage.html#project-structure
api.add_resource(FooList, '/foo', '/foo/')
api.add_resource(FooDetail, '/foo/<string:id>', '/foo/<string:id>/')

if __name__ == '__main__':
    app.run(debug=True)