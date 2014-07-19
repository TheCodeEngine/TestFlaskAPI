import json
from dateutil import parser
from flask import g
from flask.ext import restful
from flask.ext.restful import fields, marshal_with
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
from ..libs.database import RDB_NEWS, NewsRDB


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


class FooList(restful.Resource):
    mfields = {
        'pubDate': fields.DateTime,
        'description': fields.String
    }
    @marshal_with(mfields)
    def get(self):
        g.rdb_conn = r.connect(host=RDB_NEWS['host'], port=RDB_NEWS['port'], db=RDB_NEWS['db'])
        selection = list(r.table(RDB_NEWS['table_newspaper_article']).run(g.rdb_conn))
        return selection


class FooDetail(restful.Resource):
    def get(self, id):
        pass

    def post(self):
        pass


class FooActions(restful.Resource):
    def get(self, id):
        pass