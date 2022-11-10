from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'
language = 'hi'
sp = gTTS(text = '''Hello''', lang= language,slow=False)
sp.save(audio)
playsound(audio)