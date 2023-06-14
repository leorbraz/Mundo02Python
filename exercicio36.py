valorCasa = float(input('Informe qual o valor da casa: R$'))
salario = float(input('Informe o valor do seu salário: R$'))
anos = int(input('Em quantos anos você deseja pagar? '))

qntdMeses = anos * 12
prestacaoMensal = valorCasa / qntdMeses
porcentagemSalario = salario*0.3
print('\n30% do salário: {}' .format(porcentagemSalario))
print('Valor da mensalidade {:.2f}' .format(prestacaoMensal))

if prestacaoMensal > (porcentagemSalario):
    print('\nSeu empréstimo não foi aprovado!')

else:
    print('\nSeu empréstimo foi aprovado. Aproveite!')

