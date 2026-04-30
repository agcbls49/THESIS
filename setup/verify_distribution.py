# check the images and labels that are distributed in the dataset folder
import os

base_dir = r"D:\THESIS_ARGH\dataset"

for split in ["train", "val", "test"]:
    print("\n", split)

    classes_found = set()

    path = os.path.join(base_dir, "images", split)

    for file in os.listdir(path):
        if file.endswith(".jpg"):
            class_name = file.split("_")[0]
            classes_found.add(class_name)

    print("Classes in", split, ":", classes_found)