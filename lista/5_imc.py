def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


# Programa principal
peso = 95
altura = 1.80

imc = calcular_imc(peso, altura)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")