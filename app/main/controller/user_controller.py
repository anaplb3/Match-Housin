from flask import Flask, jsonify, Blueprint, request
from flask_restplus import Resource, Namespace
from ..service.user_service import UserService
from .model_factory import ModelFactory

api = Namespace('Usuário', 'Operações relacionadas aos usuários')

facade = UserService()
model_factory = ModelFactory(api)

@api.route('/caracteristicas')
class Users(Resource):
    user_model = model_factory.user_properties_model()
    
    def get(self, username):

        return jsonify({'result': facade.get_user(username)})

    @api.expect(user_model)
    def post(self, username):
        
        sexo = request.json['sexo']
        limpo = request.json['limpo']
        organizado = request.json['organizado']
        comportamento = request.json['comportamento']
        responsavel = request.json['responsavel']
        gosta_de_animais = request.json['gostaAnimais']
        fuma = request.json['fuma']
        bebe = request.json['bebe']
        
        if facade.create_user_properties(username, sexo, limpo, organizado, comportamento, responsavel, gosta_de_animais, fuma, bebe):
            return jsonify({'result': 'Usuário adicionado!'})
        else:
            return jsonify({'result': 'Usuário já existe!'})

        
        

@api.route('/filmes')
class Filmes(Resource):
    movie_model = model_factory.movie_properties_model()
    def get(self, username):
        return jsonify({'result': facade.get_movie_taste(username)})

    @api.expect(movie_model)
    def post(self, username):

        status = facade.create_movie_taste(username,
        request.json['terror'],
        request.json['suspense'],
        request.json['comedia'],
        request.json['comediaRomantica'],
        request.json['romantico'],
        request.json['ficcaoCientifica'],
        request.json['acao'],
        request.json['anime'],
        request.json['documentario'],
        request.json['drama'],
        request.json['policiais'],
        request.json['besteirolAmericano'])

        if(status):
            return jsonify({'result': 'Gosto cinéfilo adicionado!'})
        else:
            return jsonify({'result': 'Usuário não existe!'})

        


@api.route('/musicas')
class Musicas(Resource):
    musical_model = model_factory.music_properties_model()
    def get(self, username):

        return jsonify({'result': facade.get_musical_taste(username)})

    @api.expect(musical_model)
    def post(self, username):

        status = facade.create_musical_taste(username,
        request.json['pop'],
        request.json['rock'],
        request.json['bregaRecife'],
        request.json['funk'],
        request.json['mpb'],
        request.json['indie'],
        request.json['eletronica'],
        request.json['hipHop'],
        request.json['rap'],
        request.json['metal'],
        request.json['jazz'],
        request.json['folk'],
        request.json['rb'],
        request.json['classica'])

        if(status):
            return jsonify({'result': 'Gosto musical criado!'})
        else:
            return jsonify({'result': 'Usuário não existe!'})

        


@api.route('/livros')
class Livros(Resource):
    def get(self, username):
        return jsonify({'teste': 'teste'})


    def post(self):
        return jsonify({'teste': 'teste'})


@api.route('/jogos')
class Jogos(Resource):
    def get(self, username):
        return jsonify({'teste': 'teste'})


    def post(self):
        return jsonify({'teste': 'teste'})