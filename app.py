from flask import Flask
from flask.ext import restful
from api.news.ressources.foo import Foo

app = Flask(__name__)
api = restful.Api(app)

# Foo
api.add_resource(Foo, '/foo')

if __name__ == '__main__':
    app.run(debug=True)