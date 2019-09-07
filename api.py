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
create_user_parser.add_argument('email', required=True, type=str, location='form')
create_user_parser.add_argument('senha', required=True, type=str, location='form')

@api.route("/housin/create-user")
class CreateUser(Resource):
    
    @api.doc(parser=create_user_parser)
    def post(self):        
        json_data = create_user_parser.parse_args()
        nome = json_data['nome']
        n_telefone = json_data['numTelefone']
        email = json_data['email']
        senha = json_data['senha']
        
        print(api.payload)
        
        facade.create_user(User(nome, n_telefone, email, senha))
        
        return {"result": "Usuário adicionado!"}, 200

user_properties_parser = reqparse.RequestParser()
user_properties_parser.add_argument('sexo', type=str, required=True, location='form')
user_properties_parser.add_argument('isLimpo', type=str, required=True, location='form')
user_properties_parser.add_argument('isOrganizado', type=str, required=True, location='form')
user_properties_parser.add_argument('isExtrovertido', type=str, required=True, location='form')
user_properties_parser.add_argument('isIntrovertido', type=str, required=True, location='form')
user_properties_parser.add_argument('isResponsavel', type=str, required=True, location='form')
user_properties_parser.add_argument('gostaDeAnimais', type=str, required=True, location='form')
user_properties_parser.add_argument('emailUser', type=str, required=True, location='form')


    
@api.route('/housin/set-properties')
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
        
        return 200
    
house_parser = reqparse.RequestParser()
house_parser.add_argument('cidade', type=str, required=True, location='form') 
house_parser.add_argument('bairro', type=str, required=True, location='form') 
house_parser.add_argument('numero', type=str, required=True, location='form') 
house_parser.add_argument('qtdMoradores', type=int, required=True, location='form') 
house_parser.add_argument('animais', type=bool, required=True, location='form') 
house_parser.add_argument('tipo', type=str, required=True, location='form') 
house_parser.add_argument('imgBytes', type=str, required=True, location='form') 
house_parser.add_argument('emailDono', type=str, required=True, location='form') 

@api.route('/housin/create-house')
class CreateHouse(Resource):
    
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
            'emailDono': data['emailDono'],
        }
        
        
        if(facade.create_house(properties)):
            return 200
        else:
            return 400

   
app.run(debug=True)