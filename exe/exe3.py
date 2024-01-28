primeiro_valor = input('Digite um valor: ')
segundo_valor =  input('Digte outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} , é maior que ao ' 
        f'{segundo_valor=}'
        )

elif primeiro_valor < segundo_valor:
    print(
        f'{segundo_valor=} , é maior que ao' 
        f' {primeiro_valor=}'
        )
else :    
    print(
        f'{primeiro_valor=} é igual ao' 
        f'{segundo_valor}'
        )