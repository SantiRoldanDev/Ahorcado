#!/usr/bin/env python3

import game as game 


#Función principal donde inicia el juego del ahorcado.

def Iniciar():
    print("Bienvenido al juego del Ahorcado!")
    Juego = game.HangmanGame()
    Juego.display_progress()
    letrasUsadas = set()
    while not Juego.is_won() and not Juego.is_lost():        
        letra = input("Adivina una letra: ").lower()
        if letra in letrasUsadas:
            print("Ya has intentado esa letra. Intenta con otra.")
            continue
        if letra in Juego.guessed_letters:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue
        if letra < 'a' or letra > 'z' or len(letra) != 1:
            print("Por favor, ingresa una letra válida.")
            continue
        if letra in Juego.word:
            print("¡Correcto!")
            Juego.guessed_letters.add(letra)
        else:
            Juego.errors += 1
        letrasUsadas.add(letra)
        Juego.display_progress()
    if Juego.is_won():
        print("¡Ganaste!")
    else:
        print(f"Fin del juego. La palabra era: {Juego.word}")
Iniciar()   