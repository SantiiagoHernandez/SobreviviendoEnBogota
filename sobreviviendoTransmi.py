print("Hola!!! Bienvenido a -Sobreviviendo a un viaje en Transmilenio🚩- ")
nombre = input("¿cual es tu nombre? 🫡 ")
print("Que comience la travesia!!! 🚌 ")
print(nombre, "vamos a hacer un viaje por Bogota a la estacion Av. Jimenez, nuestro punto de partida sera el portal Americas 👾 ")
print("-Deberas escoger la opcion mas factible- -Selecciona la opcion {1} o {2} para confirmar tu respuesta-  -Solo tienes una oportunidad- ")
print("🚩 Para ingresar a el portal Americas tienes dos opciones: ")
print("1. Pagar el pasaje ")
print("2. Colarse, evadiendo la seguridad ")

intento = 0
while (intento == 0):
    respuesta = int(input("¿Qué opción eliges? 🤨 "))
    if respuesta == 1:
        print("Excelente", nombre, "!!! 🎊 ", "Seguimos con el viaje. Pagar el pasaje refleja tu gran cultura Bogotana 🚌 ")

    else:
        print("Ups!!", nombre, "tienes una multa. Colarse no es ejemplo de un buen ciudadano 😔 ")
        exit()

    print("🚩 Ahora, debemos seleccionar el número de Transmilenio que vamos a coger y su número de plataforma, tienes dos opciones: ")
    print("1. J23(LAS AGUAS) plataforma 2 ")
    print("2. E32(CRA. 30) plataforma 1")

    intento = 0
    while (intento == 0):
        respuesta2 = int(input("¿Qué opción eliges? 🤨 "))
        if respuesta2 == 1:
            print("Grandioso", nombre, "!!! 🎊 ", "Se nota que conoces la ruta. Sigamos con nuestra travesia")

        else:
            print("Ups!!", "Opción incorrecta", nombre, ".", "E32 se dirige hacia el norte, nuestro destino es el centro de la ciudad 😭.")
            exit()

        print("🚩 El transporte ha llegado 🚌. El bus viene lleno, hay poco espacio para subir. ", nombre, "tienes dos opciones: ")
        print("1. Subir al bus ")
        print("2. Esperar el siguiente Transmilenio ")

        intento = 0
        while (intento == 0):
            respuesta3 = int(input("¿Qué opción eliges? 🤨 "))
            if respuesta3 == 2:
                print("Gran elección", nombre, "!!! 🎊", "Es mejor esperar que incomodar y estar incomodo")

            else:
                print("Ups!! Mala elección", nombre, ".", "Procura mejorar la experiencia del transporte para todos sin aglomerarlo 👊")
                exit()

            print("🚩 Estas sentado junto a la ventanilla del Transmilenio, quieres sacar tu celular 📱.", nombre, "¿Qué haces?, tienes dos opciones: ")
            print("1. Cierra la ventanilla ")
            print("2. Dejar la ventanilla abierta ")

            intento = 0
            while (intento == 0):
                respuesta4 = int(input("¿Qué opción eliges? 🤨 "))
                if respuesta4 == 1:
                    print("Gran elección", nombre, "!!! 🎊", "Es importante prevenir accidentes. Tu celular esta a salvo 😌. ")

                else:
                    print("Ups!!", nombre, "te han robado tu dispositivo móvil 😫. Hay que prevenir, la ciudad esta insegura ")
                    exit()

                print("🚩", nombre, "vamos en la estación de puente Aranda 👍.  Tienes sueño llevas tu mochila con tus objetos personales dentro, tienes dos opciones ")
                print("1. Pones la mochila entre tus piernas en el piso ")
                print("2. Pones tu mochila encima de tus piernas y la abrazarla ")

                intento = 0
                while (intento == 0):
                    respuesta5 = int(input("¿Qué opción eliges? 🤨 "))
                    if respuesta5 == 2:
                        print("Tus objetos personales están a salvo", nombre, "!!! 🎊", "Sigamos con el viaje 🚌")
                    else:
                        print("Ups!! Te han robado tu mochila con tus objetos personales", nombre, "😫.", "Hay que prestar atención a los robos, estamos en una ciudad insegura")
                        exit()

                    print("🚩 Un frenazo en seco te ha despertado, y notas que hay una mujer embarazada con un niño en brazos 🤰. ¿Qué haces", nombre, "? 🤨" ) 
                    print("1. Sigues durmiendo ")
                    print("2. Le sedes el asiento a la mujer ")

                    intento = 0
                    while (intento == 0):
                        respuesta6 = int(input("¿Qué opción eliges? 🤨 "))
                        if respuesta6 == 2:
                            print("Gran elección", nombre, "!!! 🎊", "Tienes una gran empatía con los demás ")
                        else:
                            print("No tienes educación", nombre, "🫤.", "Hay que darle prioridad a mujeres embarazadas, con niños en brazos o adultos mayores ☝️. ")
                            exit()

                        print("🚩", nombre, "estas a punto de llegar a la estación Av. Jiménez, llevas el celular en tus manos es hora de salir del bus, ¿Qué harás con tu celular? 🤷‍♂️") 
                        print("1. Guardar el celular ")
                        print("2. Salir con el celular en las manos ")

                        intento = 0
                        while (intento == 0):
                            respuesta7 = int(input("¿Qué opción eliges? 🤨 "))
                            if respuesta7 == 1:
                                print("Gran trabajo", nombre, "!!! 🎊", "Tu celular esta a salvo. Gran habilidad para cuidar tus objetos personales 👌")
                            else:
                                print("Te han robado el celular", nombre, "😔.", "Presta atención a tus alrededores, guarda el teléfono.")
                                exit()

                            print("Gran trabajo", nombre, "!!! 🎊", "tu celular esta a salvo. Gran habilidad para cuidar tus objetos personales")
                            print("Haz llegado a tu destino!!! 🥳 Eres un gran viajero", nombre, "🚌,", "haz sobrevivido a una travesia por el Transmilenio en Bogotá. FELICITACIONES!!! 🎉🎉🎉")
                            exit()
