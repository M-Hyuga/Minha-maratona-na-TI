#facilita a organização ficando mais legivel e melhor de executar o código.

#Vamos aos exemplo

nome = "Mônica"
sobrenome = "Nascimento"
profissao = "Programadora"

#Forma por concatenação básica
textoSemFormated = "A " + nome + " " + sobrenome + " é uma exelente [" + profissao + "]."
print(textoSemFormated)

#Usando o formated 
textoComFormated = f'A {nome} {sobrenome} é uma exelente [{profissao}].'
print(textoComFormated)

