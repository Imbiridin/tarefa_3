compra_f = input("Digite a fruta que gostaria de comprar: ").lower()
compra_kg = float(input("Informe quantos kilos gostaria de levar: "))

total = 0

if compra_f == 'maçã':
    if compra_kg < 5:
        maca = 1.80
        total = maca * compra_kg
    elif compra_kg >= 5:
            maca = 1.50
            total = maca * compra_kg


if compra_f == 'morango':
    if compra_kg < 5:
        morango = 2.50
        total = morango * compra_kg
    elif compra_kg >= 5:
            morango = 2.20
            total = morango * compra_kg

if compra_kg > 25 or total >= 25:
   valor_pagar = total * 0.90
   print(f'A compra do seu produto deu: R${valor_pagar:.2f}') 


