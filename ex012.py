preco = float(input("Digite o preço do produto para saber o seu valor após o desconto R$"))
porcento = float(input("Digite a porcentagem do desconto "))
desconto = preco*porcento/100
valorfinal = preco - desconto
print("Você pagará R${}".format(valorfinal))
input("Precisone qualquer tecla para sair ")