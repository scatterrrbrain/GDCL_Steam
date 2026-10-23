import shutil
from pathlib import Path

# Scuffed hardcode for now
# TODO: Change if magic_id breaks
magic_id = 2388016574
# Static game id from Steamdb
GD_id = 219990

GD_path = Path.cwd().parent
# print(GD_path)
proton_path = GD_path.parent.parent / "compatdata"
# print(proton_path)

prefix_settings = "pfx/drive_c/users/steamuser/Documents/My Games/Grim Dawn/"
settings_path_old = proton_path / f"{GD_id}" / prefix_settings / "Settings"
# print(settings_path_old)

settings = ["options.txt", "keybindings.txt"]
settings_path_new = proton_path / f"{magic_id}" / prefix_settings / "Settings"

if not (settings_path_new.exists() and settings_path_new.is_dir()):
    print(
        "GDCL settings dir not found.\n \
        Please launch into the main menu using the GDCL launcher first!"
    )
else:
    for file in settings:
        shutil.copyfile(settings_path_old / file, settings_path_new / file)

    print("Done!")
