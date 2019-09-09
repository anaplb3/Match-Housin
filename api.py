from flask import Flask, jsonify, Blueprint, request
from flask_restplus import Resource, Api, reqparse, fields
from create import Facade
from models import User

facade = Facade()

app = Flask(__name__)

api = Api(app=app, doc='/docs')

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('nome', required=True, type=str, location='form')
create_user_parser.add_argument('numTelefone', required=True, type=str, location='form')
create_user_parser.add_argument('username', required=True, type=str, location='form')
create_user_parser.add_argument('senha', required=True, type=str, location='form')
create_user_parser.add_argument('email', required=True, type=str, location='form')

user_properties_parser = reqparse.RequestParser()
user_properties_parser.add_argument('sexo', type=str, required=True, location='form')
user_properties_parser.add_argument('isLimpo', type=str, required=True, location='form')
user_properties_parser.add_argument('isOrganizado', type=str, required=True, location='form')
user_properties_parser.add_argument('isExtrovertido', type=str, required=True, location='form')
user_properties_parser.add_argument('isIntrovertido', type=str, required=True, location='form')
user_properties_parser.add_argument('isResponsavel', type=str, required=True, location='form')
user_properties_parser.add_argument('gostaDeAnimais', type=str, required=True, location='form')
user_properties_parser.add_argument('usernameDono', type=str, required=True, location='form')


    
'''@api.route('/housin/set-properties')
class SetUserProperties(Resource):
    @api.doc(parser=user_properties_parser)
    def post(self):
        data = user_properties_parser.parse_args()
        
        sexo = data['sexo']
        is_limpo = data['isLimpo']
        is_organizado = data['isOrganizado']
        is_extrovertido = data['isExtrovertido']
        is_introvertido = data['isIntrovertido']
        is_responsavel = data['isResponsavel']
        gosta_de_animais = data['gostaDeAnimais']
        email = data['emailUser']
        
        properties = {
            'sexo': sexo,
            'is_limpo': is_limpo,
            'is_organizado': is_organizado,
            'is_extrovertido': is_extrovertido,
            'is_introvertido': is_introvertido,
            'is_responsavel': is_responsavel,
            'gosta_de_animais': gosta_de_animais,
        }
        
        facade.set_user_properties(email, properties)
        
        return 200'''
    
house_parser = reqparse.RequestParser()
house_parser.add_argument('cidade', type=str, required=True, location='form') 
house_parser.add_argument('bairro', type=str, required=True, location='form') 
house_parser.add_argument('numero', type=str, required=True, location='form') 
house_parser.add_argument('qtdMoradores', type=int, required=True, location='form') 
house_parser.add_argument('animais', type=bool, required=True, location='form') 
house_parser.add_argument('tipo', type=str, required=True, location='form') 
house_parser.add_argument('imgBytes', type=str, required=True, location='form') 
house_parser.add_argument('emailDono', type=str, required=True, location='form') 


@api.route("/housin/houses/<string:usernameDono>")
@api.doc(params={"usernameDono": "Login do dono da casa"})
class Houses(Resource):
    
    def get(self, usernameDono):
        node = facade.get_house(usernameDono)
        return jsonify(node)
    
    @api.doc(parser=house_parser)
    def post(self):
        data = house_parser.parse_args()
        
        properties = {
            'cidade': data['cidade'],
            'bairro': data['bairro'],
            'numero': data['numero'],
            'qtdMoradores': data['qtdMoradores'],
            'animais': data['animais'],
            'tipo': data['tipo'],
            'imgBytes': data['imgBytes'],
            'usernameDono': data['usernameDono'],
        }
        
        
        if(facade.create_house(properties)):
            return 200
        else:
            return 400
        

@api.route("/housin/users/<string:username>")
@api.doc(params={"username": 'Login do usuário'})
class Users(Resource):
    def get(self, username):
        print("get users")
        node = facade.get_user(username)
        return jsonify(node)
    
    @api.doc(parser=create_user_parser)
    def post(self, username):        
        json_data = create_user_parser.parse_args()
        nome = json_data['nome']
        n_telefone = json_data['numTelefone']
        username = json_data['username']
        email = json_data['email']
        senha = json_data['senha']
        
        print(api.payload)
        
        node = facade.get_user(username)
        
        if(node == None):
            facade.create_user(User(nome, n_telefone, email, senha, username))        
            return {"result": "Usuário adicionado!"}, 200
        else:
            return {"result": "Usuário já existe!"}
        
        

   
app.run(debug=True)