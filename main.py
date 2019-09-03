from create import Facade
from models import User, House

facade = Facade()

user = User("Allain Prost", "83991285615", "allain.prost@dcx.ufpb.br", "carbono13")
facade.create_user(user)
user.set_atributes("masculino", "true", "true", "true", "false", "true", "true")
facade.set_user_properties(user)

casa1 = House("Rio Tinto", "Centro", "14", "2", "true", "apartamento", "8273982783", user.email)
facade.create_house(casa1)
facade.create_ownership(user, casa1)

user1 = User("Ana Paula Lima", "83991598843", "ana.paula@dcx.ufpb.br", "h4Ns0l0")
facade.create_user(user1)
user1.set_atributes("feminino", "true", "true", "true", "false", "false", "false")
facade.set_user_properties(user1)

facade.create_match(user, user1)





