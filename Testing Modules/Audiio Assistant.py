from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'
language = 'hi'
sp = gTTS(text = '''Let r be a positive integer. By an r-permutation of a set S of n elements, we understand 
an ordered arrangement of r of the n elements. ''', lang= language,slow=False)
sp.save(audio)
playsound(audio)