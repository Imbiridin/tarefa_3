print("-" * 50)
print("SERÁ QUE VOCÊ É O ASSASSINO ?")
print("-" * 50)
perg_1 = input("Telefonou para a vítima?(s/n): ").lower()
perg_2 = input("Esteve no local do crime?(s/n): ").lower()
perg_3 = input("Mora perto da vítima?(s/n): ").lower()
perg_4 = input("Devia a vítima?(s/n): ").lower()
perg_5 = input("Já trabalhou com a vítima?(s/n): ").lower()

pontos = 0

if perg_1 == 's':
    pontos += 1
    if perg_2 == 's':
        pontos += 1
    if perg_3 == 's':
        pontos += 1
    if perg_4 == 's':
        pontos += 1
    if perg_5 == 's':
        pontos += 1

if pontos == 2:
    print("Você é SUSPEITO")
elif pontos >= 3 and pontos <=4:
    print("Você é CÚMPLICE")
elif pontos == 5:
    print("Você está preso ASSASSINO")
else:
    print("Ta liberado INOCENTE")