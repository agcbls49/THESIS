import os

folder = r"D:\THESIS_ARGH\TO SORT ANNOTATE\comb-ORIGINAL-IMG-ONLY\comb"

# The renamed file will start at 001
counter = 1
files = sorted([f for f in os.listdir(folder) if f.upper().startswith("IMG")])

for filename in files:
    ext = os.path.splitext(filename)[1].lower()
    # Change name based on image
    new_name = f"comb_img_{counter:03d}{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print(f"{filename} -> {new_name}")
    counter += 1

print("Done!")