from py2neo import Graph, Node, Relationship, NodeMatcher
from models import User, House

class Facade:
    def __init__(self):
        self.graph = Graph(host='localhost', port='7687', user='ana', password='neo4j')

    def create_user(self, user):
        node = Node("User", name=user.nome, nTelefone=user.n_telefone, email=user.email, senha=user.senha)
        self.graph.create(node)

    
    def set_user_properties(self, user):
        matcher = NodeMatcher(self.graph)
        node = matcher.match("User", email=user.email).first()

        if(node != None):
            node['sexo'] = user.sexo
            node['isLimpo'] = user.is_limpo
            node['isOrganizado'] = user.is_organizado
            node['isExtrovertido'] = user.is_extrovertido
            node['isIntrovertido'] = user.is_introvertido
            node['isResponsavel'] = user.is_responsavel
            node['gostaDeAnimais'] = user.gosta_de_animais

            self.graph.push(node)
            
    def create_house(self, house):
        node = Node('House', cidade=house.cidade, bairro=house.bairro, numero=house.numero, qtdMoradores=house.qtd_moradores, possuiAnimais=house.animais, tipoMoradia=house.tipo, imgBytes=house.img_bytes, emailDono=house.email_dono)
        self.graph.create(node)


    def get_user(self, user):
        matcher = NodeMatcher(self.graph)
        node = matcher.match("User", email=user.email).first()
        return node

    def get_house(self, user, house):
        matcher = NodeMatcher(self.graph)
        node = matcher.match('House', emailDono=user.email).first()
        return node

    def create_match(self, user1, user2):
        relationship = Relationship(self.get_user(user1), "matches", self.get_user(user2))
        relationship['compatibility'] = user1.compare_users(user2)
        self.graph.create(relationship)
    
    def create_ownership(self, user, house):
        relationship = Relationship(self.get_user(user), "possui", self.get_house(user, house))
        self.graph.create(relationship)