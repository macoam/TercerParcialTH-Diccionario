import speech_recognition as sr 
import time 
from time import ctime 
import webbrowser
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try: 
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('Lo siento, no te entendí, ¿podrías repetirlo de nuevo?')
        except sr.RequestError:
            alexa_speak('Lo siento, error de conexión')
        return voice_data


def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang="es")
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if 'buscar' in voice_data:
        buscar = record_audio('¿Qué definición quieres buscar? (para mejor resultado, decir antes de la palabra: definición de')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('¿Esto es lo que buscabas?: ' + buscar)
    if 'primero' in voice_data:
        alexa_speak ('El corazón puede mover un automovil. La potencia generada al día por un corazón bastaría para mover un coche durante 32 kilómetros.')
    if 'segundo' in voice_data:
        alexa_speak ('Los peces también toman agua. Los peces de agua dulce simplemente la beben y ya, pero los peces que viven en el mar tienen la capacidad de eliminar el exceso de sal que ingieren junto con el agua.')
    if 'tercero' in voice_data:
        alexa_speak ('Las manzanas tienen aire. Haz la prueba y tira una manzana en un bote de agua. Verás que la fruta flota. Esto se debe a que están compuestas hasta en un 25% por aire.')
    if 'hora' in voice_data:
        alexa_speak(ctime())
      

time.sleep(1)
alexa_speak('¡Hola! Soy tu diccionario, estoy aquí para darte definiciones, tambíen puedes preguntarme algunos datos interesantes y hasta la hora. Para las definiciones la palabra es: buscar, para el dato curioso es: primero, segundo o tercero y para la hora es: tiempo. Ahora dime ¿Cómo te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data) 