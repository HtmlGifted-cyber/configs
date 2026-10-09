#!/bin/bash
# Shows used/total space of the first mounted external drive (under /media or /mnt).
# Used by mybey. Prints a message if none is mounted.
line=$(df -h --output=used,size,target 2>/dev/null | awk '$3 ~ /^\/(media|mnt)\// {print $1" / "$2" ("$3")"; exit}')
if [ -n "$line" ]; then echo "$line"; else echo "No External Device Is Mounted"; fi
