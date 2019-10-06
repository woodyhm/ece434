#!/bin/bash
sudo ./on_180.sh
sleep 1
sudo fbi -noverbose -T 1 -a tux.png
sleep 2
sudo ./off.sh
sleep 1

# turn 90 degrees
sudo ./on_90.sh
sleep 1
sudo fbi -noverbose -T 1 -a tux.png
sleep 2
sudo ./text.sh
sleep 2
sudo ./off.sh
sleep 1
sudo ./on_90.sh
sleep 1
mplayer Luna2.mp4
sudo ./off.sh