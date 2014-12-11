#/bin/bash
DIR=$HOME/Mic1Audio

sudo python Pixel_Animation.py &
python audio_record.py &

trap 'sudo kill $(jobs -p)' EXIT

inotifywait -m --format '%f' -e close_write "$DIR" | while read FILE
do	
	sox $DIR/$FILE $HOME/Hackathon_Team_NSA/soundbites/$FILE remix 1
	rm -f $DIR/$FILE
	python wav2text.py soundbites/$FILE $HOME/Hackathon_Team_NSA/nsaStem/out1.txt
done
