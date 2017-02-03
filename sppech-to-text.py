import speech_recognition
import sys

audio_filename = sys.argv[1]
out_file = open('output.txt','w')
recognizer = speech_recognition.Recognizer()
recognizer.energy_threshold = 150
recognizer.dynamic_energy_threshold = True

print "loading audio file: " + audio_filename
with speech_recognition.AudioFile(audio_filename) as audio_file:
    # recognizer.adjust_for_ambient_noise(audio_file,5)
    for i in xrange(217):
        audio = recognizer.record(audio_file, 10)

        try:
            text = str(i/6)+":"+str(10*(i%6))+" > "+ recognizer.recognize_sphinx(audio)
            print text
            out_file.write(text+'\n')
        except speech_recognition.UnknownValueError:
            print("Sphinx could not understand audio")
        except speech_recognition.RequestError as e:
            print("Sphinx error; {0}".format(e))
out_file.close()