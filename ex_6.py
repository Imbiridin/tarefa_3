num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if num_1 > num_2 and num_3:
    print(f'O número {num_1} é o maior dentre os demais!')
elif num_3 > num_1 and num_2:
    print(f'O número {num_3} é o maior dentre os demais!')
else:
    print(f'O número {num_2} é o maior dentre os demais!')
    