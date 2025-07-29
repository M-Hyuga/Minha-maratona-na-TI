import datetime
#Nesse cód importei a função datetime para manter a variálvel ano_atual com o ano atualizado.
ano_atual = datetime.date.today().year
ano_nasc = int(input("Qual ano você nasceu? ")) #aqui mudei o tipo do dado pra quando  for executar o calculo não dar erro, pois ambos agora são int.

idade = ano_atual - ano_nasc
idade = str(idade) #aqui mudei o tipo do dado pra quando for concatenar não dar erro.

print ( "Você tem ou fará " + idade +  " anos." )