# This checks if all txt files have data inside of them else it would show as empty
# it includes the checking of the classes.txt file which adds +1 to the count
import os

folder = r"D:\THESIS_ARGH\20 CLASSES 100 IMAGES\source - Copy\glassescases"

empty = []
annotated = []

for f in os.listdir(folder):
    if not f.endswith(".txt"):
        continue

    path = os.path.join(folder, f)

    if os.path.getsize(path) == 0:
        empty.append(f)
    else:
        annotated.append(f)

print(f"ANNOTATED: {len(annotated)}")
print(f"EMPTY:     {len(empty)}")

if empty:
    print("\nEMPTY FILES:")
    for f in empty:
        print("  -", f)

print("\nDONE")