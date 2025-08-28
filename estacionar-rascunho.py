import datetime

carrosEstacionados = []

def addCarro():
    placa = input("Digite a placa: ").upper()
    cor = input("Digite a cor do veiculo: ")
    modelo = input("Digite o modelo do veiculo: ")

    for carro in carrosEstacionados:
        if carro['placa'] == placa:
            print("Carro Ja Cadastrado")
            break

    hora = datetime.datetime.now()
    horaFormatada = hora.strftime("%H:%M")

    carro = {
        "placa": placa,
        "cor": cor,
        "modelo": modelo,
        "horarioEntrada": horaFormatada,
    }


    carrosEstacionados.append(carro)
    print(carrosEstacionados)


def consultarCarros():

    decisao = input("O Que deseja consultar? \n 1 - Carro pela placa \n 2 - Todos os veiculos estacionados \n")

    if decisao == "1":

        placa = input("Digite a placa: ").upper()

        for carro in carrosEstacionados:
            if carro['placa'] == placa:
                print(f"Placa: {carro['placa']} | Modelo: {carro['modelo']} | Cor: {carro['cor']} | Entrada: {carro['horarioEntrada']}")
    elif decisao == "2":
        for carro in carrosEstacionados:
            print(f"Placa: {carro['placa']} | Modelo: {carro['modelo']} | Cor: {carro['cor']} | Entrada: {carro['horarioEntrada']}")



addCarro()
addCarro()

consultarCarros()
consultarCarros()


def calcularValor(horaEntrada):
    hora = datetime.datetime.now()
    horaFormatada = hora.strftime("%H:%M")

    horaPermanencia = horaEntrada - horaFormatada
    totalSegundos = horaPermanencia.total_seconds()

    print(f"Total de horas: {totalSegundos}")

