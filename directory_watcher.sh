#/bin/bash

DIR=/$HOME/Dropbox/Hackathon/Hackathon_Team_NSA/soundbites/


inotifywait -m --format '%f' "$DIR" | while read FILE
do
	python wav2text.py $FILE out.txt
	rm $FILE
done


#for f in $files
#do 
#	echo f
#	echo "Break"
#		python wav2text.py f out.txt
#	done
