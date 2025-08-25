import random

chistes = [
    ("¿Por qué los programadores confunden Halloween con Navidad?", "Porque OCT 31 = DEC 25"),
    ("¿Qué le dijo un bit al otro?", "Nos vemos en el bus."),
    ("Error 404:", "Chiste no encontrado."),
    ("¿Cuál es el lenguaje de programación favorito de los gatos?", "MeowJS."),
    ("¿Por qué los programadores prefieren el modo oscuro?", "Porque la luz atrae bugs."),
    ("¿Cuál es el animal favorito de un programador?", "El bug."),
    ("¿Qué es un terapeuta para programadores?", "Un depurador humano."),
    ("¿Por qué Java fue al gimnasio?", "Porque quería ser más fuerte tipado."),
    ("¿Cuál es el colmo de un programador?", "Tener miedo a los *arrays*."),
    ("¿Por qué el programador se fue a la playa?", "Porque necesitaba un poco de *refresh*."),
]

random.shuffle(chistes)

def mostrar_chistes():
    for setup, punchline in chistes:
        print("\n Chiste de Programadores")
        print(setup)
        input("Presiona ENTER para ver la respuesta...")
        print(punchline)
        opcion = input("\n¿Quieres otro chiste? (s/n): ").strip().lower()
        if opcion != "s":
            print("\n¡Hasta la próxima! ")
            break
mostrar_chistes()