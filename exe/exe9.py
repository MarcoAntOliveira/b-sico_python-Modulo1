frase ='O python é uma linguagem de programação '\
'multiparadigma'\
'Python foi criado por Guido van Rossum'
tam = len(frase)
i = 0
contador1 = 0
contador2 = 0
letra_mais_apareceu = ' '
while i < tam:
    letra = frase[i].lower()
    contador1 = frase.count(letra)
    if letra == ' ':
        i+=1
        continue
         
    if (contador1 > contador2) :
        contador2 = contador1 
        letra_mais_apareceu =  letra
    i+=1
print(f'A letra que mais apareceu foi {letra_mais_apareceu} e foram {contador2} vezes')
