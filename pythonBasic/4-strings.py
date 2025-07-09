#Cada letra numa string é  guardada numa posição essa posição é chamada de INDEX. Por isso o termo INDEXAÇÂO para o tratamento de encontrar o caractere numa string.

mensagem = 'Oi! Meu nome é Hyuga' 
print(mensagem)
mensagem1 = " Uma mensagem com aspas duplas hehhe"
mensagem2 = """
Uau!
Uma mensagem com várias linhas.
Que legal! :D
"""


#Indexação (mostrando a informação da mensagem baseado na posição ao qual cada letra se encontra, começando do número 0.)
print(mensagem[0])

#Fatiamento
print(mensagem[0:4]) #Atráves do fatiamente você estipula o que de informação você quer pegar baseando no INDEX. Lmebrando que se começa pelo 0 e a última informação você declara a posição após ela.

#Outra situação é você escolher apenas o ponto de partida.
print(mensagem[0:]) #aqui irá mostrar a mensagem inteira pois parte do primeiro caractere.

print(mensagem[14:20])#aqui irá mostrar meu nome inteiro pois começa a partir da posição da primeira letra dele e finaliza uma posição após a última.

print(mensagem[0:-1]) #serve pra mostrar o último caractere de uma string, levando em consideração que você não saiba o tamanho da string e nem a posição do último caractere.

#Se a partir disso você raciocinar bem, da pra fazer coisas bem legais.
