class ContaBancaria:
    def __init__(self, titular, saldo_inicial, senha):
        self.titular = titular
        self._saldo = float(saldo_inicial)
        self.__senha = str(senha)
    
    def ver_saldo(self, senha_digitada):
        if senha_digitada == self.__senha:
            print(f"Saldo de {self.titular}: R${self._saldo:.2f}")
        else:
            print("Senha incorreta! Acesso negado.")

conta2 = ContaBancaria("Matheus", 120000.00, "5943")

conta2.ver_saldo("5943")

conta2.titular = "Sara Atualizado"
conta2.ver_saldo("1234")

conta2._saldo = 50.00
conta2.ver_saldo("1234")

#Tentando alterar privado (não funciona)
try:
    print(conta2.__senha)
except AttributeError:
    print("Atributo privado não pode ser acessado diretamente") 


   




   
