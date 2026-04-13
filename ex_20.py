nota_1 = float(input("Digite a primeira nota do aluno: "))
nota_2 = float(input("Digite a segunda nota do aluno: "))
nota_3 = float(input("Digite a terceira nota do aluno: "))

media = (nota_1 + nota_2 + nota_3) / 3

print("-" * 50)
print(f"MÉDIA DO ALUNO: {media:.2f}")
print("-" * 50)

if media == 10:
    print(f'{media} APROVADO COM DISTINÇÃO')
elif media >= 7:
    print(f'{media:.2f} APROVADO')
else:
    print(f'{media:.2f} REPROVADO')

print("-" * 50)