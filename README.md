pshot
=====
<img src="data_pshot/pshot_preview.png" alt="" /><br/>
Screenshot Utility written in python

If "Point Active Window" is selected, you got the choice to include the window decorations or not, also once "take new snapshot" is selected your mouse will become a "plus" sign where you will have to LEFT click the desired window. Once clicked the program will take a snapshot of that window and will display it.

## Archlinux support
Archlinux users can install the program directly from AUR, without the need to download it from here.

    yaourt -S pshot-git

## Requirements


* imlib2 (for taking screenshot of the entire screen)
* xorg-xwd (for taking screenshot of the active window)
* imagemagick (for converting the images and for the custom width and height)
* python2
* python2-gobject
* webkitgtk
* pywebkitgtk