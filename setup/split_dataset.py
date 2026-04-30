import os
import shutil
import random

SEED = 42
TRAIN_RATIO = 0.8
VAL_RATIO = 0.1
TEST_RATIO = 0.1

SOURCE_DIR = r"D:\THESIS_ARGH\source"
OUTPUT_DIR = r"D:\THESIS_ARGH\dataset"

SPLITS = ["train", "val", "test"]
IGNORED_TXT = {"classes.txt", "notes.txt"}


def create_output_dirs():
    for split in SPLITS:
        os.makedirs(os.path.join(OUTPUT_DIR, "images", split), exist_ok=True)
        os.makedirs(os.path.join(OUTPUT_DIR, "labels", split), exist_ok=True)


def get_valid_pairs(class_folder_path):
    pairs = []
    files = os.listdir(class_folder_path)
    images = {os.path.splitext(f)[0]: f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))}
    labels = {os.path.splitext(f)[0]: f for f in files if f.lower().endswith(".txt") and f not in IGNORED_TXT}

    for stem in images:
        if stem in labels:
            pairs.append((images[stem], labels[stem]))
        else:
            raise FileNotFoundError(f"Missing label for image: {images[stem]} in {class_folder_path}")

    for stem in labels:
        if stem not in images:
            raise FileNotFoundError(f"Missing image for label: {labels[stem]} in {class_folder_path}")

    return pairs


def split_pairs(pairs):
    random.seed(SEED)
    shuffled = pairs[:]
    random.shuffle(shuffled)

    total = len(shuffled)
    train_end = int(total * TRAIN_RATIO)
    val_end = train_end + int(total * VAL_RATIO)

    return {
        "train": shuffled[:train_end],
        "val": shuffled[train_end:val_end],
        "test": shuffled[val_end:]
    }


def copy_files(pairs, split, class_folder_path):
    for img_file, lbl_file in pairs:
        src_img = os.path.join(class_folder_path, img_file)
        src_lbl = os.path.join(class_folder_path, lbl_file)

        dst_img = os.path.join(OUTPUT_DIR, "images", split, img_file)
        dst_lbl = os.path.join(OUTPUT_DIR, "labels", split, lbl_file)

        shutil.copy2(src_img, dst_img)
        shutil.copy2(src_lbl, dst_lbl)


def main():
    if not os.path.isdir(SOURCE_DIR):
        raise NotADirectoryError(f"Source directory '{SOURCE_DIR}' not found.")

    create_output_dirs()

    class_folders = [
        d for d in os.listdir(SOURCE_DIR)
        if os.path.isdir(os.path.join(SOURCE_DIR, d))
    ]

    if not class_folders:
        raise ValueError(f"No class subfolders found in '{SOURCE_DIR}'.")

    total_counts = {"train": 0, "val": 0, "test": 0}

    for class_name in sorted(class_folders):
        class_path = os.path.join(SOURCE_DIR, class_name)
        print(f"Processing class: {class_name}")

        pairs = get_valid_pairs(class_path)
        if not pairs:
            print(f"  No valid image-label pairs found, skipping.")
            continue

        split_map = split_pairs(pairs)

        for split, split_pairs_list in split_map.items():
            copy_files(split_pairs_list, split, class_path)
            total_counts[split] += len(split_pairs_list)
            print(f"  {split}: {len(split_pairs_list)} pairs")

    print("\nDone!")
    print(f"  Train : {total_counts['train']}")
    print(f"  Val   : {total_counts['val']}")
    print(f"  Test  : {total_counts['test']}")
    print(f"  Total : {sum(total_counts.values())}")


if __name__ == "__main__":
    main()
