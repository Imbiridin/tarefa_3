numero = int(input("Digite um número: "))

centenas = 0
dezenas = 0
unidades = 0

if numero >= 100:
    centenas = numero // 100
    numero = numero % 100
if numero >= 10:
    dezenas = numero // 10
    numero = numero % 10

unidades = numero


print("*" * 50)
print(f'{numero}')
print(f'{centenas} centenas, {dezenas} dezenas, {unidades} unidades')





