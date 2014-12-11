import subprocess

fileBase = "sound"
fileIter = 1

while True:
	subprocess.call(["arecord", "-f", "cd", "-d", "7", "-D", "hw:1,0", "../Mic1Audio/" + fileBase + "_1_" + str(fileIter) + ".wav"])
	#subprocess.call(["arecord", "-f", "S16_LE", "-c", "1", "-r48000", "-d", "7", "-D", "hw:2,0", "../Mic1Audio/" + fileBase + "_2_" + str(fileIter) + ".wav"])	
	fileIter += 1
