
class Carro:
    

    def __init__(self,marca,modelo,cor,ano):
       self.marca = marca
       self.modelo = modelo
       self.cor = cor
       self.ano = ano

    def acelerar(self):
           print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está acelerando")

    def frear(self):
           print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está freiando")


        
carro1 = Carro("Toyota", "Corolla", " Vermelho", "2010")
carro2 = Carro("Honda", "Civic", "Azul", "2010")
carro3 = Carro("Mercedes","Gla", "Laranja", "2013")


carro1.acelerar() 
carro2.acelerar() 
carro3.acelerar()

carro1.frear() 
carro2.frear() 
carro3.frear()
    