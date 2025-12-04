import random

def juego_adivinanza():
    # 1. Generar un número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinanza = None
    
    print("--- ¡Bienvenido al Juego de Adivinanza! ---")
    print("He pensado un número entre 1 y 100.")
    print("¡Intenta adivinarlo!")

    # 2. Ciclo para pedir al usuario que adivine
    while adivinanza != numero_secreto:
        try:
            # Solicitamos la entrada del usuario
            entrada = input("Introduce tu número: ")
            adivinanza = int(entrada)
            intentos += 1

            # 3. Dar pistas y verificar
            if adivinanza < numero_secreto:
                print("🔽 Demasiado bajo. ¡Intenta de nuevo!")
            elif adivinanza > numero_secreto:
                print("🔼 Demasiado alto. ¡Intenta de nuevo!")
            else:
                # 4. Terminar el juego
                print(f"🎉 ¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        
        except ValueError:
            print("⚠️ Error: Por favor, ingresa un número válido (ej. 50).")

# Ejecutar el juego
if __name__ == "__main__":
    juego_adivinanza()
