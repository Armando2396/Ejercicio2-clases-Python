#inicializamos la clase
class Alumno:
    # inicializamos los atributos
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    # funcion para imprimir los datos
    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)
    
    #funcion para obtener el resultado
    def resultado(self):
        if self.nota < 5:
            print("El alumno no aprobo")
        else:
            print("El alumno ha aprobado")
    
# bloque principal
# creamos los nuevos objetos
alumno1 = Alumno()
alumno2 = Alumno()

#inicializamos los atributos
alumno1.inicializar("Armando", 10)
alumno2.inicializar("Arian", 4)

#imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()