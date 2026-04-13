numero = float(input("Digite um número para saber se ele é inteiro ou decimal: "))

if numero % 1 == 0:
    print(f'O {numero:.0f} é um número inteiro')
else:
    print(f'O {numero:.1f} é um número decimal')