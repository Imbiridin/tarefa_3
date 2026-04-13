salario = int(input("Informe o seu salário: "))

if salario < 280:
    salario_1 = (salario / 100) * 20
    print("O seu aumento é de 20%")
elif salario < 700:
    salario_1 = (salario / 100) * 15
    print("O seu aumento é de 15%")
elif salario < 1500:
    salario_1 = (salario / 100) * 10
    print("O seu aumento é de 10%")
else:
    salario_1 = (salario / 100) * 5
    print("O seu aumento é de 5%")

print(f'O seu salário é: R${salario}')
print(f'O aumento do seu salário é de {salario_1}')
print(f'O seu novo salário é: R${salario + salario_1}')

