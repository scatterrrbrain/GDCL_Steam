# Grim Dawn Community League Steam bootstrapper for Linux

The goal of this script is to automate adding the Grim Dawn Community League exe as a non-steam game, while also providing a nice looking default steam page and icons.
Launching GDCL using Steam is (imo) the easiest way to make use of Steam's Proton compatability options on Linux and provides a nice, customizeable UI.

<img width="1271" height="559" alt="GDCL_Steam_preview" src="https://github.com/user-attachments/assets/e8e5c5af-e809-4cfd-87de-fc97754057b1" />

![Steam preview](GDCL_preview_large.png?raw=true "Steam preview")

# NOTE:
- This script is still work in progress, and is such likely to break and/or do weird stuff. 
- 100% all natural spaghetti, no LLMS used here.

If you're using other non-steam games in Steam, you should backup your 'shortcuts.vdf' file,located in 
```
'~/.local/share/Steam/userdata/<USER_ID>/config/'
```
just in case! You should also consider backing up your proton prefixes in 
```
~/.local/share/Steam/steamapps/compatdata/
```
(probably not a big deal but just in case)

## Usage:
*!! Important !!*
- Make sure your Steam client is fully closed!!


- Clone/unzip the repo into your Grim Dawn installation folder ie. "~/.local/share/Steam/steamapps/common/Grim\ Dawn/"
- $ cd ./GDCL_Steam
- $ python bootstrap.py

-> Should automatically open Steam and launch the GDCL-launcher. This is to initialize the Proton prefix path. 
- If you want to migrate your base GD settings, you need to launch the game, all the way up to the Grim Dawn main menu.

- Either works or doesn't

## Please report bugs etc! :)
- discord: scatterrr_
