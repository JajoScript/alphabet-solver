# Desarrollo de un concatenador de alfabetos.

# Dependencias.
import os
import time

# Definición de clase.
class MasterManager():
    # Constructor.
    def __init__(self):
        pass

    # Metodos.
    def __compiladorLaTeX(self):
        pass

    def __controladorErrores(self, error):
        self.__limpiarpantalla()
        print(f"[ERROR] {error}")    
        self.__tiempoEspera(3)

    def __manejadorArchivos(self, operacion, nombreArchivo, configuracion, contenido):
        # Lecturas de archivos.
        if(operacion == "lectura"):
            try:        
                with open(nombreArchivo, "rt") as Archivo:
                    if configuracion == "iteracion":
                        print(f"[DEV] {Archivo.read()}")

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
        else:
            self.__controladorErrores("No se ingreso una opción valida.")

    # Getters & Setters.
    @property   
    # Metodos Getters
    def obtener(self):
        pass

    @obtener.setter
    # Metodos Setter.
    def modificar(self):    
        pass

# Ejecución
def main():
    # Instancias de la clase.
    MM = MasterManager()
    
    while True:
        MM.menu()
            
if __name__ == '__main__':
    main()