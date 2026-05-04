import os  # for file and directory operations
import shutil  # for copying files
import random  # for shuffling data

SEED = 42  # ensures reproducible random splits
TRAIN_RATIO = 0.8  # 80% of data for training
VAL_RATIO = 0.1  # 10% for validation
TEST_RATIO = 0.1  # 10% for testing

SOURCE_DIR = r"D:\THESIS_ARGH\source"  # folder containing original dataset
OUTPUT_DIR = r"D:\THESIS_ARGH\dataset"  # folder where split dataset will be saved

SPLITS = ["train", "val", "test"]  # dataset split names
IGNORED_TXT = {"classes.txt", "notes.txt"}  # text files to ignore

def create_output_dirs():
    # create output folders for images and labels in each split
    for split in SPLITS:
        os.makedirs(os.path.join(OUTPUT_DIR, "images", split), exist_ok=True)
        os.makedirs(os.path.join(OUTPUT_DIR, "labels", split), exist_ok=True)

def get_valid_pairs(class_folder_path):
    pairs = []
    files = os.listdir(class_folder_path)  # list all files in class folder

    # map image filenames by name (without extension)
    images = {os.path.splitext(f)[0]: f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))}
    # map label filenames (excluding ignored txt files)
    labels = {os.path.splitext(f)[0]: f for f in files if f.lower().endswith(".txt") and f not in IGNORED_TXT}

    # match images with corresponding labels
    for stem in images:
        if stem in labels:
            pairs.append((images[stem], labels[stem]))  # valid pair
        else:
            raise FileNotFoundError(f"Missing label for image: {images[stem]} in {class_folder_path}")

    # check for labels without matching images
    for stem in labels:
        if stem not in images:
            raise FileNotFoundError(f"Missing image for label: {labels[stem]} in {class_folder_path}")

    return pairs  # return valid image-label pairs

def split_pairs(pairs):
    random.seed(SEED)  # fix randomness for reproducibility
    shuffled = pairs[:]  # copy list
    random.shuffle(shuffled)  # shuffle pairs

    total = len(shuffled)
    train_end = int(total * TRAIN_RATIO)  # index where train split ends
    val_end = train_end + int(total * VAL_RATIO)  # index where val split ends

    # return dictionary of splits
    return {
        "train": shuffled[:train_end],
        "val": shuffled[train_end:val_end],
        "test": shuffled[val_end:]
    }

def copy_files(pairs, split, class_folder_path):
    # copy image and label files to corresponding split folders
    for img_file, lbl_file in pairs:
        src_img = os.path.join(class_folder_path, img_file)  # source image path
        src_lbl = os.path.join(class_folder_path, lbl_file)  # source label path

        dst_img = os.path.join(OUTPUT_DIR, "images", split, img_file)  # destination image path
        dst_lbl = os.path.join(OUTPUT_DIR, "labels", split, lbl_file)  # destination label path

        shutil.copy2(src_img, dst_img)  # copy image
        shutil.copy2(src_lbl, dst_lbl)  # copy label

def main():
    # check if source directory exists
    if not os.path.isdir(SOURCE_DIR):
        raise NotADirectoryError(f"Source directory '{SOURCE_DIR}' not found.")

    create_output_dirs()  # create output folder structure

    # get all class subfolders inside source directory
    class_folders = [
        d for d in os.listdir(SOURCE_DIR)
        if os.path.isdir(os.path.join(SOURCE_DIR, d))
    ]

    # ensure there are class folders
    if not class_folders:
        raise ValueError(f"No class subfolders found in '{SOURCE_DIR}'.")

    total_counts = {"train": 0, "val": 0, "test": 0}  # track total files per split

    # process each class folder
    for class_name in sorted(class_folders):
        class_path = os.path.join(SOURCE_DIR, class_name)
        print(f"Processing class: {class_name}")

        pairs = get_valid_pairs(class_path)  # get valid image-label pairs
        if not pairs:
            print(f"  No valid image-label pairs found, skipping.")
            continue

        split_map = split_pairs(pairs)  # split pairs into train/val/test

        # copy files for each split
        for split, split_pairs_list in split_map.items():
            copy_files(split_pairs_list, split, class_path)
            total_counts[split] += len(split_pairs_list)  # update count
            print(f"  {split}: {len(split_pairs_list)} pairs")

    # print summary
    print("\nDone!")
    print(f"  Train : {total_counts['train']}")
    print(f"  Val   : {total_counts['val']}")
    print(f"  Test  : {total_counts['test']}")
    print(f"  Total : {sum(total_counts.values())}")

# run main function
if __name__ == "__main__":
    main()
