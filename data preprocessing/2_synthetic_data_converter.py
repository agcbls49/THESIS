# Code for synthetic data conversion as the synthetic data used may have 
# incomptible file extensions or formatting that does not work in LabelImg
import cv2
import os

folder = r"D:\THESIS_ARGH\20 CLASSES 100 IMAGES\source - Copy\flashlights"

# Rename all non-txt files to .jpg
for f in os.listdir(folder):
    path = os.path.join(folder, f)

    if not os.path.isfile(path):
        continue

    name, ext = os.path.splitext(f)

    if ext.lower() == ".txt":
        continue

    if ext.lower() != ".jpg":
        new_path = os.path.join(folder, name + ".jpg")
        os.rename(path, new_path)
        print("RENAMED:", f, "->", name + ".jpg")

# Convert renamed .jpg files into actual JPG files via OpenCV
for f in os.listdir(folder):
    path = os.path.join(folder, f)

    if not os.path.isfile(path):
        continue

    name, ext = os.path.splitext(f)

    if ext.lower() not in [".jpg", ".jpeg"]:
        continue

    img = cv2.imread(path)

    # skip unreadable files
    if img is None:
        print("SKIP:", f)
        continue

    # overwrite the same file and re-encode as clean JPEG file
    cv2.imwrite(path, img)

    print("FIXED:", f)

print("DONE")