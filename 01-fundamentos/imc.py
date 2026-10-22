peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso.")

elif 18.5 <= imc < 25:
    print(f"Seu IMC é {imc:.2f}. Você está com o peso normal.")

elif 25 <= imc < 30:
    print(f"Seu IMC é {imc:.2f}. Você está com sobrepeso.")

elif 30 <= imc < 35:
    print(f"Seu IMC é {imc:.2f}. Você está com obesidade grau I.")

elif 35 <= imc < 40:
    print(f"Seu IMC é {imc:.2f}. Você está com obesidade grau II.")

else:
    print(f"Seu IMC é {imc:.2f}. Você está com obesidade grau III.")
    