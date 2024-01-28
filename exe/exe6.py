"""
Iterando strings com while
"""
nome = "Gustavo pereira"
contador = len(nome)
test = len(nome) > 0
nova_string = ' ' 
while(contador):
    nova_string += f'*{nome[len(nome) - contador]}'
    contador-=1

    print(nova_string)
