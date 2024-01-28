"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta= input("insira a palavra secreta: ")
palavra_usuario = 0
letras_acertadas = ''
print('|\n'*10)
tentativas =  0
while palavra_usuario < len(palavra_secreta):
    print(f'Voce tem {tentativas} tentativas')
    letra_digitada = input ("insira uma letra: ")

    if(len(letra_digitada) > 1):
        print('você digitou mais de uma letra')
        continue

    palavra_usuario1 =''
    if letra_digitada in palavra_usuario1:
        print('Essa letra já foi digitada')
        tentativas+=1
        palavra_usuario+=1
        continue


    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        tentativas+=1  
        palavra_usuario+=1 
         
    else:
        tentativas+=1     
        palavra_usuario+=1  

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_usuario1+=letra_secreta
                        
        else:
            #print(palavra_usuario1)
            palavra_usuario1+='*'    

    if (palavra_usuario1 == palavra_secreta): 
        os.system('clear')
        print(tentativas)
        print('Você ganhou')
        letras_acertadas = ''
        tentativas = 0
         
    print(palavra_usuario1) 

print(f'A quantidade de tentativas do usuario foi {len(palavra_secreta)} vezes'
f'  e o usuario formou a palavra{palavra_usuario1}')