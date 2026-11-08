# Ahorcado

Proyecto grupal de UTEC. El juego está hecho en Python y se juega desde la consola.

## Cómo jugar

Desde la raíz del repositorio, ejecuta estos comandos en la terminal de VS Code.

```powershell
cd hangman_project
python main.py
```

Al iniciar cada partida, elige la dificultad. Fácil tiene hasta 5 letras, medio
tiene de 6 a 9 y difícil tiene 10 o más. Los espacios y los signos quedan fuera
del conteo.

Ingresa una letra por turno. Tienes seis intentos incorrectos antes de perder.

## Estructura del proyecto

Creación de la estructura del proyecto (carpeta principal, archivo README y archivos Python).

```text
hangman_project/
│
├── main.py          # Bucle del juego
├── game.py          # Clase HangmanGame (lógica del juego)
├── utils.py         # Funciones auxiliares
├── wordlist.txt     # Lista de palabras y títulos (uno por línea)
└── README.md        # Instrucciones y descripción del juego
```

## Tarea 0. Estructura y listado de palabras

- Creación de la estructura principal del proyecto.
- Creación del listado de palabras.
- En `main.py` creamos la función `Iniciar()`, que se encargará de realizar la Tarea 3: solicitar una letra al usuario.

## Tarea 1. Carga de una palabra desde un archivo

Creación de la función `get_random_word()` en `utils.py`.

### Funcionamiento de `get_random_word()`

- Se abre el archivo `wordlist.txt` utilizando `with open("wordlist.txt", encoding="utf-8")`.
- Se recorre cada línea del archivo.
- Se utiliza `strip()` para eliminar los espacios y saltos de línea.
- Si la línea no está vacía, se guarda en una lista de palabras.
- Finalmente, se retorna una palabra aleatoria utilizando `random.choice(words)`.

## Tarea 2. Clase `HangmanGame`

Se define una clase `HangmanGame`, con los siguientes atributos:

- `word`: Palabra objetivo. Se obtiene directamente mediante `get_random_word()` al inicializar la clase.
- `guessed_letters`: Conjunto de letras que el usuario ha adivinado.
- `max_errors`: Cantidad máxima de errores permitidos (establecido en 6).
- `errors`: Número de respuestas incorrectas.

### Método `display_progress()`

Muestra el progreso de la palabra objetivo según las letras que el usuario ha adivinado.

- Itera sobre cada letra de la palabra objetivo (`word`).
- Se muestran las letras adivinadas y los caracteres que no son letras.
- Las letras pendientes se muestran como `_`.

## Tarea 3. Entrada del usuario

**Archivo: `main.py`**

Dentro de la función `Iniciar()` que creamos en la Tarea 0:

1. El usuario inicia el juego y se crea una instancia de la clase `HangmanGame`, definida en la Tarea 2.
2. Al crear la instancia, se inicializan sus atributos: palabra objetivo, conjunto de letras adivinadas vacío, cantidad máxima de errores, etc.
3. Definimos una variable `letrasUsadas` para guardar las letras válidas que el usuario ya intentó.
4. Generamos un bucle que se ejecutará mientras el número de errores sea menor a la cantidad máxima permitida y la palabra no esté completada.

### Bucle principal

```python
while not Juego.is_won() and not Juego.is_lost():
    letra = input("\nAdivina una letra: ").lower()
```

### Validaciones de entrada

- Comprobar si la entrada del usuario es una letra válida.
- Comprobar si la letra ya fue utilizada anteriormente.
- Mostrar un mensaje de error mediante `print()` cuando alguna de estas validaciones no se cumpla.

## Tarea 4. Actualización del estado del juego

`process_guess` en `HangmanGame` (`game.py`).

## Tarea 5. Progreso del juego

Se muestran letras adivinadas e intentos restantes en `display_progress` (`game.py`).

## Tarea 6. Condiciones de fin del juego

`is_won` e `is_lost` en `game.py`, y fin del juego con mensaje en `main.py`.

## Tarea 7. Revelado automático y mejoras del juego

- Los espacios y signos se muestran desde el inicio. Para ganar solo hay que adivinar las letras.
- El juego valida que se ingrese una letra por turno y avisa si ya se intentó. Cada letra válida y nueva se procesa con `process_guess()`, y el juego indica si fue un acierto o un error.
- La lista incluye palabras y títulos de películas.
- Los turnos están separados por líneas en blanco para que se lea mejor el progreso.
- Al ganar o perder, el juego pregunta si quieres jugar otra vez. Con `s` empieza una nueva partida y con `n` termina.

## Tarea 8. Niveles de dificultad

Al comenzar cada partida, el jugador elige fácil (hasta 5 letras), medio
(de 6 a 9) o difícil (10 o más). El juego elige al azar una entrada del nivel.
Los espacios y los signos quedan fuera del conteo. Todos los niveles permiten
hasta seis errores.
