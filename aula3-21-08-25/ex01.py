nota1 = float(input("Digite a nota 1: ")) #defini nota1 como variavel global, ela vai receber um float de um input do terminal
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3 # variavel media vai receber o calculo das notas

print(f"A Média é {media:.1f}")