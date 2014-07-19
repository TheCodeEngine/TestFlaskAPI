import argparse
import json
import os
from flask import Flask, g, jsonify, render_template, request, abort
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
from libs.rethink.manager import RDB_BASE_CONFIG

RDB_NEWS = {
    'host': RDB_BASE_CONFIG['host'],
    'port': RDB_BASE_CONFIG['port'],
    'db': os.getenv('RDB_DB', 'news'),
    'table': os.getenv('RDB_TABLE', 'blogposts')
}


class NewsRDB:
    @staticmethod
    def dbSetup():
        connection = r.connect(host=RDB_NEWS['host'], port=RDB_NEWS['port'])
        try:
            r.db_create(RDB_NEWS['db']).run(connection)
            r.db(RDB_NEWS['db']).table_create(RDB_NEWS['table']).run(connection)
            print('Database setup completed. Now run the app without --setup.')
        except RqlRuntimeError:
            print('App database already exists. Run the app without --setup.')
        finally:
            connection.close()
