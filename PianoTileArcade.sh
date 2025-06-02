#!/bin/bash

xdotool mousemove 1280 1024
cd projet/PianoTile
touch highscore
python -cp .:../..:/home/pi/PianoTileArcade/app/python PianoTile