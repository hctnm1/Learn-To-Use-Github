import speech_recognition
# Obtain audio from the microphone
recognizer= speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
  print("Say something:")
audio= recognizer.listen(source)
# Recognize speech using Google Speech Recognition
words= recognizer.recognize_google(audio)
# Respond to speech
if "hello" in words:
  print("Hi there!")
elif "hi girl" in words:
  print("Well i am a boy and i hope you aren't gay")
elif "goodbye" in words:
  print("Goodbye to you too!")
else:
  print("Talk properly")
