print("-" * 50)
print("CALCULO DE SEGUNDO GRAU")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))






if a == 0:
    print("Inválido")
else: 
    delta = (b**2) - (4*a*c)

    
    if delta < 0:
        print(f"A equação não possui raizes reais. O valor é {delta}")
    elif delta == 0:
        print("A equação possui apenas uma raiz real")
    else:
        x_1 = ((-b + delta ** 0.5)) / (2*a)
        x_2 = ((-b - delta ** 0.5)) / (2*a)
        print(f"a equação possui duas raiz reais. O valor é {x_1:.0f} e {x_2:.0f}")



