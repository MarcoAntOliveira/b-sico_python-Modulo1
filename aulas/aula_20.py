salas = [
    ['Maria', 'Helena'],
    ['Elena'],
    ["Luiz", 'João', 'Eduarda', (0, 10 , 10, 20 , 30)],
  
 ]

#print(salas[2][3][3])
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)