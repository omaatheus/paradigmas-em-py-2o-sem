from datetime import datetime

print("Bem Vindo ao Estacionar!")

bancoDeCarros = []

placa = str(input("Insira o placa: "))


horaEntrada = input("Insira o horário de entrada (HH:MM): ")

today = datetime.today().date()
horaEntrada = datetime.strptime(horaEntrada, "%H:%M").time()

horaEntrada = datetime.combine(today, horaEntrada)

print(horaEntrada)

print("Selecione uma opção:")
opcao = int(input("==========================================================\n 1 - Cadastrar nova placa\n 2 - Consultar tempo estacionado\n 3 - Dar baixa em um veiculo estacionado\n ==========================================================\n"))

