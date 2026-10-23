# import sys
import datetime
import os
import sys
import webbrowser
from pathlib import Path

import vdf

# TODO: Turn this into a "properly written" script

# Scuffed implementation:
# Clone/unzip repo into your Grim Dawn steam installation folder
# ie. ~/.local/share/Steam/steamapps/common/Grim\ Dawn/GDCL_Steam
# TODO: arbitary install location

# Create a new non-steam game in
# ~/.local/share/Steam/userdata/<USER_ID>/config/shortcuts.vdf
# using the vdf module. This is required by some gaming related packages,
# so probably fine tohave it as a dependency.

GAME_NAME = "Grim Dawn Community League"
EXE_NAME = "GDCommunityLauncher.exe"

# ----------------------
# INIT
# ----------------------

script_path = Path.cwd()

cfg_file = script_path / "config.json"

# Maybe use relative paths like
# data_path = Path("~/.local/share/Steam/userdata/").resolve()
# TODO make this not stupid xdd
data_path = script_path.parent.parent.parent.parent / "userdata"

# subdirs vs listdir
# subdirs = [d for d in script_path.iterdir() if d.is_dir()]
# for d in subdirs:
#     print(d)

# listdir also gives files but this does not matter here
users = os.listdir(data_path)
# print(users)

if len(users) > 1:
    print(
        "Multiple users detected. Check your user id by going to Steam's\
          'Add Friend' page!"
    )
    print(
        "---------------------------------------------------------------\
        -------------------"
    )
    for i, u in enumerate(users):
        print(i, u)

    user_input = input("Select your userid: ")
    user_index = int(user_input)

    user_id = users[user_index]
elif len(users) == 1:
    user_id = users[0]
elif len(users) == 0:
    print(
        "No users found :(.\
        Check that you have the correct directory setup!"
    )

# mb rename to shortcut_path or smth
file_path = (data_path / user_id / "config").resolve()
shortcuts_path = (file_path / "shortcuts.vdf").resolve()


# ----------------------
# BACKUP
# ----------------------
# Backup previous shortcuts.vdf
if shortcuts_path.exists():
    backup_dir = script_path / "backup/"
    if not (backup_dir.exists() and backup_dir.is_dir()):
        os.mkdir(backup_dir)

    # Generate backup with a timestamp of last change under script_path/backup.
    backup_ts = shortcuts_path.stat().st_mtime
    ts_stem = f"{shortcuts_path.stem}_{datetime.datetime.fromtimestamp(backup_ts):%d-%m-%Y-%H-%M-%S}.vdf"
    backup_path = (backup_dir / shortcuts_path.stem).with_stem(ts_stem)
    if not backup_path.exists():
        shortcuts_path.copy(backup_path)


# ----------------------
# SET SHORTCUTS.VDF
# ----------------------

# TODO: Make a check here st. only add shortcut if "Grim Dawn Community Launcher" doesn't exist

game_path = (script_path.parent).resolve()
exe_path = (game_path / EXE_NAME).resolve()

# Actually do the stuff now
# Context mngr
if shortcuts_path.exists():
    print("shortcuts.vdf found!")
    with open(shortcuts_path, "rb") as f:
        # Check mapper here:
        # Default dict vs VDFDict
        data = vdf.binary_load(f)
else:
    print("shortcuts.vdf not found -> new file")
    data = {'shortcuts': {}}


shortcuts = data['shortcuts'].values()
# print(shortcuts)
# print("----------------------")

# Check for existing GDCL shortcuts
for s in shortcuts:
    for v in s.values():
        if v == GAME_NAME:
            print("Existing GDCL shortcut found. Exiting program.")
            sys.exit()


# Set random appid for now just in case, to make sure format etc. stays correct.
# When you first launch the game (using proton, default should be Proton Stable or Experimental)
# Steam creates a proton prefix environment (or whatever) under
# ~/.local/share/Steam/steamapps/compatdata/<NEW_ID> (also stores game settings etc.)
# where NEW_ID is a newly generated appid. The new appid is then used to get the app icons from
# ~/.local/share/Steam/userdata/<USER_ID>/config/grid .
# Afaik this is just random for non-steam games,
# so we'll just let Steam generate it and use the new one.

# appid here is an int 32 (or something) ie ~ -300000000 < int < 300000000
# -> unsigned conversion of int = appid number used for grid and proton prefix
# ie.  -190695072 -> 2388016574
# NOTE Try using this as a magic number for now, fix later if needed

