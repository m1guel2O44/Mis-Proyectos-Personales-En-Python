inventario = [
    {"nombre": "Laptops", "actual": 5, "minimo": 10},
    {"nombre": "Monitores", "actual": 12, "minimo": 8},
    {"nombre": "Teclados", "actual": 3, "minimo": 15},
    {"nombre": "Mouse", "actual": 20, "minimo": 20},
    {"nombre": "Audífonos", "actual": 1, "minimo": 5}
]

def generar_alerta(lista_productos):
    for prod in lista_productos:
        if prod["actual"] < prod["minimo"]:
            print(f"- {prod['nombre']}: faltan {prod['minimo'] - prod['actual']} unidades.")

inventario_norte = [
    {"nombre": "Sillas Gamer", "actual": 2, "minimo": 5},
    {"nombre": "Escritorios", "actual": 10, "minimo": 4}
]
generar_alerta(inventario)
generar_alerta(inventario_norte)

