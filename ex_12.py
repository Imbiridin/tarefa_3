hora_t = float(input("Informe a sua Hora Trabalhada no mês: "))
valor_h = float(input("informe o quanto você ganha por hora: "))

salario_bruto = hora_t * valor_h

if salario_bruto <= 900:
    print('Você está insento de imposto')
elif salario_bruto <= 1500:
    desconto = (salario_bruto / 100) * 5
elif salario_bruto <= 2500:
    desconto = (salario_bruto / 100) * 10
else:
    desconto = (salario_bruto / 100) * 20

ir = (salario_bruto / 100) * 5
inss = (salario_bruto / 100) * 10
sindicato = (salario_bruto / 100) * 3
salario_liquido = (salario_bruto - desconto - ir - inss - sindicato)

print("-" * 50)
print(f'O seu salário bruto é: R${salario_bruto}')
print(f'O desconto do seu IR é: R${ir}')
print(f'O desconto do seu INSS é: R${inss}')
print(f'O desconto do seu sindicato é: R${sindicato}')
print(f'O seu salário líquido é: R${salario_liquido}')
print("-" * 50)