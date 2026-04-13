nota_1 = float(input("Digite a primeira nota do aluno: "))
nota_2 = float(input("Digite a segunda nota do aluno: "))

media = (nota_1 + nota_2) / 2
print(media)

if media == 10 and media >= 9:
    print("A")
    print("APROVADO")
elif media <= 8.9 and media >= 7.5:
    print("B")
    print("APROVADO")
elif media <= 7.4 and media >= 6:
    print("C")
    print("APROVADO")
elif media <= 5.9 and media >= 4:
    print("D")
    print("REPROVADO")
else:
    print("E")
    print("REPROVADO")
