from juego_encapsulado import Juego
import readchar, os, random
from readchar import readkey,key

mapas = os.listdir(r'mapas')
seleccion = random.choice(mapas)
lectura = r'mapas\\'+seleccion

mapa = Juego.leer_archivo(lectura)
posicion_inicial = (int(mapa[0]), int(mapa[1]))
posicion_final = (int(mapa[3]), int(mapa[2]))
laberinto = mapa[4:len(mapa)+1]
laberinto = "\n".join(["".join(fila) for fila in laberinto])


jugar = Juego(laberinto, posicion_inicial, posicion_final)

def main_loop(juego):
    print("Ingresa tu Nombre: ")
    nombre = input()
    print(f"Hola {nombre} Bienvenido al juego")
    px = juego.posicion_inicial[0]
    py = juego.posicion_inicial[1]
    mat = juego.conv_matriz(juego.laberinto)
    mat[px][py] = '☻'
    juego.laberinto = juego.matriz_a_cadena(mat)
    print(juego.laberinto)
    while True:
        if px == juego.posicion_final[0] and py == juego.posicion_final[1]:
            print(f"Felicidades {nombre}, lo lograste!!!!")
            break          
        else:
            print("Para jugar usa las teclas , arriba'↑' , Abajo'↓', Derecha '→' , Izquierda '←")
            teclas = readkey()
            if teclas == key.UP :
                if px-1 >= 0 and mat[px-1][py] != '#':
                    mat[px][py] = ' '
                    px -= 1
            elif teclas == key.LEFT :
                if py-1 >= 0 and mat[px][py-1] != '#':
                    mat[px][py] = ' '
                    py -= 1
            elif teclas == key.DOWN:
                if px+1 <= 20 and mat[px+1][py] != '#':
                    mat[px][py] = ' '
                    px += 1
            elif teclas == key.RIGHT:
                if py+1 <= 20 and mat[px][py+1] != '#':
                    mat[px][py] = ' '
                    py += 1
            else:
                print("Ingrese una tecla válida")
            mat[px][py] = '☻'
            juego.limpiar_pantalla(mat)

main_loop(jugar)