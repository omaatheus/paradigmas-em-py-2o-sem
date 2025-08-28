cores = ["Vermelho", "Azul", "verde", "amarelo"]
print(f"{cores} \n")

cores[3] = "Rosa" # sobrescrevo a cor da 4a posição
print(f"{cores} \n")

cores.append("Amarelo") # adiciona algo a mais na lista, mas na ultima posição
print(f"{cores} \n")

cores.insert(0, "Azul") # altera o objeto no indice escolhido
print(f"{cores} \n")

cores.extend(["Azul", "Turquesa"]) # adiciona em lote, mas no fim da lista
print(f"{cores} \n")

cores.remove("Azul") # Remove o azul, o primeiro azul que achar
print(f"{cores} \n")

print(len(cores)) #quantos elementos tem na lista

print(cores.count("Azul")) # exibe quantos Azul tem na lista

print(cores.reverse())

