# Desarrollo de un concatenador de alfabetos.

# Dependencias.
import os
import time

# Definición de clase.
class MasterManager():
    # Propiedades.
    modoDepurador = False

    # Constructor.
    def __init__(self, modo):
        self.__modoDepurador = modo
        self.__normal = '\033[92m'
        self.__error = '\033[91m'
        self.__dev = '\033[93m'
        self.__end = '\033[0m'
        self.__lineasArchivo = 5

    # Metodos.
    def __registro(self, id,contenido):
        tiempo = time.localtime(time.time())

        if id == "DEV" and self.modoDepurador == True:
            print(self.__dev + f"[{tiempo.tm_hour}:{tiempo.tm_min}:{tiempo.tm_sec}][{id}] {contenido}" + self.__end)
            self.__tiempoEspera(1)

        elif id == "ERROR":
            print(self.__error + f"[{tiempo.tm_hour}:{tiempo.tm_min}:{tiempo.tm_sec}][{id}] {contenido}" + self.__end)
            self.__tiempoEspera(2)

        else:
            print(self.__normal + f"[{tiempo.tm_hour}:{tiempo.tm_min}:{tiempo.tm_sec}][{id}] {contenido}" + self.__end)

    def __compiladorLaTeX(self):
        pass

    def __controladorErrores(self, error):
        self.__limpiarpantalla()
        self.__registro("ERROR", error)

    def __manejadorArchivos(self, operacion, nombreArchivo, configuracion, contenido):
        # Lecturas de archivos.
        if(operacion == "lectura"):
            try:        
                with open(nombreArchivo, "rt") as Archivo:
                    if configuracion == "iteracion":
                        
                        linea = 1
                        while(linea <= self.__lineasArchivo): 
                            contenido = Archivo.readline()
                            if (contenido[0] != "#") and (contenido[0] != " ") and (contenido[0] != '\n'):
                                # Determinando el lenguaje.
                                if contenido[0] == "L":
                                    self.__registro("DEV", "Pille el lenguaje")
                                    array = contenido[3:-2].split(",")
                                    self.__registro("DEV", array)

                                # Determinando la iteración.
                                else:
                                    self.__registro("DEV", "Pille la iteracion")
                                    
                                    iteracion = int(contenido)
                                    self.__registro("DEV", iteracion)
                                

                            linea += 1

                    elif configuracion == "determinacion":
                        print(f"[DEV] {Archivo.read()}")

                    elif configuracion == "concatenacion":
                        print(f"[DEV] {Archivo.read()}")

            except FileNotFoundError:
                self.__controladorErrores("No se encontro el archivo especificado.")

        # Escritura de archivos.
        elif(operacion == "escritura"):
            with open("output", "wt") as Archivo:
                pass
            
        else:
            self.__controladorErrores("Ocurrio un error al administrar los archivos.")

    def __tiempoEspera(self, segundos):
        time.sleep(segundos)

    def __limpiarpantalla(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def __iteracionLenguaje(self):
        self.__limpiarpantalla()
        print("[Alphabet-solver/IteracionLenguaje]")

        # Apertura de archivo.
        nombreArchivo = input("[>] Ingresa el nombre del archivo (input): ")
        self.__manejadorArchivos("lectura", nombreArchivo, "iteracion", "")


    def __determinacionLenguaje(self):
        self.__limpiarpantalla()

        # Apertura de archivo.
        nombreArchivo = input("[>] Ingresa el nombre del archivo (input): ")
        self.__manejadorArchivos("lectura", nombreArchivo, "determinacion", "")


    def __concatenarCadenas(self):
        self.__limpiarpantalla()

        # Apertura de archivo.
        nombreArchivo = input("[>] Ingresa el nombre del archivo (input): ")
        self.__manejadorArchivos("lectura", nombreArchivo, "concatenar", "")


    def menu(self):
        self.__limpiarpantalla()
        print("[Alphabet-solver]\n")
        print("[1] Iteración de un lenguaje.")
        print("[2] Determinar si una cadena pertenece a un lenguaje.")
        print("[3] Concatenación de dos cadenas.")
        print("[4] Salir.")

        opcion = input("[>] Escriba el numero de problema que desea resolver: ")

        if opcion == '1':
            self.__iteracionLenguaje()

        elif opcion == '2':
            self.__determinacionLenguaje()

        elif opcion == '3':
            self.__concatenarCadenas()

        elif opcion == '4':
            self.__limpiarpantalla()
            exit()
        elif opcion == "jose":
            self.modoDepurador = True
            self.__registro("", "Modo depurador esta activado!")
            self.__tiempoEspera(2)

        else:
            self.__controladorErrores("No se ingreso una opción valida.")

    # @GODFataliti, con amor para ti.
    # Getters & Setters.
    # @property   
    # # Metodos Getters
    # def obtenerModoDepurador(self):
    #     return self.__modoDepurador

    # @obtenerModoDepurador.setter
    # # Metodos Setter.
    # def modificarModoDepurador(self, modo):
    #     self.__modoDepurador = modo


# Ejecución
def main():
    # Instancias de la clase.
    MM = MasterManager(False)
    
    while True:
        MM.menu()
            
if __name__ == '__main__':
    main()