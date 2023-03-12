import os

carros = [
    ("BMW", 180),
    ("RENEGADE", 150),
    ("SPIN", 130),
    ("HB20", 99),
    ("ONIX", 99),
    ("MOBI", 79),
    ("UP", 79)
]

alugados = []

def mostrar_lista_carros(lista_carros):
        for i, car in enumerate(lista_carros):
           print("[{}] {} - R$ {} dia".format(i,car[0], car[1]))     
        
mostrar_lista_carros(carros)

while True:
    os.system("clear")
    print("===================")
    print("Seja Benvindo a Locacar!!")
    print("===================")
    print("Escolha um serviço")
    print("0 - Mostrar Portifólio | 1 - Alugar um Carro | 2 - Devolver um Carro")
    op = int(input())

    os.system("clear")

    if op == 0:
        mostrar_lista_carros(carros)        

    elif op == 1:
        mostrar_lista_carros(carros)
        print("===================")
        print("Escolha o codigo do carro:")
        cod_car = int(input())
        print("Por quantos dias você deseja alugar este carro?")
        dias = int(input())
        os.system("clear")

        print("Sua ecolha é o {} por {} dias".format(carros[cod_car] [0], dias))
        print("O alugal totalizara R$ {} Deseja alugar?".format(dias * carros[cod_car][1]))

        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
             print("Parabens você alugar o {} por {} dias".format(carros[cod_car] [0], dias))
             alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
            print("Não ha carros para devolver!")
        else:
            print("===================")
            print("Escolha o codigo do carro que deseja devolver:")
            mostrar_lista_carros(alugados)
            cod = int(input())
            if conf == 0:
                print("Obrigado por devolver o carro {}".format(alugados[cod][0]))
                carros.append(alugados.pop(cod))        
    
    print("")
    print("===================")
    print("DIGITE 0 para Continuar | 1 para SAIR")
    if int(input()) == 1:
         break

    

    

