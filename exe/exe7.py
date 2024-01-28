""" calculadora com while"""
while(True):
   num1 = input('Digite um numero: ')
   num2 = input('Digite outro numero: ')
   operador =  input('Digite um operador: ')
   numeros_validos =  None

   try:
      num1_float= float(num1)
      num2_float=float(num2)
      numeros_validos = True
   except:
      numeros_validos = None

   if numeros_validos is None:
      print('Um ou ambos os numeros não são float')
      continue
   
   operadores_permitidos= '+-/*'
   if operador  not in operadores_permitidos:
      print('Operador inválido')
      continue
   if len(operador) > 1: 
      print('Digite apenas um operador: ')  
      continue
   print('Realizando sua conta. confira abaixo sua resposta') 
   if operador == '+':
      print(f'{num1_float}+ {num2_float}=',num1_float+ num2_float)
   elif operador =='-':
       print(f'{num1_float} - {num2_float}=',num1_float - num2_float)
   elif operador =='/':
       print(f'{num1_float}/{num2_float}=',num1_float / num2_float)
   elif operador =='*':   
       print(f'{num1_float}*{num2_float}=',num1_float * num2_float)
   else:
      print('Você nunca deveria chegar aqui')   
   
         
   sair = input('Quer sair [s]im: ').lower().startswith('s')
   if sair:
      break 


