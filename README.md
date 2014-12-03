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