#!/usr/bin/env python3

import game as game 


#Función principal donde inicia el juego del ahorcado.

def Iniciar():
    print("\n--- Nueva partida ---")
    Juego = game.HangmanGame()
    Juego.display_progress()
    letrasUsadas = set()
    while not Juego.is_won() and not Juego.is_lost():        
        letra = input("\nAdivina una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Ingrese una letra")
            continue
        if letra in letrasUsadas:
            print("Ya has intentado esa letra. Intenta con otra.")
            continue
        if Juego.process_guess(letra):
            print("¡Correcto!")
        else:
            print("Esa letra no está en la palabra.")
        letrasUsadas.add(letra)
        print()
        Juego.display_progress()
    if Juego.is_won():
        print("\n¡Ganaste!")
    else:
        print(f"\nFin del juego. La palabra era: {Juego.word}")

print("Bienvenido al juego del Ahorcado!")
while True:
    Iniciar()
    respuesta = input("\n¿Querés jugar otra vez? (s/n): ").strip().lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input("Ingresá s o n: ").strip().lower()
    if respuesta == "n":
        break
