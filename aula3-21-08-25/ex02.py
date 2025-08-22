altura = float(input("Insira a altura em metros: "))

peso = float(input("Insira o peso: "))

imc = peso / (altura **2)

if imc < 18.5:
    print(f"Seu imc é de: {imc:.1f}, você está em status de Magreza")
elif (imc >= 18.5) and (imc <= 24.9):
    print(f"Seu imc é de: {imc:.1f}, você está no status Normal")
elif (imc >= 25) and (imc <= 29.9):
    print(f"Seu imc é de: {imc:.1f}, você está no status Sobrepeso")
elif (imc >= 30) and (imc <= 34.9):
    print(f"Seu imc é de {imc:.1f}, você está no status Obesidade Grau I")
elif (imc >= 35) and (imc <= 39.9):
    print(f"Seu imc é de {imc:.1f}, você está no status Obesidade Grau II")
else:
    print(f"Seu imc é de {imc:.1f}, você está no status Obesidade Grau III")