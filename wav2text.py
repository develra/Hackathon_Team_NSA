import speech_recognition as sr
import sys

#The First arugment is a .wav file to interpret
soundFile=sys.argv[1]
#The second argument is a file to write the results to, usually .txt
outfile = sys.argv[2]

outf = open(str(sys.argv[2]), 'w')

r = sr.Recognizer()
with sr.WavFile(soundFile) as source:              
	audio = r.record(source)
try:
	list = r.recognize(audio,True)
	best_prediction = {}
	best_prediction["confidence"] = -1
	best_prediction["text"]=""     
	for prediction in list:
		if best_prediction["confidence"]<prediction["confidence"]:
			best_prediction=prediction
		print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
	for word in best_prediction["text"].split(' '):
		outf.write(word+'\n')

except LookupError:                               
	print("Could not understand audio - attempting SPHINX")
