import os
import shutil

directory = "C:/Users/edmark/Downloads"
categories = {
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [
        ".py",
        ".c",
        ".cpp",
        ".js",
        ".html",
        ".css",
        ".java",
        ".php",
        ".rb",
        ".go",
        ".rs",
    ],
    "Executables": [".exe", ".bat", ".sh"],
    "Fonts": [".ttf", ".otf"],
    "Others": [".iso", ".dll", ".log", ".ini", ".cfg"],
}


def organized_files(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            pathfile = os.path.join(directory, filename)
            if os.path.isdir(pathfile):
                continue

            file_extention = os.path.splitext(filename)[1].lower()
            moved = False

            for categ_name, extention in categories.items():
                if file_extention in extention:
                    category_dir = os.path.join(directory, categ_name)
                    if not os.path.exists(category_dir):
                        os.makedirs(category_dir)

                    shutil.move(pathfile, os.path.join(category_dir, filename))
                    print(f"{filename} is Successfully Moved in {categ_name}")
                    moved = True
                    break

            if not moved:
                other_dir = os.path.join(directory, "Other")
                if not os.path.exists(other_dir):
                    os.makedirs(other_dir)
                shutil.move(pathfile, os.path.join(other_dir, filename))
                print(f"{filename} is Successfully Moved in Other")
    else:
        print(f"{directory} does not exist")


print(organized_files(directory))
