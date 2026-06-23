import time

class jugador:
    def __init__(self):
        self.vida = 100
        self.daño = 10
        self.armadura = 10
class restarvida:
    def __init__(self, vida, daño):
        self.vida = vida
        self.daño = daño
    def restar(self):
        self.vida -= self.daño
class enemigo:
    def __init__(self):
        self.vida = 10
        self.daño = 25
        self.armadura = 10

print("Bienvenido a la dungeon del campeon.")
el_jugador = jugador()
while True:
    try:
        entrar = int(input("¿Vas a entrar?\n1. Si\n2. No\n- "))
        if entrar == 1:
            atacarOpasar = int(input("Haz encontrado un enemigo, lo vas a atacar o pasar de el\n1. Atacar\n2. Pasar\n- "))
            if atacarOpasar == 1:
                un_enemigo = enemigo()
                un_enemigo.vida -= el_jugador.daño
                el_jugador.vida -= un_enemigo.daño
                print(f"La vida del enemigo es: {un_enemigo.vida}")
                print(f"El enemigo te ataco, tu vida actual es: {el_jugador.vida}")
                if un_enemigo.vida <= 0:
                    print("Haz matado al enemigo.\n")
                    if el_jugador.vida <= 0:
                        print("Haz Muerto, Fin del juego.")
                        time.sleep(5)
                        break
            if atacarOpasar == 2:
                print("El enemigo te ha atacado por la espalda y haz muerto. FIN DEL JUEGO\n")
                break
        elif entrar == 2:
            print("Haz decido no entrar.\n")
            break
        else:
            print("Eso no es una opcion elegible.\n")
    except:
        print("Error\n")