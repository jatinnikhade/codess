import os
import sys
import pathlib
import zipfile

dirName = input("enter directory nme that you want to backup : ")

if not os.path.isdir(dirName) :
    print("directory",dirName, "doesn't exist")
    sys.exit(0)

curDirectory = pathlib.Path(dirName)

with zipfile.ZipFile("MYFIL.zip", mode="w") as archive:
    for file_path in curDirectory.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(curDirectory))

if os.path.isfile("MYFIL.zip"):
    print("Archive", "MYFIL.zip", "created successfully")

else:
    print("error in creating zip file")
