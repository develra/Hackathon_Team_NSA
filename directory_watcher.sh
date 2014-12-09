#/bin/bash

: dir = $HOME/soundbites
: FILES = $HOME/soundbites/*
chsum1=`digest -a md5 $dir | awk '{print $dir}'`
chsum2=$chsum1

while [$chsum1 -eq $chsum2]
	do
		sleep 5
		chsum2=`digest -a md5 $dir | awk '{print $dir}'`
	done
	for f in $files
	do 
		echo f
		echo "Break"
		python wav2text.py f out.txt
	done
