print("=== CALCULADORA ===")

a = float(input("Número 1: "))
b = float(input("Número 2: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)

if b != 0:
    print("División:", a / b)
    print("Módulo (residuo):", a % b)
else:
    print("No se puede dividir entre 0")

print("Potencia (a^b):", a ** b)
print("División entera:", a // b)