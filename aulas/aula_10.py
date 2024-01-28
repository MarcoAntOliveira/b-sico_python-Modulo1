nome = "Marcos Antonio"
altura = 1.80
peso = 95
imc = ...

imc = peso/(altura**2)
linha_1= f'{nome} tem {altura:,.2f} de altura'
linha_2 = f'pesa {peso:.2f} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(imc)