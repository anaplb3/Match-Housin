from py2neo import Graph, Node, Relationship, NodeMatcher
from models import User, House

class Facade:
    def __init__(self):
        self.graph = Graph(host='localhost', port='7687', user='neo4j', password='admin')

    def create_user(self, user):
        node = Node("User", name=user.nome, nTelefone=user.n_telefone, email=user.email, senha=user.senha)
        self.graph.create(node)

    
    def set_user_properties(self, email, properties):
        matcher = NodeMatcher(self.graph)
        node = matcher.match("User", email=email).first()

        if(node != None):
            node['sexo'] = properties['sexo']
            node['isLimpo'] = properties['is_limpo']
            node['isOrganizado'] = properties['is_organizado']
            node['isExtrovertido'] = properties['is_extrovertido']
            node['isIntrovertido'] = properties['is_introvertido']
            node['isResponsavel'] = properties['is_responsavel']
            node['gostaDeAnimais'] = properties['gosta_de_animais']

            self.graph.push(node)
            
    def create_house(self, properties):
        node = Node('House', cidade=properties['cidade'], bairro=properties['bairro'], numero=properties['numero'], qtdMoradores=properties['qtdMoradores'], possuiAnimais=properties['animais'], tipoMoradia=properties['tipo'], imgBytes=properties['imgBytes'], emailDono=properties['emailDono'])
        self.graph.create(node)
        status = self.create_ownership(properties['emailDono'], node)
        return status

    
    def get_user(self, email):
        matcher = NodeMatcher(self.graph)
        node = matcher.match("User", email=email).first()
        return node
    
    def get_house(self, email_dono, house):
        matcher = NodeMatcher(self.graph)
        node = matcher.match('House', emailDono=email_dono).first()
        return node

    #ajeitar o get user daqui
    def create_match(self, user1, user2):
        relationship = Relationship(self.get_user(user1), "matches", self.get_user(user2))
        relationship['compatibility'] = user1.compare_users(user2)
        self.graph.create(relationship)
    
    def create_ownership(self, email_dono, house):
        user = self.get_user(email_dono)
        if (user != None):
            relationship = Relationship(user, "possui", house)
            self.graph.create(relationship)
            return True
        else:
            return False
        