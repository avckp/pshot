#!/bin/sh
# https://wiki.archlinux.org/index.php/Taking_a_Screenshot#Screenshot_of_the_active.2Ffocused_window
# convert: clGetPlatformIDs failed. - https://bbs.archlinux.org/viewtopic.php?id=172274
activeWinLine=$(xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)")
activeWinId=${activeWinLine:40}
import -window "$activeWinId" /tmp/Screenshot1.png 
convert /tmp/Screenshot1.png -resize 425x240 /tmp/Screenshot2.png