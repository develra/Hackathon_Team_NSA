import wave
import struct

print(struct.unpack("HH", b"\x00\x00\x00\x00"))

sound = wave.open("test_audio/voice1.wav",'r')

nchannels, sampwidth, framerate, nframes, comptype, compname =  sound.getparams()
print "Number of channels: " + str(nchannels)
print "Framerate: " + str(framerate) + "Hz"
sounddata = sound.readframes(10)
print sounddata[0]
print sounddata[1]
print sounddata[2]
print sounddata[3]
print sounddata[4]