# Google says the shortcut name ie. what's used to launch steam://runappid/ and the shortcut
# number that's the unsigned int such as 2388016574, used for icons and prefix etc.
# are related by the formula/function:
# https://github.com/scottrice/Ice/blob/7130b54c8d2fa7d0e2c0994ca1f2aa3fb2a27ba9/ice/steam_grid.py#L105

# Looks like this works out exactly for our magic number 2388016574 -> 10256453087669518336
# which is the correct shortcut "name". This can be verified experimentally or by checking
# steamdir/userdata/user_id/760/screnshots.vdf (for some reason it shows up here idk lol)
magic_appid = -1906950722
# bitwise & conversion into uint32
magic_id = magic_appid & 0xFFFFFFFF
# print(magic_appid)
# print(magic_id)

# magic shortcut id used to launch the game using
# steam://rungameid/magic_shortcut_id
# is obtained using the bitshift formula:
magic_shortcut_id = (magic_id << 32) | 0x02000000
# print(magic_shortcut_id)

# ----------------------
# IMPORT ICONS
# ----------------------

# TODO:
# Need to run game with Proton to create the prefix path + new id
# Running the launcher creates the path but GD needs to be launched
# from the launcher to create the settings folder.

# NOTE: Could try creating a proton path and see if you can
# attach a appid to it without chaning the id
# NOTE: Looks like a hacky way to *maybe* solve this is to
# use a steam generated / "valid" appid that already has a prefix


# Copy ./art/ into the icon grid folder
art_dir = script_path / "art"
grid_path = file_path / "grid"
if not (grid_path.exists() and grid_path.is_dir()):
    os.mkdir(grid_path)

# icon_path = script_path / "art/S8_logo.png"
icon_path = grid_path / f"{magic_id}_icon.png"

# Check that app_id in shortcuts.vdf matches the prefix of *_icon.pdf

# Grid icons have the following naming convention:
# Game background = {app_id}_hero.png
Path(art_dir / "S8_bg.png").copy(grid_path / f"{magic_id}_hero.png")

# Vertical cover = {magic_id}p.png
Path(art_dir / "S8_cover.png").copy(grid_path / f"{magic_id}p.png")

# Horizontal/wide cover = {magic_id}.png
Path(art_dir / "S8_cover_wide.png").copy(grid_path / f"{magic_id}.png")

# Logo = {magic_id}_logo.png
Path(art_dir / "S8_logo_no_bg.png").copy(grid_path / f"{magic_id}_logo.png")

# Logo scaling/orientation config
Path(art_dir / "logo.json").copy(grid_path / f"{magic_id}.json")


# Actually set vdf now
# TODO: Fix icon not working (the small side panel icon)
# TODO: Launch options from config.json

# Need triple/double quotes or whatever '""' for fstrings
GDCL_shortcut = {
    "appid": magic_appid,
    "AppName": GAME_NAME,
    "Exe": f'"{exe_path}"',
    "StartDir": f'"{game_path}"',
    "icon": f'"{icon_path}"',
    "ShortcutPath": "",
    "LaunchOptions": "",
    "IsHidden": 0,
    "AllowDesktopConfig": 1,
    "AllowOverlay": 1,
    "OpenVR": 0,
    "Devkit": 0,
    "DevkitGameID": "",
    "DevkitOverrideAppID": "",
    "LastPlayTime": 0,
    "FlatpakAppID": "",
    "sortas": "",
    "tags": {},
}

# Add GDCL_shortcut to shortcuts

# Effectively index last+1 of shortcuts
# new_index = len(data['shortcuts'])
data['shortcuts'][str(len(data['shortcuts']))] = GDCL_shortcut

# print("---------------")
#
# for k, v in data['shortcuts'].items():
#     print(k, v)


# Make sure to create the proton prefix directory
proton_path = script_path.parent.parent.parent / "compatdata" / f"{magic_id}"
print(proton_path)

if not (proton_path.exists() & proton_path.is_dir()):
    os.mkdir(proton_path)

# Binary dump back into shortcuts.vdf:
# Write binary as task manager
with open(shortcuts_path, "wb") as f:
    vdf.binary_dump(data, f)


GD_url = f"steam://rungameid/{magic_shortcut_id}"
webbrowser.open(GD_url)
