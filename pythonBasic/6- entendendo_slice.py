#Sendo uma string uma éspecie de "lista" que guarda dados atrávez do slice cortamos os dados com objetivo de usar apenas o que é necessário naquele momento.z

fruta = "Acerola"
        #0123456
# conta-se os itens de uma lista a partir do 0

print(fruta[0:3])

email = "monicansilva00@gmail.com" 
         
#na lógica todo em todo gmail.com o @ fica "-10" (contando atráves dos números negativos). Então uma forma de válidar um email é procurando esse item. Usando o Slice pode ser possivel.

print(email[-10])

#e também a partir do @ (-10) até o m (da palavra "com") pra isso basta colocar a posição acompanhada apenas dos dois pontos :

print(email[-10:])

print(email[:-10]) #também é possivel fazer o contrário caso seja necessário pegar apenas os dados da pessoa. 
# só não esqueça de colocar sempre o valor do item que sucede o que vocÊ quer que apareça.