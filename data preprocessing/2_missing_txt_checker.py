# Code for checking if there is a missing jpg or annotated txt file
import pathlib

root_dir = pathlib.Path(r"D:\THESIS_ARGH\20 CLASSES 100 IMAGES\source - Copy\combs")

missing_labels = []

for img in list(root_dir.glob("*.jpg")) + list(root_dir.glob("*.jpeg")) + list(root_dir.glob("*.png")):
    txt_file = img.with_suffix(".txt")

    if not txt_file.exists():
        missing_labels.append(img.name)

print("Missing Labels: ")
for name in missing_labels:
    print(name)

print(f"\nTotal missing: {len(missing_labels)}")