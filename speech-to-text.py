import speech_recognition
import sys
import time

audio_filename = sys.argv[1]
out_file = open('output.txt','w')
recognizer = speech_recognition.Recognizer()
recognizer.energy_threshold = 150
recognizer.dynamic_energy_threshold = True

file_len = 2160
chunk = 10
wait = 5
print "loading audio file: " + audio_filename

with speech_recognition.AudioFile(audio_filename) as audio_file:
    
    audio = recognizer.record(audio_file, 300+420+180+420+240+60+300+60+120)
    # recognizer.adjust_for_ambient_noise(audio_file,5)
    for i in xrange(file_len/chunk):
        audio = recognizer.record(audio_file, chunk)
	    # Speech recognition using Google Speech Recognition
        
        try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
            text = str(i*chunk/60)+":"+str((i*chunk)%60)+" > "+ recognizer.recognize_google(audio)
            print text
            out_file.write(text+'\n')
        except speech_recognition.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except speech_recognition.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        if i*chunk%300 == 0:
            time.sleep(30)

out_file.close()

"""
        try:
            text = str(i/6)+":"+str(10*(i%6))+" > "+ recognizer.recognize_google(audio)
            print text
            out_file.write(text+'\n')
        except speech_recognition.UnknownValueError:
            print("Sphinx could not understand audio")
        except speech_recognition.RequestError as e:
            print("Sphinx error; {0}".format(e))
"""