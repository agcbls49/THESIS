# Code for checking if there is missing jpg
import pathlib

# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\backpacks")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\books")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\cups")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\eyeglasses")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\headphones")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\keys")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\phones")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\remotes")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\wallets")
root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\waterbottles")

missing_labels = []

for img in list(root_dir.glob("*.jpg")) + list(root_dir.glob("*.jpeg")) + list(root_dir.glob("*.png")):
    txt_file = img.with_suffix(".txt")

    if not txt_file.exists():
        missing_labels.append(img.name)

print("Missing Labels: ")
for name in missing_labels:
    print(name)

print(f"\nTotal missing: {len(missing_labels)}")


# Show all txt file names 
import pathlib

# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\backpacks")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\books")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\cups")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\eyeglasses")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\headphones")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\keys")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\phones")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\remotes")
# root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\wallets")
root_dir = pathlib.Path(r"D:\THESIS_ARGH\source\waterbottles")


for txt in root_dir.rglob("*.txt"):
    print(txt.name)