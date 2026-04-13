saque = float(input("Digite o valor que você gostaria de sacar: "))

nota_100 = 0
nota_50 = 0
nota_10 = 0
nota_5 = 0
nota_1 = 0

print(f'Para sacar o valor de: R${saque}')

if saque >= 100:
    nota_100 = saque // 100
    saque = saque % 100

if saque >= 50:
    nota_50 = saque // 50
    saque %= 50

if saque >= 10:
    nota_10 = saque // 10
    saque %= 10

if saque >= 5:
    nota_5 = saque // 5
    saque %= 5

nota_1 = saque

print("=" *50)
print(f"O programa oferece: \n"
       f"{nota_100:.0f} notas de R$100.\n"
       f"{nota_50:.0f} notas de R$50.\n" 
       f"{nota_10:.0f} notas de R$10.\n" 
       f"{nota_5:.0f} notas de R$5.\n" 
       f"{nota_1:.0f} notas de R$1.")
print("="*50)