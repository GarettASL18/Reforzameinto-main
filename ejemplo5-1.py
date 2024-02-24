#Haciendo que el usuario digite su edad y nombre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años. ")
    def despedir(self):
        print(f"Adios, que te vaya bien {self.nombre}")
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"        
#Pedir al usuario que ingrese el nombre y su edad:
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
#Crear su instancia persona1 = Persona
persona1= Persona(nombre, edad)
#Imprimir los atributos de la instancia persoonal y saludar()
#print("Nombre: ", persona1.nombre)
#print("Edad: ", persona1.edad)
print(persona1)