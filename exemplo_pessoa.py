from exemplo__carro2 import Carro #importando a classe a Carro

class Pessoa:
    

    def __init__(self, nome,idade,cidade,exemplo__carro2:Carro):
     self.nome = nome
     self.idade = idade
     self.cidade = cidade
     self.exemplo__carro2 = exemplo__carro2
    

    def apresentar (self):
           print(f"Olá meu nome é {self.nome} minha idade é {self.idade} moro em {self.cidade}")
           
        

    def dirigir (self):
           print(f"{self.nome} está dirigindo o {self.exemplo__carro2.marca} {self.exemplo__carro2.modelo} {self.exemplo__carro2.cor} {self.exemplo__carro2.ano}")
           self.exemplo__carro2.acelerar()
        
meu_carro = Carro("Ford", "Fiesta", "vermelho", "1990")
        
Pessoa1 = Pessoa("Fabio", "15 anos", " São Paulo", meu_carro)
#Pessoa2 = Pessoa("Carla", "19 anos", "Santa Catarina")
#pessoa3 = Pessoa("Vitoria","20 anos", "Rio de Janeiro")


Pessoa1.apresentar() 
Pessoa1.dirigir()

