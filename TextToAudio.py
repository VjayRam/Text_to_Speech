from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
lang = 'en'
msg = input("Enter the text to be played:")
sp = gTTS(text=msg, lang=lang, slow=False)
sp.save(audio)
playsound(audio)