febre = input ("Você está com febre? (s/n)")

if febre == "s":
    dor_de_cabeca = input ("Você está com dor de cabeça (s/n)")
    if dor_de_cabeca =="s":
        print ("Possível diagnóstico: Gripe!")
    else:
     print("Possível diagnóstico: infecção leve.")
else:
   coriza = input ("Você está com coriza? (s/n)")
   if coriza == "s":
      print ("Possível resfriado comum.")
   else:
      print ("Possível diagnóstico: estado normal ou outra condição")

    
   

