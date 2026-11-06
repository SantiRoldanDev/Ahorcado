Carpeta principal de proyecto ahorcado.


=======================================================================================
06/11 ACTUALIZACIÓN (SANTI)
=======================================================================================
Creación de estructura de proyecto (carpeta principal, archivo readme, y archivos python)

Estructura de archivos:
    hangman_project/
        │
        ├── main.py # Bucle del juego
        ├── game.py # Clase HangmanGame (lógica del juego)
        ├── utils.py # Funciones auxiliares 
        ├── wordlist.txt # Lista de frases (una por línea)
        └── README.md # Instrucciones y descripción del juego


TAREA 0: 
        - Creación de estructura y listado de palabras.
        - En main.py creamos la función Iniciar() que realiza la tarea 3 de solicitar una palabra.
        
TAREA 1: CLASE UTILS
    - Creación de funcion en utils.py: get_random_word().
    - get_random_word():
        - Se abre el archivo wordlist con with open("wordlist.txt", encoding="utf-8") as wordlist
        - Se recorre cada linea del archivo y se hace Split() que elimina los espacios y saltos de linea, si la linea es diferente a vacía se guarda en una lista de palabras.
        - Se retorna una de las palabras de la lista words con random.choice(words)

TAREA 2: 
CLASE GAME:
    - Se define una clase Game, con los atributos:
        - word: Palabra objetivo llama directamente a get_random_word() al inicializarse.
        - guessed_letters: las letras que el usuario ha adivinado
        - max_errors: maxima cantidad de errores posibles (establecido en 6)
        - errors: numero de respuestas incorrectas
    - Función display_progress(): Muestra las letras adivinadas en guessed_letters 
        - Itera sobre cada letra de la palabra objetivo de la clase (atributo word)
        - Si la letra se encuentra dentro de las letras adivinadas (guessed_letters), se muestra la letra y continua iterando, si no la encuentra se muestra un _.
        
TAREA 3:
MANEJAR LA ENTRADA DEL USUARIO
ARCHIVO MAIN.PY

En la función Iniciar que nombramos en la TAREA 0:
    - El usuario ingresa y se crea la clase HangmanGame definida en la tarea 2.
        - Al crearla la tendremos seteada con una palabra objetivo, una listas de palabras adivinadas vacia, etc como se define en la Tarea 2.
    - Definimos una variable letras usadas para guardar todas las letras que el usuario ingrese (esto es para un paso mas adelante)
    - Generamos un bucle donde mientras el numero de errores sea menor a la cantidad maxima de errores y no esté la palabra completada se siguen solicitando palabras.

        while Juego.errors < Juego.max_errors and not Juego.palabra_completa():
            letra = input("Adivina una letra: ").lower()
    
    - Debajo se hacen diferentes validaciones:
        - si es una letra valida.
        - Si es una letra que ya se intentó
    Reproduce un mensaje de error por ahora solo un print() cuando pasa.

FIN ACTUALIZACIÓN 6/11
==========================================================================================