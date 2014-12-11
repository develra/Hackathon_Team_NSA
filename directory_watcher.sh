#/bin/bash
DIR=$HOME/Mic1Audio

python audio_record.py &

inotifywait -m --format '%f' -e close_write "$DIR" | while read FILE
do	
	sox $DIR/$FILE $HOME/Hackathon_Team_NSA/soundbites/$FILE remix 1
	rm $DIR/$FILE
	python wav2text.py soundbites/$FILE out.txt
done

trap "kill 0" SIGINT SIGTERM EXIT
