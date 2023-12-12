import speech_recognition as jarvis
recognizer =jarvis.recognizer('jarvis')
with jarvis.Microphone() as source:
     print('say somethink:')