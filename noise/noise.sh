#!/bin/bash

# can be installed with brew install switchaudio-osx
if ! [ -x "$(which SwitchAudioSource)" ]; then
  echo "switchaudio-osx not installed"
  exit 1
fi

desiredInterface="Komplete Audio 6"
currentInterface=`SwitchAudioSource -c`

echo -e "desired interface:\t$desiredInterface"
echo -e "current interface:\t$currentInterface"

if [ "$currentInterface" == "$desiredInterface" ]; then
  afplay -v 0.4 ~/Desktop/tom/noise.wav &
else
  echo "desired interface not connected"
  exit
fi

audiopid=`echo $!`
echo -e "afplay pid:\t\t$audiopid"
echo "playing! ▶️"

trap "kill $audiopid; exit" SIGHUP SIGINT SIGTERM


while true; do
  currentInterface=`SwitchAudioSource -c`
  if [ "$currentInterface" != "$desiredInterface" ]; then
    echo "disconnected"
    osascript -e 'set volume output muted true'
    kill $audiopid
    break
  fi
  sleep 0.5
done
