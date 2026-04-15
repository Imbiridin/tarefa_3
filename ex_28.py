compra = input("Digite o nome do produto: ").lower()
kilo = float(input("Informe quantos kilos você quer levar :"))
cartao = input("Gostaria de realizar como o pagamento D/C/CT: ").lower()

if compra == 'file duplo':
    if kilo < 5:
        file_duplo = 4.90
        total = file_duplo * kilo
    elif kilo >= 5:
        file_duplo = 5.80
        total = file_duplo * kilo
if compra == 'alcatra':
    if kilo < 5:
        alcatra = 5.90
        total = alcatra * kilo
    elif kilo >= 5:
        alcatra = 6.80
        total = alcatra * kilo
if compra == 'picanha':
    if kilo < 5:
        picanha = 6.90
        total = picanha * kilo
    elif kilo >= 5:
        picanha = 7.80
        total = picanha * kilo


print(f'O que você comprou: {compra}')
print(f'A quantidade de kg é: {kilo}')
print(f'O total da compra: R${total:.2f}')

if cartao == 'ct':
    valor_pagar = total * 0.95
    print(f'O desconto com o cartão tabajaras é: R${valor_pagar:.2f}')