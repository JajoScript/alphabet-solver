# Desarrollo de un concatenador de alfabetos.
# Autor: Javier Almarza.

class MasterManager():
    # Propiedades.
    # Constructor.

    # Metodos.
    def compiladorLaTeX(self):
        pass
    
    def manejadorArchivos(self, operador):
        # Lecturas de archivos.
        if(operador == 1):
            try:        
                with open("input", "rt") as Archivo:
                    print(f"[CONTENT] {Archivo.read()}")
            except FileNotFoundError:
                print(f"[ERROR] El archivo input no fue creado.")    
        # Escritura de archivos.
        elif(operador == 2):
            pass

        else:
            print(f"[ERROR] Ocurrio un error al administrar los archivos.")

    def menu(self):
        # 1. Iteracion de Lenguajes.
        # 2. Determinación de la pertenencia de un Lenguaje.
        # 3. Concatenación de dos cadenas.
        pass

    def administradorCadenas(self):
        
        pass

    # Getters & Setters.
    
    @property   #Metodo Getter
    def obtener(self):
        pass
    @obtener.setter
    def modificar(self):    #Metodo Setter
        pass
    
    
    pass


def main():
    # Instancias de la clase.
    MM = MasterManager()
    MM.manejadorArchivos(1)
    
    
if __name__ == '__main__':
    main()
