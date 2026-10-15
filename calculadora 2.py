elif operacion == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Error: no se puede dividir entre cero")

else:
    print("Operación no válida")