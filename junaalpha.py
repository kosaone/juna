import speech_recognition as sr
import gtts
from playsound import playsound
import os
import wolframalpha
from googletrans import Translator
translator = Translator()
app_id = "WEE6TH-92ALK8REX8"
client = wolframalpha.Client(app_id)

r = sr.Recognizer()
def order(result):
    fullstring = result
    substring = "Kdo je"
    substring2 = "Co je"

    if result == "ahoj":
        response("Ahoj! Kdyby jsi něco potřeboval jsem tu pro tebe.")

    if result == "test":
        response(input("Debugging:"))

    if substring in fullstring or substring2 in fullstring:
        question = translator.translate(result, src="cs", dest="en")
        res = client.query(question.text)
        answer = next(res.results).text
        answered = translator.translate(answer, src="en", dest="cs")
        response("Odpověď na vaši otázku je: "+answered.text)

    if result == "jak se máš":
        response("Ale jo, pomáhám ti takže super.")

    else:
        response("Bohužel jsem vám nerozuměla. Mohl by jste to zopakovat prosím?")


def voice():
    with sr.Microphone() as source:
        playsound("beep.mp3")
        audio = r.listen(source)
        with open("res.wav", "wb") as f:
            f.write(audio.get_wav_data())
            res=sr.AudioFile('res.wav')
            with res as source:
                audio = r.record(source)
                try:
                    s = r.recognize_google(audio, language="cs-CZ")
                    print("Uživatel: "+s)
                    order(s)
                except Exception as e:
                    print("Chyba: "+str(e))

def voiceone():
    with sr.Microphone() as source:
        print("Ahoj, já jsem Juna. Jak ti mohu pomoci?")
        tts = gtts.gTTS("Ahoj, já jsem Juna. Jak ti mohu pomoci?", lang="cs")
        tts.save("resp.mp3")
        playsound("resp.mp3")
        os.remove("resp.mp3")
        playsound("beep.mp3")
        audio = r.listen(source)
        with open("res.wav", "wb") as f:
            f.write(audio.get_wav_data())
            res=sr.AudioFile('res.wav')
            with res as source:
                audio = r.record(source)
                try:
                    s = r.recognize_google(audio, language="cs-CZ")
                    print("Uživatel: "+s)
                    order(s)
                except Exception as e:
                    print("Chyba: "+str(e))


def response(response):
    tts = gtts.gTTS(response, lang="cs")
    tts.save("odpoved.mp3")
    playsound("odpoved.mp3")
    os.remove("odpoved.mp3")
    voice()
voiceone()