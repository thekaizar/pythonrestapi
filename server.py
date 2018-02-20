#!/usr/bin/python3
from flask import Flask, flash, request, jsonify, render_template, redirect, session
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///tmp.db')
app = Flask(__name__, static_url_path="/static")
api = Api(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

class alltickers():
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from option") # This line performs query and returns json result
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class Options(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from option") # This line performs query and returns json result
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Select_Options(Resource):
    def get(self, stock_ticker):
        conn = db_connect.connect()
        query = conn.execute("select * from option where Root = '%s' "  %(stock_ticker))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Options, '/options') # Route_1
api.add_resource(Select_Options, '/options/<stock_ticker>') # Route_3

if __name__ == '__main__':
     app.run()
