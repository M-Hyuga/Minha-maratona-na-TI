
rendaAcima5Mil = int(input("Qual sua renda?"))
nome_limpo = input("Seu nome está limpo?")


if (rendaAcima5Mil > 5000) and (nome_limpo == "sim"):
    print("Financiamento aprovado!")

else:
    print("Financimento negado")