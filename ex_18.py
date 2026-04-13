dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

if dia > 31:
    print("Esse dia não existe!")
elif mes > 12:
    print("Não existe esse mês!")
else:
    print(f"Data {dia}/{mes}/{ano}")