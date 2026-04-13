dia_semana = (int(input("Digite de 1-7 para saber o dia da semana: ")))

match dia_semana:
    case 1:
        print('Domingo')
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sábado")
    case _:
        print("Inválido")