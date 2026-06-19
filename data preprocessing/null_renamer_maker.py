# This script renames all null images and creates empty text files
import os

folder = r"D:\THESIS_ARGH\300 IMAGES 20 CLASSES\waterbottles"

counter = 1

NAME = "null"

IMAGE_EXTS = {".jpg", ".jpeg", ".png"}

files = sorted([f for f in os.listdir(folder)])

for filename in files:
    ext = os.path.splitext(filename)[1].lower()
    if ext not in IMAGE_EXTS:
        continue

    new_name = f"{NAME}_img_{counter:03d}{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print(f"{filename} -> {new_name}")

    # Create matching empty .txt
    txt_name = f"{NAME}_img_{counter:03d}.txt"
    with open(os.path.join(folder, txt_name), "w") as f:
        pass
    print(f"Created -> {txt_name}")

    counter += 1

print("Done!")