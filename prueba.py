import speech_recognition as sr

# Definimos la palabra que queremos deletrear
palabra_correcta = "hola"

# Función para deletrear la palabra y verificar si está correcta
def deletrear():
    recognizer = sr.Recognizer()

    print("Por favor, deletrea la palabra 'hola' letra por letra:")

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        palabra_ingresada = recognizer.recognize_google(audio, language="es-ES")

        # Verificar si la longitud de la palabra ingresada es igual a la de la palabra correcta
        if len(palabra_ingresada) != len(palabra_correcta):
            print("La palabra ingresada no tiene la longitud correcta.")
            return

        # Verificar si la palabra ingresada coincide con la palabra correcta
        for i in range(len(palabra_correcta)):
            if palabra_ingresada[i] != palabra_correcta[i]:
                print("La letra '{}' es incorrecta.".format(palabra_ingresada[i]))
                return

        print("¡Felicidades! Has deletreado la palabra correctamente.")

    except sr.UnknownValueError:
        print("No se ha podido entender la entrada de voz.")
    except sr.RequestError:
        print("Error en la solicitud de reconocimiento de voz. Comprueba tu conexión a internet.")

# Llamamos a la función para comenzar el proceso de deletreo
deletrear()










