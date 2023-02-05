
# ***task:  speech recognition program that takes audio file as input
# and produces texts as output of the transcribed file ***

# to run this program, internet connection is required

# importing the speech recognition package
import speech_recognition as sr

# creating an instance of the speech reognition recognizer class
rg = sr.Recognizer()

# collecting the data from a prerecoded audio file

test_audio = sr.AudioFile('test_audio2.wav')
with test_audio as source:
    input = rg.record(source)

    # getting output with the re instance using google speech recgnition API
    output = rg.recognize_google(input)

    print(output)

