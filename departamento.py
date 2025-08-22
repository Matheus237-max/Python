departamento = input("Digite o nome do departamento: ").strip().lower()

if departamento == "desenvolvimento de software":
    print("Recomendação: Laptop de alto desempenho.")
elif departamento == "marketing":
    print("Recomendação: Tablet para apresentações e mobilidade.")
elif departamento == "recursos humanos":
    print("Recomendação: Computador desktop pela estabilidade e custo-benefício.")
elif departamento == "pesquisa e desenvolvimento" or departamento == "p&d":
    print("Recomendação: Equipamento com especificações de última geração.")
else:
    print("Departamento não reconhecido. Por favor, verifique a digitação.")
 