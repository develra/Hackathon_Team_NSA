#/bin/bash
DIR=/home/pi/Mic1Audio

python Pixel_Animation.py &
python audio_record.py &

inotifywait -m --format '%f' -e close_write "$DIR" | while read FILE
do	
	sox $DIR/$FILE /home/pi/Hackathon_Team_NSA/soundbites/$FILE remix 1
	rm -f $DIR/$FILE
	python wav2text.py soundbites/$FILE out.txt
done

trap "kill 0" SIGINT SIGTERM EXIT
