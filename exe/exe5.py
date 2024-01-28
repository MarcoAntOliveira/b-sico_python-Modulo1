"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input("Digite um numero inteiro: ")

try:
    num_int = int(num)    
    test1= num_int % 2 == 0
    if(test1):
        print("Este numero é par")
    else:
        print("Este numero é impar")    
except:
    print('Este não é um numero inteiro ou não é um numero')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora1 = input('Digite a hora: ')
try:
    hora = int(hora1)
    manha = hora >= 0 and hora <= 11
    tarde = hora >= 12 and hora <=17
    noite = hora >= 12 and hora <=17
    if(manha):
        print('Bom Dia')
    elif(tarde):
        print('Boa tarde')
    elif(noite):
        print('Boa Noite')
except:
    print("você não digitou um numero inteiro")                

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('escreva o seu primeiro nome: ')
if nome:
    tam = len(nome)
    curto = tam<=4
    normal = tam >= 5 and tam <= 6
    grande = tam > 6
    if(curto):
        print('Seu nome é curto')
    elif(normal):
        print('Seu nome é normal')  
    elif(grande):
        print('Seu nome é grande')   
else:
    print('por favor digite alguma coisa')           