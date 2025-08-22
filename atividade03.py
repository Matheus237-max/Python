valorcompra=float(input(' Digite o valor da compra do cliente: '))

if valorcompra >=100:
    desconto=float((valorcompra/10))
    print(' Valor da compra com desconto é: ', desconto)
else:
    print(' Valor da compra sem desconto: ', valorcompra)