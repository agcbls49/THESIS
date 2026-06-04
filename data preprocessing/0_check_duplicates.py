# Code for checking if there are duplicate images by checking the image hashes
import pathlib
import hashlib
from collections import defaultdict

root_dir = pathlib.Path(r"D:\THESIS_ARGH\300 IMAGES 20 CLASSES\waterbottles")

hash_map = defaultdict(list)

for img_path in root_dir.rglob("*"):
    if img_path.suffix.lower() in {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".tif", ".webp"}:
        hasher = hashlib.md5()
        with open(img_path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        hash_map[hasher.hexdigest()].append(img_path)

duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}

if not duplicates:
    print("No duplicates found.")
else:
    for paths in duplicates.values():
        print("\nDuplicate group:")
        for p in paths:
            print(f"  {p}")