# Tiendita de Miguel
objetos = ["Arroz", "Carne De Res", "Pollo", "Habichuelas", "Cilantro", "Lechuga", "Toallitas Humedas"]
print("Bienvenido a la tienda de Miguel\n")

print("¿Desea comprar algun objeto?\n Si\n No")

while True:

        respuesta = (input)("- ")
        if respuesta == "Si":
            print(f"Inventario: {', ' .join(objetos)}")
        if respuesta == "No":
                break
        while True:
            compra = input("- ").title()
            final = input(f"Haz comprado: {compra}, ¿Desea salir de la aplicacion?, ¿Si o No? - ")
            if final == "Si":
                break
            elif final == "No":
                print("Compra Puesta\n")




