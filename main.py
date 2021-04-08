# Desarrollo de un concatenador de alfabetos.
class MasterManager():
    # Propiedades.

    # Constructor.
    def __init__(self):
        pass

    # Metodos.
    def _compiladorLaTeX(self):
        pass
    
    def _manejadorArchivos(self, operador):
        # Lecturas de archivos.
        if(operador == 1):
            try:        
                with open("input", "rt") as Archivo:
                    print(f"[DEV][CONTENT] {Archivo.read()}")
            except FileNotFoundError:
                print(f"[ERROR] El archivo input no fue creado.")    

        # Escritura de archivos.
        elif(operador == 2):
            with open("output", "wt") as Archivo:
                pass
            
        else:
            print(f"[ERROR] Ocurrio un error al administrar los archivos.")

    def __iteracionLenguaje(self):
        pass

    def determinacionLenguaje(self):
        pass

    def concatenarCadenas(self):
        pass

    def menu(self):
        print("[Alphabet-solver]\n")
        print("[1] Iteración de un lenguaje.")
        print("[2] Determinar si una cadena pertenece a un lenguaje.")
        print("[3] Concatenación de dos cadenas.")
        print("[4] Salir.")

        opcion = input("[>] Escriba el numero de problema que desea resolver: ")

        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            exit()
        else:
            print("[ERROR] No se ingreso una opción valida.")

    def __administradorCadenas(self):
        pass

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
