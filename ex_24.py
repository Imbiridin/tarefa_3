num_1 = float(input("DIgite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))

total = 0

pergunta = input("Qual operação você gostaria de fazer: +, -, * ou / ?: ")

if pergunta == '+':
    total = num_1 + num_2
    print(f'{total}')

    if total % 2 == 0:
        print(f'{total} é par')
    else:
        print(f"{total} é ímpar")

    if total > 0:
        print(f'{total} é positivo')
    else:
        print(f'{total} é negativo')

    if total % 1 == 0:
        print(f'{total} é um número inteiro')
    else:
        print(f'{total} é um número decimal')


if pergunta == '-':
    total = num_1 - num_2
    print(f'{total}')
    
    if total % 2 == 0:
        print(f'{total} é par')
    else:
        print(f"{total} é ímpar")

    if total > 0:
        print(f'{total} é positivo')
    else:
        print(f'{total} é negativo')

    if total % 1 == 0:
        print(f'{total} é um número inteiro')
    else:
        print(f'{total} é um número decimal')

if pergunta == '*':
    total = num_1 * num_2
    print(f'{total}')
    
    if total % 2 == 0:
        print(f'{total} é par')
    else:
        print(f"{total} é ímpar")

    if total > 0:
        print(f'{total} é positivo')
    else:
        print(f'{total} é negativo')

    if total % 1 == 0:
        print(f'{total} é um número inteiro')
    else:
        print(f'{total} é um número decimal')


if pergunta == '/':
    total = num_1 / num_2
    print(f'{total}')
    
    if total % 2 == 0:
        print(f'{total} é par')
    else:
        print(f"{total} é ímpar")

    if total > 0:
        print(f'{total} é positivo')
    else:
        print(f'{total} é negativo')

    if total % 1 == 0:
        print(f'{total} é um número inteiro')
    else:
        print(f'{total} é um número decimal')



    