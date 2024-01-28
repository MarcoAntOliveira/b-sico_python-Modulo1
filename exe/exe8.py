frase = 'O python é uma linguagem de programação '\
'multiparadigma'\
'Python foi criado por Guido van Rossum'
contador1 = 0 #contador de iterações
contador2 = 0 # contador de iterações 2
contador3 = 0 # contador de letras 1
contador4 = 0 #contador de letras 2
tam = len(frase)
letra_mais_apareceu = ' '
letra = ' '
while contador1 < tam:
    letra = frase[contador1].lower()
    while contador2 < tam:
        if letra == frase[contador2].lower():
            contador3+=1
            contador2+=1
        else:
            contador2+=1
            continue       
    contador2 = 0      
    if (contador3 > contador4) and (letra != ' '):
        letra_mais_apareceu = letra
        contador4 = contador3
    contador1+=1    
       
print(f'A letra com mais ocorrência é {letra_mais_apareceu} e apareceu {contador4} vezes') 