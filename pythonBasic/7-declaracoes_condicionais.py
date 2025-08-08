#ESTRUTURA CONDICIONAL if 

#REGRAS:
"""A ordem das condições importa!
        Se mais de uma condição estiver satisfeita, então as ações
        associadas à primeira condição satisfeita serão executadas
        e saltarão as demais condições e códigos.
"""

""" "elif" = "else if"
     "elif" expressa o mesmo significado que "else if"

     Pelo menos uma condição DEVE ser prevista para ambas as cláusulas if e elif, senão ERROR!

     Os parênteses para if e elif são opcionais. Seu código funcionará com ou sem o ()."""

x = 7
y = 14

if ( 2 * x == y) :
    print("y é o dobro de x")

elif(x**2 == y):
    print("y é o quadrado de x")

else:
    print("y não é o dobro de x")

x2 = 7
y2 = 49

if (x2*2 == y2):
    print("y2 é o dobro de x2")

elif (x2**2 == y2):
    print("y2 é o quadrado de x2")

else:
    print("y2 NÃO está relacionado a x2")


x3 = 7
y3 = 50

if (2*x3 == y3):
    print("y3 é o dobro de x3")

elif (x3**2 == y3):
    print("y3 é o quadrado de x3")
    
else:
    print("y3 NÃO está relacionado a x3")
