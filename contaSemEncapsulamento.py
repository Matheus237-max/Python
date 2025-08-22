class contaSemEncapsulamento:
  def __init__(self,titular,saldo,senha):
   
    # Todos são públicos
    self.titular = titular
    self.saldo = saldo
    self.senha = senha

  def ver_saldo(self,senha_digitada):
      #Verifica se a senha está correta
      if senha_digitada == self.senha:
         print(f"Saldo de {self.titular}: R${self.saldo:.2f}")
      else:
         print("Senha Incorreta! Acesso negado.")

    #Teste
conta1 = contaSemEncapsulamento("matheus", 1000, "1234")

conta1.ver_saldo("1234")


#conta1.saldo = 999_999.00
#conta1.senha = "0000"
#conta1.titular = "Novo Titular"

#Consulta com a senha alterada indevimente
#conta1.ver_saldo("0000")

    



