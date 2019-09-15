from py2neo import Graph, Node, NodeMatcher, Relationship
from app.main import db

class UserService:
    def __init__(self):
        self.matcher = NodeMatcher(db)

    def get_user(self, username):
        node = self.matcher.match('User', username=username).first()
        return node

    def create_user_properties(self, username, sexo, limpo, organizado, comportamento, responsavel, gosta_animais, fuma, bebe):
        if self.get_user(username) == None:
            node = Node("User", username=username, sexo=sexo, limpo=limpo, organizado=organizado, comportamento=comportamento, responsavel=responsavel, gostaDeAnimais=gosta_animais, fuma=fuma, bebe=bebe)
            db.create(node)
            return True
        else:
            return False
    
    def create_musical_taste(self, username, pop, rock, brega_recife, funk, mpb, indie, eletronica, hip_hop, rap, metal, jazz, folk, r_b, classica):
        musical_taste = Node('Musical', usernameDono = username, pop=pop, rock=rock, bregaRecife=brega_recife, funk=funk, mpb=mpb, indie=indie, eletronica=eletronica, hipHop=hip_hop, rap=rap, metal=metal, jazz=jazz, folk=folk, rb=r_b, classica=classica)
        user = self.get_user(username)
        if (user != None):
            musical_taste = Relationship(user, "temGosto", musical_taste)
            db.create(musical_taste)
            return True
        else:
            return False

    
    def get_musical_taste(self, username):
        return self.matcher.match('Musical', usernameDono=username).first()

    
    def create_movie_taste(self, username, terror, suspense, comedia, comedia_romantica, romantico, ficcao_cientifica, acao, anime, documentario, drama, policiais, besteirol_americano):
        movie_taste = Node('Cinefilo', usernameDono = username, terror=terror, suspense=suspense, comedia=comedia, comediaRomantica=comedia_romantica, romantico=romantico, ficcaoCientifica=ficcao_cientifica, acao=acao, anime=anime, documentario=documentario, drama=drama, policiais=policiais, besteirolAmericano=besteirol_americano)
        user = self.get_user(username)
        if (user != None):
            movie_taste = Relationship(user, "temGosto", movie_taste)
            db.create(movie_taste)
            return True
        else:
            return False

    def get_movie_taste(self, username):
        return self.matcher.match('Cinefilo', usernameDono=username).first()
        