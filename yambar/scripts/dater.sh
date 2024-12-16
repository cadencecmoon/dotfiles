#!/bin/sh


while true; do
number=$(date +'%d')

case $number in
    1*)extension=th;;
    *1)extension=st;;
    *2)extension=nd;;
    *3)extension=rd;;
    *)extension=th;;
esac

date=$(date +"%A $(printf ${number##0}$extension) %B %Y -")

echo "date|string|$date"
echo ""

hour=$(date +'%H')
minute=$(date +'%M')

second=$(expr $hour \* 3600 + $minute \* 60)

sleep "$second"
done
