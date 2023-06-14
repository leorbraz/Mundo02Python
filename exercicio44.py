valorProduto = float(input('Qual o preço das compras? R$'))

print('\nFORMAS DE PAGAMENTO')
print('[ 1 ] à vista no dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('\nQual é a opção de pagamento? ' ))

if opcao == 1:
    aVista = valorProduto - (valorProduto * 0.1)
    print('Sua compra terá 10% de desconto e sairá pelo valor de R${:.2f}' .format(aVista))

elif opcao == 2:
    cartaoAvista = valorProduto - (valorProduto * 0.05)
    print('Sua compra terá 5% de desconto e sairá pelo valor de R${:.2f}' . format(cartaoAvista))

elif opcao == 3:
    cartao2x = valorProduto / 2
    print('Sua compra sairá pelo valor normal, dividido em 2x de R${:.2f}' .format(cartao2x))

elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    cartaoParcelado = valorProduto + (valorProduto * 0.2)
    valorParcelas = cartaoParcelado / parcelas
    print('Sua compra terá um juros de 20% e sairá valor de R${}, parcelada em {}x de R${}' .format(cartaoParcelado, parcelas, valorParcelas))




