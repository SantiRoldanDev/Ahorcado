# Proyecto Ahorcado – Python

## Cómo jugar

Desde la raíz del repositorio, ejecuta estos comandos.

```bash
cd hangman_project
python main.py
```

Ingresa una letra por turno. Pierdes al acumular seis errores.
Los espacios y signos de la palabra oculta se muestran desde el comienzo.

## Carpeta principal del proyecto

### 06/11 – ACTUALIZACIÓN (SANTI)

Creación de la estructura del proyecto (carpeta principal, archivo README y archivos Python).

**Estructura de archivos:**

```text
hangman_project/
│
├── main.py          # Bucle del juego
├── game.py          # Clase HangmanGame (lógica del juego)
├── utils.py         # Funciones auxiliares
├── wordlist.txt     # Lista de palabras (una por línea)
└── README.md        # Documentación del proyecto
```

---

## TAREA 0: Creación de estructura y listado de palabras

- Creación de la estructura principal del proyecto.
- Creación del listado de palabras.
- En `main.py` creamos la función `Iniciar()`, que le pide al usuario una letra por turno.

## TAREA 1: Clase UTILS

Creación de la función `get_random_word()` en `utils.py`.

**Funcionamiento de `get_random_word()`:**

- Se abre el archivo `wordlist.txt` utilizando `with open("wordlist.txt", encoding="utf-8")`.
- Se recorre cada línea del archivo.
- Se utiliza `strip()` para eliminar los espacios y saltos de línea.
- Si la línea no está vacía, se guarda en una lista de palabras.
- Finalmente, se retorna una palabra aleatoria utilizando `random.choice(words)`.

## TAREA 2: Clase GAME

Se define una clase `HangmanGame`, con los siguientes atributos:

- `word`: Palabra objetivo. Se obtiene directamente mediante `get_random_word()` al inicializar la clase.
- `guessed_letters`: Conjunto de letras que el usuario ha adivinado.
- `max_errors`: Cantidad máxima de errores permitidos (establecido en 6).
- `errors`: Número de respuestas incorrectas.

**Función `display_progress()`:**

Muestra el progreso de la palabra objetivo según las letras que el usuario ha adivinado.

- Itera sobre cada letra de la palabra objetivo (`word`).
- Se muestran las letras adivinadas y los caracteres que no son letras.
- Las letras pendientes se muestran como `_`.

## TAREA 3: Manejar la entrada del usuario

**Archivo: `main.py`**

Dentro de la función `Iniciar()` que creamos en la Tarea 0:

1. El usuario inicia el juego y se crea una instancia de la clase `HangmanGame`, definida en la Tarea 2.
2. Al crear la instancia, se inicializan sus atributos: palabra objetivo, conjunto de letras adivinadas vacío, cantidad máxima de errores, etc.
3. Definimos una variable `letrasUsadas` para guardar las letras válidas que el usuario ya intentó.
4. Generamos un bucle que se ejecutará mientras el número de errores sea menor a la cantidad máxima permitida y la palabra no esté completada.

**Bucle principal:**

```python
while not Juego.is_won() and not Juego.is_lost():
    letra = input("Adivina una letra: ").lower()
```

**Validaciones posteriores:**

- Comprobar si la entrada del usuario es una letra válida.
- Comprobar si la letra ya fue utilizada anteriormente.
- Mostrar un mensaje de error mediante `print()` cuando alguna de estas validaciones no se cumpla.

---

**FIN ACTUALIZACIÓN 06/11**
