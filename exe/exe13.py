import os
lista_compras = [] 
while True:
    option = input("[i]nserir [a]pagar [l]istar: \t")
    if option == 'i':
        os.system('clear')
        compra = 's' 
        while compra == 's':
            valor = input('valor:')  
            lista_compras.append(valor)
            compra = (input('inserir? [s]im ou [n]ão')).lower()

    elif option == 'l':
        os.system('clear')
        if(len(lista_compras)==0):
            print("lista vazia")
        for indice , iten in enumerate(lista_compras):
            print(indice , iten) 
            continue   

    elif option == 'a':
        os.system('clear')
        print("digite a posição o item que você quer apagar")
        pos = int(input('posição: '))
        try:
            item = lista_compras[pos]
            del lista_compras[pos]
            print(f'o item {item} foi deletado da lista, na posição {pos}')
        except IndexError:
            print('Ocorreu um problema ao tentar remover esse valor da lista')    
        except ValueError:
            print("Por favor digite um inteiro")    
        except Exception:
            print("Erro desconhecido")           
    else:
        print('Opção inválida')    