soma_nota = 0

for i in range (5):
    nota = int(input('Digite a {i}º nota: '))
    soma_nota += nota

media = soma_nota / 5
print (f'A média das 5 notas é: {media}')