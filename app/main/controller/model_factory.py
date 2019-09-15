from flask_restplus import fields

class ModelFactory:
    def __init__(self, api):
        self.api = api

    def user_properties_model(self):
        users_model = self.api.model('Users model', {
            'sexo': fields.String(required = True,
            description = 'Username do usuário'),
            'limpo': fields.Boolean(required = True,
            description = 'O usuário se considera limpo?'),
            'organizado': fields.Boolean(required=True,
            description='O usuário se considera organizado?'),
            'comportamento': fields.String(required=True,
            description='O usuário é introvertido ou extrovertido?'),
            'responsavel': fields.Boolean(required=True,
            description='O usuário se considera responsável?'),
            'gostaAnimais': fields.Boolean(required=True,
            description='O usuário gosta de animais?'),
            'fuma': fields.Boolean(required=True,
            description='O usuário fuma?'),
            'bebe': fields.Boolean(required=True,
            description='O usuário bebe?')
        })

        return users_model

    def music_properties_model(self):
        musical_model = self.api.model('Musical model', {
            'pop': fields.Boolean(required=True,
            description='O usuário gosta de pop?'),
            'rock': fields.Boolean(required=True,
            description='O usuário gosta de rock?'),
            'bregaRecife': fields.Boolean(required=True,
            description='O usuário gosta de brega recife?'),
            'funk': fields.Boolean(required=True,
            description='O usuário gosta de funk?'),
            'mpb': fields.Boolean(required=True,
            description='O usuário gosta de mpb?'),
            'indie': fields.Boolean(required=True,
            description='O usuário gosta de indie?'),
            'eletronica': fields.Boolean(required=True,
            description='O usuário gosta de eletronica?'),
            'hipHop': fields.Boolean(required=True,
            description='O usuário gosta de hip hop?'),
            'rap': fields.Boolean(required=True,
            description='O usuário gosta de rap?'),
            'metal': fields.Boolean(required=True,
            description='O usuário gosta de metal?'),
            'jazz': fields.Boolean(required=True,
            description='O usuário gosta de jazz?'),
            'folk': fields.Boolean(required=True,
            description='O usuário gosta de folk?'),
            'rb': fields.Boolean(required=True,
            description='O usuário gosta de R&B?'),
            'classica': fields.Boolean(required=True,
            description='O usuário gosta de música clássica?')
        })

        return musical_model

    def movie_properties_model(self):
        movie_model = self.api.model('Movie model', {
            'terror': fields.Boolean(required=True,
            description='O usuário gosta de filmes de terror?'),
            'suspense': fields.Boolean(required=True,
            description='O usuário gosta de filmes de suspense?'),
            'comedia': fields.Boolean(required=True,
            description='O usuário gosta de filmes de comédia?'),
            'comediaRomantica': fields.Boolean(required=True,
            description='O usuário gosta de filmes de comédia romântica?'),
            'romantico': fields.Boolean(required=True,
            description='O usuário gosta de filmes de romance?'),
            'ficcaoCientifica': fields.Boolean(required=True,
            description='O usuário gosta de filmes de ficção científica?'),
            'acao': fields.Boolean(required=True,
            description='O usuário gosta de filmes de ação?'),
            'anime': fields.Boolean(required=True,
            description='O usuário gosta de animes?'),
            'documentario': fields.Boolean(required=True,
            description='O usuário gosta de documentários?'),
            'drama': fields.Boolean(required=True,
            description='O usuário gosta de filmes de drama?'),
            'policiais': fields.Boolean(required=True,
            description='O usuário gosta de filmes policiais?'),
            'besteirolAmericano': fields.Boolean(required=True,
            description='O usuário gosta de filmes de besteirol americano?'),
        })
        return movie_model
        