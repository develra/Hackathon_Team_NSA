import speech_recognition as sr
import sys
import os
import subprocess
import requests
import json

#Th .wav file to interpret
soundFile=sys.argv[1]
#The file to write the results to, usually .txt
outfile = sys.argv[2]



outf = open(str(outfile), 'w')
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
		#print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
	print(best_prediction["text"])
	for word in best_prediction["text"].split(' '):
		outf.write(word+'\n')
		payload = [{"word":str(word), "variance":""}]
		print payload
		headers = {'content-type': 'application/json'}
		cb = requests.post("http://104.236.60.203:5000/words/", data=json.dumps(payload), headers=headers)
		print (cb)

except LookupError:                               
	print("Could not understand audio - ignoring input")

try: 
	subprocess.call(["rm", soundFile])
except IOError:
	pass
