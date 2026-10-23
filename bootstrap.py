# import sys
import datetime
import os
from pathlib import Path

import vdf

# Scuffed implementation:
# Clone/unzip repo into your Grim Dawn steam installation folder
# ie. ~/.local/share/Steam/steamapps/common/Grim\ Dawn/GDCL_Steam
# TODO: arbitary install location

# Create a new non-steam game in
# ~/.local/share/Steam/userdata/<USER_ID>/config/shortcuts.vdf
# using the vdf module. This is required by some gaming related packages,
# so probably fine tohave it as a dependency.
# TODO: Handle multiple USER_IDs under userdata

GAME_NAME = "Grim Dawn Community League"
EXE_NAME = "GDCommunityLauncher.exe"

# TODO CHANGE TEST NAMES
script_path = Path.cwd()

# Maybe use relative paths like
# data_path = Path("~/.local/share/Steam/userdata/").resolve()
data_path = script_path.parent.parent.parent.parent / "userdata"
# print(data_path)

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
file_path = data_path / user_id / "config"
shortcuts_path = file_path / "shortcuts.vdf"
# print(file_path)

# Backup previous shortcuts.vdf
backup_dir = script_path / "backup/"
# print(backup_path.resolve())
if not (backup_dir.exists() and backup_dir.is_dir()):
    os.mkdir(backup_dir)

# Generate backup with a timestamp of last change under script_path/backup.
backup_ts = shortcuts_path.stat().st_mtime
ts_stem = f"{shortcuts_path.stem}_{datetime.datetime.fromtimestamp(backup_ts):%d-%m-%Y-%H-%M-%S}.vdf"
backup_path = (backup_dir / shortcuts_path.stem).with_stem(ts_stem)
# print(backup_path)
if not backup_path.exists():
    shortcuts_path.copy(backup_path)


# Check if proper appid generation needed
app_id = 7777777777

# Copy ./art/ into the icon grid folder
art_dir = script_path / "art"
grid_path = file_path / "grid"


# Grid icons have the following naming convention:

# Game background = {app_id}_hero.png
Path(art_dir / "S8_bg.png").copy(grid_path / f"{app_id}_hero.png")

# Vertical cover = {app_id}p.png
Path(art_dir / "S8_cover.png").copy(grid_path / f"{app_id}p.png")

# Horizontal/wide cover = {app_id}.png
Path(art_dir / "S8_cover_wide.png").copy(grid_path / f"{app_id}.png")

# Logo = {appid}_logo.png
Path(art_dir / "S8_logo_no_bg.png").copy(grid_path / f"{app_id}_logo.png")

# Logo scaling/orientation config
Path(art_dir / "logo.json").copy(grid_path / f"{app_id}.json")

game_path = script_path.parent
exe_path = game_path / EXE_NAME

# Actually do the stuff now
# Context mngr
with open(shortcuts_path, "rb") as file:
    data = vdf.binary_load(file, mapper=dict)

# vdf.dump()
# print(shortcuts_path)
# data = vdf.binary_load(open("shortcuts_path", "rb"))
print(data)
# print()


# Check if resolved paths needed
GDCL_shortcut = {
    "appid": app_id,
    "appname": GAME_NAME,
    "exe": f"{exe_path}",
    "StartDir": f"{game_path}",
    "LaunchOptions": "",
    "IsHidden": 0,
    "AllowDesktopConfig": 1,
    "OpenVR": 0,
    "Devkit": 0,
    "DevkitGameID": "",
    "LastPlayTime": 0,
    "tags": {},
}

# dict_input = vdf.binary_load(file)
#
# print(dict_input)
# print(dict_input.keys())
# #print(vdf.dumps(d))
# #input_str = vdf.dumps(dict_input)
# #print(input_str)
#
# output_str_fmt = vdf.dump(dict_input, open('./test.txt',"w"))
# mydic = vdf.parse(open('test.txt'))
# output_bytes = vdf.binary_dumps(input_str)

# output = vdf.binary_dump(input_str, open('./test.vdf', 'wb'))

# vdf.dump(file, open('test.txt', 'w'), pretty=True)
