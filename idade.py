dias=int(input("Digite sua idade em dias: "))

anos = dias // 365

dias = dias % 35 

meses = dias //30

dias = dias % 30 

print (f" {anos} ")
print (f" {meses}")
print (f" {dias}")