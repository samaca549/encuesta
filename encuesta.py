class Estudiante:
    def __init__(self, nombre, proyecto, trabajo_en_grupo, edad, temas_preferidos):
        self.nombre = nombre
        self.proyecto = proyecto
        self.trabajo_en_grupo = trabajo_en_grupo
        self.edad = edad
        self.temas_preferidos = temas_preferidos

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Proyecto: {self.proyecto}")
        print(f"¿Sabe trabajar en grupo?: {self.trabajo_en_grupo}")
        print(f"Edad: {self.edad}")
        print(f"Temas preferidos: {self.temas_preferidos}")

class Encuesta:
    def __init__(self):
        self.respuestas = []

    def pedir_datos(self):
        print("////////////////////////////")
        print("USUARIO")
        nombre = input("Digite su nombre: ")
        proyecto = input("Digite su proyecto: ")
        trabajo_en_grupo = input("¿Sabe trabajar en grupo? (Sí/No): ")
        edad = int(input("Digite su edad: "))
        temas_preferidos = input("¿Qué temas prefiere para el proyecto?: ")

        return Estudiante(nombre, proyecto, trabajo_en_grupo, edad, temas_preferidos)

    def agregar_respuesta(self, estudiante):
        self.respuestas.append(estudiante)

    def mostrar_respuestas(self):
        print("\n--- Respuestas de los encuestados ---")
        contador = 1
        for estudiante in self.respuestas:
            print(f"\nEncuestado #{contador}")
            estudiante.mostrar_info()
            contador += 1
def main():
    encuesta = Encuesta()

    for i in range(10):
        print(f"\n--- Ingresando datos del estudiante {i+1} de 10 ---")
        estudiante = encuesta.pedir_datos()
        encuesta.agregar_respuesta(estudiante)

    encuesta.mostrar_respuestas()

if __name__ == "__main__":
    main()


