import random
 
numero = random.randint (1,5)

tentativa = 0

while tentativa <5:
    palpite = int(input("Digite o seu palipte 1 até o 5: "))
    tentativa +=1

    if palpite == numero:
        print (" Você acertou o numero")
        break   
    elif palpite < numero:
        print (" O numero é menor")
    else:
        print(" O numero é maior")

if palpite != numero:
     print("f Fim de jogo! O número era {numero}")