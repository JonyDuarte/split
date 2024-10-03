nome_completo = input("Informe seu nome completo: ")

nome_completo_lista = nome_completo.split(" ")

print("Nome completo :", end="")
for nome in nome_completo_lista:
    print(nome.capitalize(), end=" ")