from .main.controller.user_controller import api as user_namespace
from flask import Blueprint
from flask_restplus import Api

api_url_prefix = '/housin'

blueprint = Blueprint('api', __name__, url_prefix=api_url_prefix)
api = Api(blueprint, 
        doc='/docs',
        version='1.0',
        title='Match',
        description='API que provê os matchs para a aplicação Housin')

api.add_namespace(user_namespace, path='/usuarios/<string:username>')