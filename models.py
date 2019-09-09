class User:
    def __init__(self, nome, n_telefone, email, senha, username):
        self.nome = nome
        self.email = email
        self.username = username
        self.n_telefone = n_telefone
        self.senha = senha
        self.sexo = None
        self.is_limpo = None
        self.is_organizado = None
        self.is_extrovertido = None
        self.is_introvertido = None
        self.is_responsavel = None
        self.gosta_de_animais = None

    def set_atributes(self, sexo, is_limpo, is_organizado, is_extrovertido, is_introvertido, is_responsavel, gosta_de_animais):
        self.sexo = sexo
        self.is_limpo = is_limpo
        self.is_organizado = is_organizado
        self.is_extrovertido = is_extrovertido
        self.is_introvertido = is_introvertido
        self.is_responsavel = is_responsavel
        self.gosta_de_animais = gosta_de_animais

    def compare_users(self, user):

        count = 0

        count += self.compare_atributes(self.is_limpo, user.is_limpo)
        count += self.compare_atributes(self.is_organizado, user.is_organizado)
        count += self.compare_atributes(self.is_extrovertido, user.is_extrovertido)
        count += self.compare_atributes(self.is_introvertido, user.is_introvertido)
        count += self.compare_atributes(self.is_responsavel, user.is_responsavel)
        count += self.compare_atributes(self.gosta_de_animais, user.gosta_de_animais)

        return count
    
    def compare_atributes(self, atr1, atr2):
        if atr1 == atr2:
            return 1
        else:
            return 0


class House:
    def __init__(self, cidade, bairro, numero, qtd_moradores, animais, tipo, img_bytes, username_dono):
        self.cidade = cidade
        self.bairro = bairro
        self.numero = numero
        self.qtd_moradores = qtd_moradores
        self.animais = animais
        self.tipo = tipo
        self.img_bytes = img_bytes
        self.username_dono = username_dono
