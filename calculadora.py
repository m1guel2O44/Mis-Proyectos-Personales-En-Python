#Calculara de Miguel
print("Bienvenido a la calculadora de Miguel, ¿Deseas calcular algo?\n")

while True:
    try:
        calcular = int(input("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\n - "))
        if calcular == 1:
            print("¿Que Numeros Quieres Sumar?\n")
            suma1 = int(input("Primer Numero a sumar: "))
            suma2 = int(input("Segundo Numero a sumar: "))
            resultadoSuma = suma1 + suma2
            print(f"El resultado de la suma es: {resultadoSuma}")
        elif calcular == 2:
            print("¿Que Numeros Quieres Restar?\n")
            resta1 = int(input("Primer Numero a Restar: "))
            resta2 = int(input("Segundo Numero a Restar: "))
            resultadoResta = resta1 - resta2
            print(f"El Resultado de la resta es: {resultadoResta}")
        elif calcular == 3:
            print("¿Que Numero Desea Multiplicar?\n")
            Multi1 = int(input("Primer Numero a Multiplicar: "))
            Multi2 = int(input("Segundo Numero a Multiplicar: "))
            resultadoMulti = Multi1 * Multi2
            print(f"El Resultado De La Multiplicacion Es: {resultadoMulti}")
        elif calcular == 4:
            print("¿Que Numeros Quieres Dividir")
            division1 = int(input("Primer numero a dividir: "))
            division2 = int(input("Segundo numero a dividir: "))
            resultadoDivision = division1 / division2
            print(f"El resultado de la division es: {resultadoDivision}")
        elif calcular == 5:
            break
        else:
            print("Error, ese numero no esta en la lista\n")
    except ValueError:
        print("Ingresa un digito, no una cadena de texto, ni mucho menos un simbolo especial.\n")
    except ZeroDivisionError:
        print("No se puede dividir por 0")



