class Estudiantes:
    def __init__(self):
        self.respuestas = []

    def pedir_datos(self):
        print("////////////////////////////")
        print("USUARIO")
        nombre = input("Digite su nombre: ")
        proyecto = input("Digite su proyecto: ")
        trabajo = input("¿Sabe trabajar en grupo? (Sí/No): ")
        edad = int(input("Digite su edad: "))
        temas = input("¿Qué temas prefiere para el proyecto?: ")

        return {
            "nombre": nombre,
            "proyecto": proyecto,
            "trabajo": trabajo,
            "edad": edad,
            "temas": temas
        }

    def agregar_respuesta(self, respuesta):
        self.respuestas.append(respuesta)

    def mostrar_respuestas(self):

        print("\n--- Respuestas de los encuestados ---")
        contador = 1
        for respuesta in self.respuestas:
            print(f"\nEncuestado #{contador}")
            contador += 1
            print(f"Nombre: {respuesta['nombre']}")
            print(f"Proyecto: {respuesta['proyecto']}")
            print(f"¿Sabe trabajar en grupo?: {respuesta['trabajo']}")
            print(f"Edad: {respuesta['edad']}")
            print(f"Temas preferidos: {respuesta['temas']}")

def main():
    encuesta = Estudiantes()

    for i in range(10):
        print(f"\n--- Ingresando datos del estudiante {i+1} de 10 ---")
        datos = encuesta.pedir_datos()
        encuesta.agregar_respuesta(datos)

    encuesta.mostrar_respuestas()

if __name__ == "__main__":
    main()

