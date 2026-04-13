num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if num_1 > num_2 and num_3:
    print(f"O maior número é {num_1} e o menor número é {min(num_2, num_3)}")
elif num_3 > num_2 and num_1:
    print(f"O maior número é {num_3} e o menor número é {min(num_2, num_1)}")
else:
    print(f"O maior número é {num_2} e o menor número é {min(num_1, num_3)}")