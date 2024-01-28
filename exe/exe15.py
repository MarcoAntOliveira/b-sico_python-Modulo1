"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
CPF1 = '111.111.111-11'
CPF = CPF1.split('.')
ult = CPF[-1].split('-')
CPF[-1]= ult[0] 

primeiro_caractere_entrada = CPF[0]
primeiro_caractere_entrada_repetido= primeiro_caractere_entrada * len(CPF)
print(CPF,primeiro_caractere_entrada_repetido)
num = range(10, 1, -1)
count = 0

sum = 0
for strings in CPF:
    for j  in strings:
        sum+=num[count]*int(j)
        count+=1   
sum = (sum*10)%11
f_dig = sum if sum < 9 else 0
 
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

'''CPF1 = '746.824.890-70'
CPF = CPF1.split('.')
ult = CPF[-1].split('-')
CPF[-1]= ult[0] 
'''

num = range(11, 2, -1)
count = 0

sum = 0
for strings in CPF:
    for j  in strings:
        sum+=num[count]*int(j)
        count+=1   
sum+=(2*f_dig)     
sum = (sum*10)%11
s_dig = sum if sum < 9 else 0

#validação cpf
cpf_gerado_calculo =''

for i in CPF:
    cpf_gerado_calculo+=i

cpf_gerado_calculo+=str(f_dig)
cpf_gerado_calculo+=str(s_dig)

cpf_usuario = ''
CPF.append(ult[1])
for j in CPF:
    cpf_usuario+=j 
if cpf_gerado_calculo == cpf_usuario:
    print(f'{cpf_usuario} cpf valido')
else:
    print('Por favor insira um cpf')    

