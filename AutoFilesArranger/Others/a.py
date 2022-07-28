import os

files = os.listdir()

folders = [folder for folder in files if not os.path.isfile(folder)]

for i in range(len(folders)):
    if len(os.listdir(folders[i])) == 0:
        print("0")
    else:
        print(len(os.listdir(folders[i])))