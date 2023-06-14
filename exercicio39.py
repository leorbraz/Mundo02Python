from datetime import date
atual = date.today().year

nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
tempo = idade - 18
tempo2 = 18 - idade

print('idade = {} anos' .format(idade))

if idade < 18:
    print("Você ainda deverá se alistar ao serviço militar. Faltam {} anos para se alistar." .format(tempo2))

elif idade == 18:
    print("Está na hora de você se alistar.")

else: 
    print("Já passou do tempo de alistamento. Já se passaram {} anos desde a data de se alistar." .format(tempo))

