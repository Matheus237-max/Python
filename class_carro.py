#class = Palavra chave no python para definir uma classe

#Carro = Nome que damos à classe. Por covenção começa com letra Maiúscula se for nome composto, usamos CamelCase Ex: MinhaCasa



class Carro:
    #def = palavra chave que define uma função ou método no Python
    #__init__ = método construtor da classe. Ele é chamado do automaticamente quando criamos a classe com um novo objeto. Serve para inicializar atributos do objeto
    #self = Uma referênca ao próprio objeto que está sendo criado

    def __init__(self,marca, modelo):
       self.marca = marca
       self.modelo = modelo

    def acelerar(self):
           print(f"O carro {self.marca} {self.modelo} está acelerando")

        
# Criando dois objetos diferentes
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")
carro3 = Carro("Mercedes","Gla")

# Chamando métodos
carro1.acelerar() #Usa os atributos do carro1
carro2.acelerar() #Usa os atributos do carro2
carro3.acelerar() 
    

    