#!/usr/bin/env python3
import random


def get_random_word(dificultad=None):
    words = []
    with open("wordlist.txt", encoding="utf-8") as wordlist:
        for line in wordlist:
            word = line.strip()
            cantidad = 0
            for letter in word:
                if letter.isalpha():
                    cantidad += 1

            if cantidad == 0:
                continue
            if dificultad is None:
                words.append(word)
            elif dificultad == "1" and cantidad <= 5:
                words.append(word)
            elif dificultad == "2" and 6 <= cantidad <= 9:
                words.append(word)
            elif dificultad == "3" and cantidad >= 10:
                words.append(word)

    if not words:
        return None
    return random.choice(words)
