distancia = int(input("Digite a distância total percorrida (em Km): "))
litros = float(input("Digite o total de combustível gasto (em litros): "))

consumo_medio = distancia / litros

print(f"{consumo_medio:.3f} km/l")
