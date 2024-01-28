lista = [ 'Maria', 'Luiz', 'Pedro']
lista.append('João')
indices = range(len(lista))
print(indices)

for indice in indices:
    print(indice,lista[indice],type(lista[indice]))