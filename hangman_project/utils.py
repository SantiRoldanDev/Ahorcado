#!/usr/bin/env python3
import random

def get_random_word():
    #Obtener una palabra random de la lista de palabras.
    #Como funciona:     
    #se leen todas las palabras y se elige una al azar.
    
    #Se abre el archivo wordlist.txt, (open(wordlist.txt))
    with open("wordlist.txt", encoding="utf-8") as wordlist:
        #Se leen todas las palabras y se elige una al azar.
        #Se eliminan los espacios en blanco al inicio y al final de cada palabra con strip
        #En strip() si la palabra está vacia, el if da false y no se agrega a la lista words.
        words = []
        for line in wordlist: #se recorre cada línea del archivo wordlist.txt
            if line.strip(): #si la palabra no está vacía se agrega a words
                words.append(line.strip()) 

    return random.choice(words) #se selecciona una palabra al azar de la lista de words y se devuelve.


