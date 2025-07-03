#Variáveis:um conjunto que contém algumas informações.

#Regras de criação:
#-Case-sensitive (ou seja, caracteres em caixa alta ou baixa são tratados como diferentes)
#-DEVE começar com uma letra ou um sublinhado; NÃO PODE começar com números.
#-NÃO PODE ser o mesmo nome que as palavras-chave Python (por exemplo, class, finally, etc.)
#-NÃO especificar o tipo de informação armazenada na variável. 

# TIPOS DE DADOS

#armazenando um int
idade = 12

#armazenando uma string (str)
helloMessage = "Hello World!"
first_name = "John"

#armazenando um caractere (str)
character_example = 'a'

#armazenando um float (float)
_newFloat = 1.0

#armazenando um valor booleano (bool)
bool_Condition = True

#A função utilizada pelo python pra vizualizar o resutado do que foi programado é a 'print'

#PARA VISUALIZAR RESULTADO NO TERMINAL CLIQUE ctrl + ' (aspas)

print(helloMessage)
print(first_name)
print(character_example)
print(_newFloat)
print(bool_Condition)
 
#FUNÇÃO "type"(mostra o tipo de dado que a variavél está guardando)

print(type(idade))
 # A partir da declaração acima idade é int , então esperamos que a função retorne int.

#CONVERSOR DE TIPO- 
# cód. para converter float em int
_newInt = int(_newFloat)

print(type(_newInt))

