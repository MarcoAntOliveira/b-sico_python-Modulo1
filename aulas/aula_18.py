for i in range(10):
    if i == 2:
        print('i é igual a 2 pulando ...')
        continue
    if i == 8:
        print('i é iual a 8 , seu else não executara')
    for j in range(1, 4):
        print(i, j)
else:
    print('For completo com sucessso')                