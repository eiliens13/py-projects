import random

def adivina_el_número(x):

    print("=================================")
    print("      AlOhA al Juego   ")
    print("=================================")
    print("tu meta es adivinar el numero generado por la computadora")

    número_aleaotrio = random.randint(1, x) #numero aleatorio entre 1 y x.

    predicción = 0

    while predicción != número_aleaotrio:
        #el usuario ingresa un numero
        predicción = int(input(f"Adivina un número entre 1 y {x}: ")) #f-string
        
        if predicción < número_aleaotrio:
            print("Intenta otra vez iello, este numero es muy pequeño.")
        elif predicción > número_aleaotrio:
                print("intenta nuevamente. este numero es muy grande.")

    print(f" ! Felicitaciones adivinaste el numero {número_aleaotrio} correctamente.")


adivina_el_número(10)