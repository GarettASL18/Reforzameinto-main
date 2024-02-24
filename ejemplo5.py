class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años. ")
persona1 = Persona("Juan", 30)
persona2 = Persona("Robert", 32)
persona2.saludar()
