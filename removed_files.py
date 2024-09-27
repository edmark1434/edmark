import os
import shutil

path = r"C:\Users\edmark\Downloads\New folder\Images".replace("\\", "/")
image_to_removed = ["original", "cat", "garden"]


def removed_all_files(path):
    if os.path.exists(path):
        for filename in os.listdir(path):
            pathfile = os.path.join(path, filename)
            image_name = os.path.splitext(filename)[0]
            if os.path.isfile(pathfile):
                for i in image_to_removed:
                    if image_name in i:
                        os.remove(pathfile)
                        print(f"Successfully Removed {filename}")
    else:
        print(f"{path} does not exist")


print(removed_all_files(path))
