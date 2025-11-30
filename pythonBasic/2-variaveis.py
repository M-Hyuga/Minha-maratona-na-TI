
#Variáveis = um espaço no código para armazenar dados.(pense como se fosse uma gaveta que armazena apenas 1 tipo de coisa. )


"""Regras de criação:
-Case-sensitive (ou seja, caracteres em caixa alta ou baixa são tratados como diferentes)
-DEVE começar com uma letra ou um sublinhado; NÃO PODE começar com números.
-NÃO PODE ser o mesmo nome que as palavras-chave Python (por exemplo, class, finally, etc.)
-Especificar o tipo de informação armazenada na variável.""" 

# TIPOS DE DADOS

#int = numeros inteiros
idade = 12

#string (str) =  caractere (não apenas textos, tudo que tiver antre aspas...)
helloMessage = "Hello World!"
first_name = "John"

#float (float) =  números fracionados (números em fração..números quebrados...)
_newFloat = 1.0

# booleano (bool) = valores binários; 1 = true\ 0 = false (usados geralmente quanto existe condições que precisam de verificação.)
bool_Condition = True

#print =  FUNÇÃO, utilizada para mostrar resultado do código no terminal.
print(helloMessage)
print(first_name)
print(_newFloat)
print(bool_Condition)
 
#type = FUNÇÃO, mostra o tipo de dado que a variavél está guardando.

print(type(idade))
 # A partir da declaração acima idade é int , então esperamos que a função retorne int.

#CONVERSOR DE TIPO- 
# cód. para converter float em int
_newInt = int(_newFloat)

print(type(_newInt))
