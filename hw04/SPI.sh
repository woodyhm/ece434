#!/bin/bash
sudo ./on_180.sh
sleep 2
sudo fbi -noverbose -T 1 -a tux.png
sleep 2
sudo ./off.sh
sleep 2

# turn 90 degrees
sudo ./on_90.sh
sleep 2
sudo fbi -noverbose -T 1 -a tux.png
sleep 2
# sudo ./text.sh
# sleep 10
# sudo mplayer RedsNightmare.mpg
sudo ./off.sh