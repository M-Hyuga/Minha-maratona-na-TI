#DECLARaçÕES CONDICIONAIS

velocidade = 30

if velocidade > 110: 
    print('A cima da Velocidade Permitida')
    print(' Favor reduzir a sua velocidade')
#SE o valor da variável estiver "True" nas condições do IF, será esse resultado impresso como resposta.

elif velocidade < 80:
    print('Favor dirigir acima de 80km/h')
#SE_CASO o valor da variável estiver "True" nas condições do ELIF, será esse resultado impresso como resposta.(o ELIF você pode ter quantos quiser.)
else:
    print('Velocidade OK')
#SENÃO as condições do ELSE que aparecerão no resultado.
#(Basicamente é como se dissesse: "se a velocidade não está a cima de 110 então faça isso")

#IMPORTANTE: Respeitar a organização da indentação de acordo mostrado nos exemplos.
