import random

# Base de chistes
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

def obtener_chiste():
    """Devuelve un chiste aleatorio (setup, punchline)."""
    return random.choice(chistes)

def mostrar_chistes():
    vistos = 0
    print("🤣 Bienvenido al generador de Chistes de Programadores 🤓\n")

    while True:
        setup, punchline = obtener_chiste()
        print("💻 Chiste de Programadores")
        print(f"👉 {setup}")
        input("🔎 Presiona ENTER para ver la respuesta...")
        print(f"😂 {punchline}\n")
        
        vistos += 1
        opcion = input("¿Quieres otro chiste? (s/n): ").strip().lower()
        if opcion != "s":
            print(f"\nMostraste {vistos} chiste(s). ¡Hasta la próxima! 👋")
            break

# Ejecutar
if __name__ == "__main__":
    mostrar_chistes()
