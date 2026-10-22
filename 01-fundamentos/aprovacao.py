nota = float(input("Digite sua nota: "))
frequencia = float(input("Digite sua frequência (em %): "))

if nota >= 7 and frequencia >= 75:
    print("Aprovado!")

elif nota >= 5 and frequencia >= 75:
    print("Recuperação.")

else:
    print("Reprovado.")
