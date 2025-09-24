soma = 0

numero = int(input('Digite o número inteiro(0 para sair): '))

while numero !=0:
    soma +=numero
    numero = int(input('Digite o número inteiro(0 para sair): '))
print(f'a soma dos números é: {soma}')