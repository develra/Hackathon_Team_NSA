import subprocess

fileBase = "sound_"
fileIter = 1

#showIP = subprocess.check_output(["ifconfig"])
#subprocess.call(["ifconfig", "|", "mail", "-s", "piP", "korn94sam@gmail.com"])
for i in xrange(1,10):
	subprocess.call(["arecord", "-f", "cd", "-d", "5", "-D", "hw:1,0", "soundbites/" + fileBase + str(fileIter) + ".wav"])
	#subprocess.call(["arecord", "-f", "S16_LE", "-t", "raw", "-r22050", "-d", "5", "-D", "hw:1,0", "soundbites/" + fileBase + str(fileIter) + ".wav"])
	fileIter += 1
#print showIP
