# Lista de que haceres
QueHaceres = []

print("Lista de que haceres\n")

while True:
    try:
        hacer = int(input("1. Agregar algo a la lista\n2. Ver la lista\n3. Borrar algo de la lista\n4. Salir\n - "))
        if hacer == 1:
            agregar = input("Que Deseas Agregar: ")
            QueHaceres.append(agregar)
        elif hacer == 2:
            print(f"La Lista De Que Haceres Es: {QueHaceres}\n")
            
        elif hacer == 3:
            borrar = int(input(f"Que Desea borrar, Comienza Desde El 0 y Depende De La Cantidad De Cosas En La Lista: {QueHaceres}\n - "))
            QueHaceres.pop(borrar)
            print("Haz borrado un que hacer")
        elif hacer == 4:
            break
    except:
        print("Por Favor Introduce Un Valor De Int")