import random

# Elige y comprueba la dificultad
def elige_dificultad():
    dif = input("""Elija la dificultad en la que quiere jugar:
    Facil   (F)
    Medio   (M)
    Dificil (D)
    """).upper()
    while dif != "F" and dif != "M" and dif != "D":
        dif = input("""Caracter ingresado no valido.
        Elija la dificultad en la que quiere jugar:
        Facil   (F)
        Medio   (M)
        Dificil (D)
        """).upper()
    return dif

# Imprime la palabra segun la dificultad elegida 
def imprimir_facil(secret_word, lista):
    letters = []
    for i in ["a","e","i","o","u"]:
        if not i in lista:
            lista.append(i)

    for letter in secret_word:
        if letter in lista:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    return word_displayed

def imprimir_medio(secret_word, lista):
    letters = []
    letters.append(secret_word[0])
    rango = len(secret_word) -1
    for i in range(1,rango):
        if secret_word[i] in lista:
            letters.append(secret_word[i])
        else:
            letters.append("_")
    letters.append(secret_word[-1])
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    return word_displayed

def imprimir_dificil(secret_word, lista):
    letters = []
    for letter in secret_word:
        if letter in lista:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    return word_displayed

def imprimir_segun_dificultad (dif,secret_word,lista):
    if dif == "F":
        word_displayed = imprimir_facil(secret_word, lista)
    elif dif == "M":
        word_displayed = imprimir_medio(secret_word, lista)
    else:
        word_displayed = imprimir_dificil(secret_word, lista)
    return word_displayed

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos 
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
dificultad = elige_dificultad()
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = imprimir_segun_dificultad(dificultad,secret_word,guessed_letters)
intentos = 0

while intentos < max_attempts and word_displayed != secret_word:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingrese una letra: ").lower()

    # Muestra un error en caso de ingresar un string vacio
    cond = bool(letter)
    while not cond:
        letter = input("No se ha ingresando ninguna letra. Ingrese una letra: ").lower()
        cond = bool(letter)

    # Muestra un error en caso de ingresar mas de una letra
    while len(letter) != 1:
        letter = input("Se ha ingresado mas de una letra. Ingrese una letra")

    # Verificar si la letra ya ha sido adivinada
    while letter in guessed_letters:
        letter = input("Ya has intentado con esa letra. Intente con otra: ").lower()
    
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        intentos += 1
        if max_attempts - intentos > 0:
            print(f"Te quedan {max_attempts - intentos} intentos")
    
    # Mostrar la palabra parcialmente adivinada
    word_displayed = imprimir_segun_dificultad(dificultad,secret_word,guessed_letters)
    
# Verificar si se ha adivinado la palabra completa
if word_displayed == secret_word:
    print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")