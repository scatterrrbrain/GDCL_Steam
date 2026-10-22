# import sys
import datetime
import os
from pathlib import Path

# Scuffed implementation:
# Clone/unzip repo into your Grim Dawn steam installation folder
# ie. ~/.local/share/Steam/steamapps/common/Grim\ Dawn/GDCL_Steam
# TODO: arbitary install location

# Create a new non-steam game in
# ~/.local/share/Steam/userdata/<USER_ID>/config/shortcuts.vdf
# using the vdf module. This is required by some gaming related packages,
# so probably fine tohave it as a dependency.
# TODO: Handle multiple USER_IDs under userdata


# TODO CHANGE TEST NAMES
script_path = Path.cwd()
file_path = Path("./shortcuts.vdf").resolve()
data_path = Path("/home/vilppu/.local/share/Steam/userdata/").resolve()

# print(script_path.resolve())

# subdirs vs listdir
subdirs = [d for d in script_path.iterdir() if d.is_dir()]
for d in subdirs:
    print(d)
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

    USER_ID = users[user_index]
elif len(users) == 1:
    USER_ID = users[0]
elif len(users) == 0:
    print(
        "No users found :(.\
        Check that you have the correct directory setup!"
    )

# Backup previous shortcuts.vdf
backup_dir = script_path / "backup/"
# print(backup_path.resolve())
if not (backup_dir.exists() and backup_dir.is_dir()):
    os.mkdir(backup_dir)

# Generate backup with a timestamp of last change under script_path/backup.
backup_ts = file_path.stat().st_mtime
ts_stem = f"{file_path.stem}_{datetime.datetime.fromtimestamp(backup_ts):%d-%m-%Y-%H-%M-%S}.vdf"
backup_path = (backup_dir / file_path.stem).with_stem(ts_stem)
# print(backup_path)
if not backup_path.exists():
    file_path.copy(backup_path)


# Actually do the stuff now
file = open(file_path, "rb")
#
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
