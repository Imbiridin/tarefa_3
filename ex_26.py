print("-" * 50)
print("Preço da G-gasolina: R$2,50")
print("Preço do A-álcool: R$1,90")
print("-" * 50)

pedido = input("Qual dos combustíveis você gostaria?(G-gasolina)(A-álcool): " ).lower()
litro = float(input("Quantos litros de combustível você gostaria de colocar?: "))

gasolina = 2.5
alcool = 1.9
total = 0

if pedido == 'g':
    if litro <= 20:
        total = (litro * gasolina)
        desconto = (gasolina * litro) * 0.04
        total_desc = total - desconto
if pedido == 'g':
    if litro >= 20:
        total = (litro * gasolina)
        desconto = (gasolina * litro) * 0.06
        total_desc = total - desconto

if pedido == 'a':
    if litro <= 20:
        total = (litro * alcool)
        desconto = (alcool * litro) * 0.03
        total_desc = total - desconto
if pedido == 'a':
    if litro >= 20:
        total = (litro * alcool)
        desconto = (alcool * litro) * 0.05
        total_desc = total - desconto

print("-" * 50)
print(f'O total da gasolina é: R${total}')
print(f'O desconto é: R${desconto}')
print(f'Total a pagar: R${total_desc}')
print("-" * 50)