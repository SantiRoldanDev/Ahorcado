#!/usr/bin/env python3
import utils as utils

class HangmanGame:
    def __init__(self):
        self.word = utils.get_random_word()
        self.guessed_letters = set()
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        #Muestra el progreso del jugador en el juego del ahorcado
        progreso_mostrado = ""
        
        #Itera sobre cada letra de la palabra y 
        #guarda en la variable progreso_mostrado la letra si ha sido adivinada, 
        #o un guion bajo si no lo ha sido.
        for letter in self.word:
            if letter in self.guessed_letters:
                progreso_mostrado += letter + " "
            else:
                progreso_mostrado += "_ "
        print(f"Errores: {self.errors}/{self.max_errors}")
        print(f"Progreso: {progreso_mostrado}")

    def palabra_completa(self):
        #True si ya se adivinaron todas las letras de la palabra.
        return set(self.word) <= self.guessed_letters







    def process_guess(self, letter):
        if letter in self.word:
            self.guessed_letters.add(letter)
            return True
        else:
            self.errors += 1
            return False