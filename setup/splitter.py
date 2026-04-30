# make sure to create two separate folders (one for splitting and one for actual dataset creation)
import splitfolders
import os
import shutil

# splits the folders first
splitfolders.ratio(
    r"D:\THESIS_ARGH\source",
    output=r"D:\THESIS_ARGH\split",
    seed=42,
    # 80, 10, 10 split
    ratio=(0.8, 0.1, 0.1)
)

# applies proper formatting for YOLO (RUN ONCE ONLY SO IT ACTUALLY WORKS BECAUSE THIS CODE DUPLICATES WHEN RUN TWICE)
import os
import shutil

input_dir = r"D:\THESIS_ARGH\split"
output_dir = r"D:\THESIS_ARGH\dataset"

print("Running")

for split in ["train", "val", "test"]:
    image_out = os.path.join(output_dir, "images", split)
    label_out = os.path.join(output_dir, "labels", split)

    os.makedirs(image_out, exist_ok=True)
    os.makedirs(label_out, exist_ok=True)
    split_path = os.path.join(input_dir, split)

    for class_folder in os.listdir(split_path):
        class_path = os.path.join(split_path, class_folder)

        if not os.path.isdir(class_path):
            continue

        for file in os.listdir(class_path):
            src = os.path.join(class_path, file)
            file_lower = file.lower()

            if file_lower.endswith((".jpg", ".jpeg", ".png")):
                dst = os.path.join(image_out, file)

                if not os.path.exists(dst):
                    shutil.copy(src, dst)

            elif file_lower.endswith(".txt"):
                dst = os.path.join(label_out, file)

                if not os.path.exists(dst):
                    shutil.copy(src, dst)

print("Done")