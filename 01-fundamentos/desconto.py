produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))

if preco <= 100: 
    preco_final = preco
    print("Sem desconto.")
    print(f"Preço final: R$ {preco_final:.2f}")
elif preco <= 500:
    desconto = preco * 0.10
    preco_final = preco - desconto 
    print("Produto com desconto de 10%.")
    print(f"Preço final: R$ {preco_final:.2f}")
else:
    desconto = preco * 0.15
    preco_final = preco - desconto
    print("Produto com desconto de 15%.")
    print(f"Preço final: R$ {preco_final:.2f}")
    


