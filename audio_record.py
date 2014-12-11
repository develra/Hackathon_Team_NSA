import subprocess

fileBase = "sound"
fileIter = 1

while True:
	subprocess.call(["arecord", "-f", "cd", "-q", "-d", "7", "-D", "hw:0,0", "../Mic1Audio/" + fileBase + "_1_" + str(fileIter+1) + ".wav"])
	subprocess.call(["arecord", "-f", "cd", "-q", "-d", "7", "-D", "hw:1,0", "../Mic1Audio/" + fileBase + "_1_" + str(fileIter) + ".wav"])
	fileIter += 2
