import random


def adivina_el_numero_computadora(x):

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("         ! AlOhA illa !")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"Piensa en un numero entre 1 y {x} para que la Pc intente adivinarlo ...")

    límite_inferior = 1
    límite_superior = x
    
    respuesta = ""

    while respuesta != "c":
        #generar prediccion
        if límite_inferior != límite_superior: #[1, 10]
            predicción = random.randint(límite_inferior, límite_superior)
        else: 
            predicción = límite_inferior	#tambien podria ser el limite superior.

        #obtener una respuesta del usuario
        respuesta = input(f"mi prediccion es {predicción}. si es muy alta, ingresa (A). si es muy baja, ingresa (B). si es correcto, ingresa (C)").lower()

        if respuesta == "a":
            límite_superior = predicción -1
        elif respuesta == "b":
            límite_inferior = predicción +1


            #intervalo inicial:[1, 10]
            #prediccion: 6
            #respuesta: b
            #intervalo: [7,10]

    print(f"YASSSS, la pc es una pro, una crack, adivino tu numero! : {predicción}")


adivina_el_numero_computadora(10)
