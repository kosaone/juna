import speech_recognition as sr
import gtts
from playsound import playsound
import os

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Ahoj, já jsem Juna. Jak ti mohu pomoci?")
    tts = gtts.gTTS("Ahoj, já jsem Juna. Jak ti mohu pomoci?", lang="cs")
    tts.save("resp.mp3")
    playsound("resp.mp3")
    os.remove("resp.mp3")
    audio = r.listen(source)

# write audio to a WAV file
with open("res.wav", "wb") as f:
    f.write(audio.get_wav_data())

    res=sr.AudioFile('res.wav')
with res as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio, language="cs-CZ")
    print("Odpověď: "+s)
    tts = gtts.gTTS(s, lang="cs")
    tts.save("resp.mp3")
    playsound("resp.mp3")
    os.remove("resp.mp3")

except Exception as e:
    print("Exception: "+str(e))
