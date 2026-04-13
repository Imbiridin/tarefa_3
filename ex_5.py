nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input("DIgite a segunda nota do aluno: "))

media = (nota_1 + nota_2) / 2

if media == 10:
    print(F'A nota do aluno é: {media}. Aluno APROVADO COM DISTINÇÃO!')
elif media >= 7:
    print(f'A nota do aluno é: {media}. Aluno APROVADO!')
else:
    print(f"A nota do aluno é: {media}. Aluno REPROVADO!")
