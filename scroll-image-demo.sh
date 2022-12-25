#!/bin/bash

reset

# Print some text to fill the scrolling region
for i in {1..20}; do
  if [[ "$i" == 4 || "$i" == 16 ]]; then
    echo "===================="
  else
    echo "Line $i"
  fi
done

# These small images are outside of the region and shouldn't move
for i in {20..21}; do
  kitty icat --place 1x1@${i}x3 ./logo/kitty.png
  kitty icat --place 1x1@${i}x15 ./logo/kitty.png
done

kitty icat --place 22x9@9x5 ./logo/kitty.png

sleep 0.5

# Move lines down
for i in {1..3}; do
  echo -en "\033[5;15r\033[5;1H\033M"
  sleep 0.5
done


# Move lines up
for i in {1..6}; do
  echo -en "\033[5;15r\033[15;1H\033D"
  sleep 0.5
done

echo -en "\033[30;1H"
