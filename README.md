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
*** Important ***
- Make sure your Steam client is fully closed before running the script!

- Clone/unzip the repo into your Grim Dawn installation folder ie. "~/.local/share/Steam/steamapps/common/Grim\ Dawn/"
- Navigate to the GDCL_Steam directory and run the python script "bootstrap.py":
``` 
$ cd ./GDCL_Steam
$ python bootstrap.py

```
- This should automatically open Steam and launch the GDCL launcher after GDCL has been added to Steam.
This is done to make Steam initialize the Proton prefix for the GDCL launcher.

- NOTE: Automated Steam restart + game launch is done using [Steam Browser Protocol](https://developer.valvesoftware.com/wiki/Steam_browser_protocol). On my system "this just works", but you might get a browser popup saying to "Open a link in steam". If the automated start does not work,
you can just launch the game manually from your Steam library.

## Setting Migration (optional)
- If you want to migrate your base GD settings over to GDCL, you need to:
```
-> Launch the GDCL launcher from steam at least once (the automated launch works here).
-> LOGIN to download the latest launcher updates and click play.
-> Wait until Grim Dawn loads *ALL THE WAY UP TO THE GRIM DAWN MAIN MENU*.
```
- After this, you can exit the game and run the "migrate_settings.py" script from the GDCL_Steam directory:
```
$ python migrate_settings.py
```

## Please report bugs etc! :)
- discord: scatterrr_
