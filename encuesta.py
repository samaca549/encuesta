class Estudiantes:
    def __init__(self):
        self.respuestas = []

    def pedir_datos(self):
        print("////////////////////////////")
        print("USUARIO")
        nombre = input("Digite su nombre: ")
        proyecto = input("Digite su proyecto: ")
        trabajo_en_grupo = input("¿Sabe trabajar en grupo?: ")
        edad = int(input("Digite su edad: "))
        temas_preferidos = input("¿Qué temas prefiere para el proyecto?: ")

        return {
            "nombre": nombre,
            "proyecto": proyecto,
            "trabajo_en_grupo": trabajo_en_grupo,
            "edad": edad,
            "temas_preferidos": temas_preferidos
        }

    def agregar_respuesta(self, respuesta):
        self.respuestas.append(respuesta)

    def mostrar_respuestas(self):
        print("\n--- Respuestas de los encuestados ---")
        for i, respuesta in enumerate(self.respuestas, 1):
            print(f"\nEncuesado #{i}")
            print(f"Nombre: {respuesta['nombre']}")
            print(f"Proyecto: {respuesta['proyecto']}")
            print(f"¿Sabe trabajar en grupo?: {respuesta['trabajo_en_grupo']}")
            print(f"Edad: {respuesta['edad']}")
            print(f"Temas preferidos: {respuesta['temas_preferidos']}")

def main ():
    encuesta = Estudiantes()

    for i in range(11):
        datos = encuesta.pedir_datos()
        encuesta.agregar_respuesta(datos)

    encuesta.mostrar_respuestas()


if __name__=="__main__":
    main()
