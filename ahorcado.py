import random
import funciones;

words = ["tecnologia", "programacion", "computadora", "mouse", "ordenador", "pantalla"]
count = 6
guessed = []

random_word = random.choice(words)
print(random_word)

main_display = "_" * len(random_word)

while(count > 0):
    print(main_display)
    
    if "_" not in main_display:
        print("Ganaste el juego!! La palabra era: " + random_word)
        break

    letter = input("Ingrese una letra: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Ingreso mas de una letra. Intente nuevamente.")
        continue

    if letter not in guessed: 
        guessed.append(letter)

        if letter in random_word:
            main_display = funciones.guess(random_word, guessed)
            print("Letra correcta. ")
        else:
            count -= 1
            print(f"Incorrecto. {count} intentos restantes.")
    else:
        print("Letra ingresada anteriormente. Intente con otra.")
        continue
    

else:
    print(f"La palabra oculta era: {random_word}")