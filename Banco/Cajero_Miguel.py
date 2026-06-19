print("Bienvenido al Banco Digital de Miguel\n".title())
saldo = 1000

while True:
    Banco = int(input("¿Que desea hacer?\n 1. Ver Saldo\n 2. Retirar Saldo\n 3. Depositar Saldo\n 4. Salir\n - "))
    if Banco == 1:
        print(f"Su saldo actual es: {saldo}")
    elif Banco == 2:
        Retirar = int(input("Ingrese el monto que desea retirar: "))
        if Retirar <= saldo:
            print(f"Haz retirado: {Retirar}")
            saldo -= Retirar
        else:
            print("El monto a retirar es mayor al de la cuenta\n".title())
    elif Banco == 3:
        Depositar = int(input("Ingrese el monto que desea depositar: "))
        if Depositar > 0:
            saldo += Depositar
            print(f"Haz depositado: {Depositar}\n")
        else:
            print("El monto a depositar debe ser mayor que cero\n".title())
    elif Banco == 4:
        print("Gracias por utilizar el Banco Digital de Miguel".title())
        break
    else:
        print("Opción no válida. Ingrese una opción válida".title())
