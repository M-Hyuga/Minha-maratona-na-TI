#OPERAÇÕES-Operadores Aritméticos
#ORDEM DOS OPERADORES 
#1-Parênteses() 2-Exponenciação** 3-Multiplicação* 4-Divisão/ 5-Div.Inteira// 6-Módulo% 7-Adição+ 8-Subtração-
#Operações matemáticas básicas com Números

#Adição 
print(4+5)

#Subtração
print(23-12)

#Multiplicação
print(4*3)

#Potência/Expoente 
#o operador ** é equivalente ao expoente
print(5**2) 
#5*5 = 5^2 = 5**2

#Divisão(float)
#Retornar o valor decimal real da divisão
print(36/4)
print(10/3)

#Divisão(int)
#Retornar um int> Se o quociente real for um valor decimal, apenas um número inteiro irá retornar
print(10/3)
print(19/6)

#Divisão Modular: retornar o restante da divisão
print(10%3)

#OPERAÇÃO COM STRINGS E CARACTERES
print("foo"*5)
print('x'*3)

#---ATENÇÃO---
#NÃO PODE CONCATENAR UM int COM UMA string ---> necessidade de computar int com uma string
#-ERRO print("hello" + 5)
#-CORRETO
print("hello" + str(5)) #Dessa se converte o dado int em string.

#Adição de String = concatenação
print("hello" + "world")


#OUTROS OPERADORES

#OPERADOR DE ATRIBUIÇÃO 
#funciona em adição, subtração, multiplicação, divisão, etc.
pro1 = 10

pro1 += 3 #todo valor atribuido a pro1 será acrescentado +3

pro1**= 3 #todo valor atribuido a pro1 será elevado ao cubo

#COMPARADORES- retornar valor booleano

#igualdade == -deve ser sinais de igual duplos, um sinal de igual único é atribuição
print(5==5.0)

#maior que > 
print(7 > 1)

#menor que < 
print(1.4 < 10)

#maior ou igual >=
print( 12.0 >= 12)
print(12.0 >= 11)
print(12 >= 13)

#menor ou igual <= 
print(10 <= 10.0)
print(10 <= 20)
print(8 <= 3)

#COMPARADORES EM STRINGS 

print("Hello" < "world")
print("hello" == "world")
print("hello" > "world")

print("hello" == "hello")

print("cat" < "dog")
