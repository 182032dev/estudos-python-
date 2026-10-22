nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ingresso = input("Você possui ingresso (SIM/NÃO): ").lower()
bloqueado = input("Você está bloqueado (SIM/NÃO): ").lower()

if idade >= 18 and ingresso == "sim" and bloqueado == "não":
    print(f"Bem-vindo(a), {nome}! Você pode acessar o evento.")

elif idade < 18:
    print(f"Desculpe, {nome}. Você não pode acessar o evento, pois é menor de idade.")

elif ingresso == "não":
    print(f"Desculpe, {nome}. Você não pode acessar o evento, pois não possui ingresso.")
