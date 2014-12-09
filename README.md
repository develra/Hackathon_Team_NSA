Hackathon_Team_NSA
==================

Visualizing Microphone Data from the Atlas Lobby 

wav2text.py --

Dependencies --
Python Speech Recognition Library =>

	pip install SpeechRecognition
	or
	https://github.com/develra/speech_recognition

Usage --

	python wav2text.py inwav.wav outtext.txt

=Black Box Diagram: (Input/Output Data) <br />
==Hardware and Sound Input: Sam and Logan <br />
Voice --->[Sound Processing, splicing] ---> .WAV File <br />
==NLP: Ryan and Michael <br />
.WAV File ---> wav2text.py ---> best prediction of words in .txt file
==Web Server: Peyman <br />
==Visualization: Irfan <br />


WEB API DOCUMENTATION
---------------------

PRODUCTION SERVER ADDRESS: http://104.236.60.203:5000/
STAGING SERVER ADDRESS   : https://teamnsa.herokuapp.com/

// TO REPORT WORDS
POST /words
[ { word: "<word>", variance: "<variance>"}, ... ]

	for example: [ {word: "stand", variance: "ing"}, {word: "hi", variance: ""} ]

// TO GET RECENT WORDS
GET /words/recent?max=<max>&period=<t>
Will return maximum of "max" words within the last "t" seconds.

// TO GET MOST COMMONLY USED WORDS
GET /words/top?max=<max>
