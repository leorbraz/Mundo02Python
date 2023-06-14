from datetime import date
atual = date.today().year

nascimento = int(input("Digite o seu ano de nascimento: "))
idade = atual - nascimento

print('O atleta tem {} anos.' .format(idade))

if idade <= 9:
    print("Você faz parte da categoria: MIRIM")

elif idade <= 14:
    print("Você faz parte da categoria: INFANTIL")

elif idade <= 19:
    print("Vocêfaz parte da categoria: JUNIOR")

elif idade <= 25:
    print("Você faz parte da categoria: SÊNIOR") 

else: 
    print("Você faz parte da categoria: MASTER")
