import os
import shutil

os.chdir(os.path.dirname(__file__))


def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:]

directories = {
    "Videos": ["mp4","wav","obb"],
    "Audio": ["mp3"],
    "Documents": ["doc","txt","pdf"],
    "Scripts": ["html","py"],
    "Images": ["png","jpg","jpeg"]
}

exceptions = ["app.py"]

for directory in directories:
    print(directory)
    os.makedirs(directory,exist_ok=True)


files = os.listdir()

for file in files:
    if file in exceptions:
        continue
    elif os.path.isfile(file):
        extension = get_file_extension(file)
        for folder,extension_list in directories.items():
            if extension in extension_list:
                shutil.move(file,folder)
