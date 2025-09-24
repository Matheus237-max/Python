while True:

    numero = input('Digite um número entre 0 e 10:')
    numero = int(numero)

    if numero > 10:
        print('Número inválido. Tente novamente.')
        break
    else:
        print('Número válido')
        break
