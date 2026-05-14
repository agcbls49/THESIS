# This mass renames the images inside the folder
import os

folder = r"D:\THESIS_ARGH\TO SORT ANNOTATE\body spray-ORIGINAL-IMG-ONLY\body spray"

# The renamed file will start at 001
counter = 1
files = sorted([f for f in os.listdir(folder) if f.upper().startswith("IMG")])

NAME = "body spray"

for filename in files:
    ext = os.path.splitext(filename)[1].lower()
    # Change name based on image
    new_name = f"{NAME}_img_{counter:03d}{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print(f"{filename} -> {new_name}")
    counter += 1

print("Done!")