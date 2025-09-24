num1 = int(input('Digite o 1º número:'))
op = input('Digite a operação matemática:(+ , - , /, *)')
num2 = int(input('Digite o 1º número: '))

if op == '+':
    resultadoSoma = num1 + num2
    print(f'O resultado é: {resultadoSoma}')
elif op == '-':
    resultadoSub = num1 - num2
    print(f'O resultado é : {resultadoSub}')
elif op == '/':
    resultadoDiv = num1 / num2
    print(f'O resultado é: {resultadoDiv}')
elif op == '-':
    resultadoMul = num1 * num2
    print(f'O resultado é : {resultadoMul}')

else:
    print("Deu Erro!")
