from flask import Flask
from py2neo import Graph

db = Graph(host='localhost', port='7687', user='neo4j', password='admin')

def create_app():
    app = Flask(__name__)
    return app