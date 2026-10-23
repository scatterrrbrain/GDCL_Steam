# Grim Dawn Community League Steam bootstrapper for Linux

The goal of this script is to automate adding the Grim Dawn Community League exe as a non-steam game, while also providing a nice looking default steam page and icons.
Launching GDCL using Steam is (imo) the easiest way to make use of Steam's Proton compatability options on Linux and provides a nice, customizeable UI.

TODO: Lutris etc.

# NOTE:
- This script is still work in progress, and is such likely to break and/or do weird stuff. If you're using other non-steam games in Steam, you should backup your 'shortcuts.vdf' file,located in 
```
'~/.local/share/Steam/userdata/<USER_ID>/config/'
```
just in case!

## Usage:
TODO: Check all this

*!! Important !!*
- Make sure your Steam client is fully closed!

- Clone/unzip the repo into your Grim Dawn installation folder ie. "~/.local/share/Steam/steamapps/common/Grim\ Dawn/"
- $ cd ./GDCL_Steam
- $ python bootstrap.py
- Either works or doesn't

## Please report bugs etc! :)
- discord: scatterrr_
