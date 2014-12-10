#/bin/bash

DIR=$HOME/Mic1Audio

inotifywait -m --format '%f' -e close "$DIR" | while read FILE
do
	sox $DIR/$FILE soundbites/$FILE.out.wav remix 1
	python wav2text.py soundbites/$FILE.out.wav out.txt
done
