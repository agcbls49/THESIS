import os

source_dir = r"D:\THESIS_ARGH\source"

# Get all the directory inside the source directory
for folder_name in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder_name)

    # if not folder then dont touch
    if not os.path.isdir(folder_path):
        continue

    # rename img based on folder with exceptions
    if folder_name == "eyeglasses":
        class_name = "glasses"
    if folder_name == "waterbottles":
        class_name = "water bottle"
    elif folder_name.endswith("s"):
        class_name = folder_name[:-1]
    else:
        class_name = folder_name

    for file in os.listdir(folder_path):
        if not file.startswith("img_"):
            continue

        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, class_name + "_" + file)
        os.rename(old_path, new_path)