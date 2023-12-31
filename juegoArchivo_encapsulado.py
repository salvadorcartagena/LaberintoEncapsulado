import os

class Juego:
    def __init__(self, laberinto, posicion_inicial, posicion_final):
        self.laberinto = laberinto
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
    
    def conv_matriz(self, cadena):
        matriz = cadena.split("\n")
        for i in range(len(matriz)):
            matriz[i] = list(matriz[i])
        return matriz
    
    def limpiar_pantalla(self, mat):
        os.system('cls' if os.name=='nt' else 'clear')
        self.laberinto = self.matriz_a_cadena(mat)
        print(self.laberinto) 

    def matriz_a_cadena(self, matriz):
        cadena_laberinto = "\n".join(["".join(fila) for fila in matriz])
        return cadena_laberinto    
    
    def leer_archivo(ruta):
        with open(ruta, "r") as archivo:
            contenido = archivo.read()
        contenido = contenido.strip()
        contenido = contenido.split()
        return contenido
    
class JuegoArchivo(Juego):
    def __init__(self, laberinto, posicion_inicial, posicion_final, archivo):
        super().__init__(laberinto, posicion_inicial, posicion_final)
        self.archivo = archivo
        