print("===== CALCULADORA EN PYTHON =====")

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
operacion = input("Elige una operación (+, -, *, /): ")


if operacion == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif operacion == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)
