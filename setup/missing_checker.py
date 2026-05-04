# Code for checking if there is missing jpg
import pathlib

root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\waterbottles")

missing_labels = []

# Check if the images also have the same corresponding txt file with the same base name (ex. img_001.txt for img_001.jpg)
for img in list(root_dir.glob("*.jpg")) + list(root_dir.glob("*.jpeg")) + list(root_dir.glob("*.png")):
    txt_file = img.with_suffix(".txt")

    if not txt_file.exists():
        missing_labels.append(img.name)

print("Missing Labels: ")
for name in missing_labels:
    print(name)

print(f"\nTotal missing: {len(missing_labels)}")
