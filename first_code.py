import random
import sys

# Intentamos usar colorama para compatibilidad con Windows; si no está, definimos colores vacíos.
try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
    COLORS_AVAILABLE = True
except Exception:
    COLORS_AVAILABLE = False
    # Definimos constantes vacías para no romper el resto del código.
    class _Empty:
        RESET_ALL = ""
    class _Fore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
    Fore = _Fore()
    Style = _Empty()


PALETTES = {
    "neón": {
        "title": Fore.MAGENTA,
        "prompt": Fore.CYAN,
        "hint_low": Fore.BLUE,
        "hint_high": Fore.YELLOW,
        "success": Fore.GREEN,
        "error": Fore.RED,
    },
    "pastel": {
        "title": Fore.WHITE,
        "prompt": Fore.MAGENTA,
        "hint_low": Fore.CYAN,
        "hint_high": Fore.BLUE,
        "success": Fore.MAGENTA,
        "error": Fore.RED,
    },
    "cálido": {
        "title": Fore.YELLOW,
        "prompt": Fore.RED,
        "hint_low": Fore.MAGENTA,
        "hint_high": Fore.YELLOW,
        "success": Fore.GREEN,
        "error": Fore.RED,
    },
    "monocromo": {
        "title": Fore.WHITE,
        "prompt": Fore.WHITE,
        "hint_low": Fore.WHITE,
        "hint_high": Fore.WHITE,
        "success": Fore.WHITE,
        "error": Fore.WHITE,
    },
}


def color(text: str, color_code: str) -> str:
    """Aplica color si está disponible, si no devuelve el texto sin cambios."""
    if COLORS_AVAILABLE and color_code:
        return f"{color_code}{text}{Style.RESET_ALL}"
    return text


def elegir_paleta() -> dict:
    """Permite al usuario elegir una paleta de colores o seleccionar aleatoriamente."""
    nombres = list(PALETTES.keys())
    print("Elige una paleta de colores:")
    for i, name in enumerate(nombres, start=1):
        # Mostramos una vista previa con color si está disponible
        preview = color("■", PALETTES[name]["title"])
        print(f"  {i}. {name} {preview}")
    print("  Enter (vacío) = aleatoria  |  q = salir")

    seleccion = input("Selecciona número o deja Enter para aleatoria: ").strip().lower()
    if seleccion == "q":
        print("Saliendo. ¡Hasta luego!")
        sys.exit(0)
    if seleccion == "":
        elegido = random.choice(nombres)
        print(f"Paleta aleatoria seleccionada: {elegido}")
        return PALETTES[elegido]
    try:
        idx = int(seleccion) - 1
        if 0 <= idx < len(nombres):
            elegido = nombres[idx]
            print(f"Has elegido: {elegido}")
            return PALETTES[elegido]
    except ValueError:
        pass

    print("Entrada no válida, usando paleta por defecto.")
    return PALETTES[nombres[0]]


def juego_adivinanza():
    paleta = elegir_paleta()

    titulo = color("--- ¡Bienvenido al Juego de Adivinanza! ---", paleta["title"])
    instrucciones = color("He pensado un número entre 1 y 100. ¡Intenta adivinarlo!", paleta["prompt"])

    print(titulo)
    print(instrucciones)

    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinanza = None

    while adivinanza != numero_secreto:
        try:
            entrada = input(color("Introduce tu número: ", paleta["prompt"]))
            adivinanza = int(entrada)
            intentos += 1

            if adivinanza < numero_secreto:
                print(color("🔽 Demasiado bajo. ¡Intenta de nuevo!", paleta["hint_low"]))
            elif adivinanza > numero_secreto:
                print(color("🔼 Demasiado alto. ¡Intenta de nuevo!", paleta["hint_high"]))
            else:
                print(color(f"🎉 ¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.", paleta["success"]))

        except ValueError:
            print(color("⚠️ Error: Por favor, ingresa un número válido (ej. 50).", paleta["error"]))


if __name__ == "__main__":
    if not COLORS_AVAILABLE:
        print("Nota: colorama no está instalado. Los colores pueden no mostrarse correctamente en Windows.")
        print("Para instalar colorama, ejecuta: pip install colorama\n")
    juego_adivinanza()
