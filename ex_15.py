lado_1 = float(input("Digite o primeiro lado do triângulo: "))
lado_2 = float(input("Digite o segundo lado do triângulo: "))
lado_3 = float(input("Digite o terceiro lado do triângulo: "))

if lado_1 == lado_2 and lado_1 == lado_3:
    print("É um Triângulo Equilátero")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("É um Triângulo Isósceles")
else: 
    print("É um Triângulo Escaleno")