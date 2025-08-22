severidade = int (input("Digite o nível da severidade: (1 a 5)"))
probabilidade = int ( input("Digite o nível da probalidade ()1 a 5"))

if severidade > 3 and probabilidade > 3:
    print ("Risco de Alta Prioridade")
elif severidade > 3 or probabilidade > 3:
    print ("Risco de média prioridade")
else:
    print (" Risco de baixa prioridade")