import json
from flask import g
from flask.ext import restful
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
from ..lib.database import RDB_NEWS, NewsRDB

class FooList(restful.Resource):
    def get(self):
        g.rdb_conn = r.connect(host=RDB_NEWS['host'], port=RDB_NEWS['port'], db=RDB_NEWS['db'])
        selection = list(r.table(RDB_NEWS['db']).run(g.rdb_conn))
        return json.dumps(selection)


class FooDetail(restful.Resource):
    def get(self, id):
        pass

    def post(self):
        pass


class FooActions(restful.Resource):
    def get(self, id):
        pass