import os

# This contains code for converting annotated files to contain the new class list id.
# For example the dataset before was 20 classes and was later reduced to specifically 10 objects.
# Since 300 images per object class were already annotated using the previous class list id's,
# this file is used so that reannotation is not needed or rechecking of the correct 
# class annotations are much easier.

# For example, the previous phone class in the 20 object classes dataset was class id 6.
# With the new class list of 10 objects, this code converts every instance of the previous 
# 6 in the YOLO annotation files into 7. 

# NOTE that this file has to be modified accordingly and the class id's still have to manually be 
# checked to ensure correctness. This file also removes every other instance of the previous class id
# and modifies the existing class id of the objects that are in the new and specific 10 objects class list.

folder = r"D:\A_FINALE\source\ANNOTATED PHONES"

print("Program starting...")

ID_MAPPING = {
    4: 4,    # headphone → headset
    6: 7,    # phone → phone
    12: 2,   # charger → charger
    13: 3,   # comb → comb
    16: 6    # medicine → medicine
}


# Old classes that were removed from the dataset.
# Any annotation using one of these IDs will be deleted.
DELETED_IDS = {
    0, 1, 2, 3, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19
}

# os.listdir() returns the names of files and folders directly
# inside the specified folder. It does not open or modify them.
for filename in os.listdir(folder):

    # Ignore images and ignore classes.txt. This prevents the script from trying
    # to process JPG/PNG files.
    if not filename.endswith(".txt") or filename == "classes.txt":
        continue


    file_path = os.path.join(folder, filename)

    # open(..., "r") opens the file in read mode.
    # readlines() reads every line and returns them as a list,
    # allowing the script to examine each YOLO annotation separately.
    with open(file_path, "r") as file:
        lines = file.readlines()


    new_lines = []


    for line in lines:

        # strip() removes whitespace from the beginning and end
        # of the string, including the newline character (\n).
        # Example:
        # "12 0.43 0.36 0.19 0.06\n"
        # becomes:
        # "12 0.43 0.36 0.19 0.06"
        line = line.strip()


        # Ignore completely empty lines.
        if not line:
            continue


        # split() separates the annotation into individual values
        # wherever whitespace occurs.
        # Example:
        # "12 0.43 0.36 0.19 0.06"
        # becomes:
        # ["12", "0.43", "0.36", "0.19", "0.06"]
        parts = line.split()


        # A normal YOLO bounding-box annotation has at least five
        # values: class ID, x, y, width, and height.
        if len(parts) < 5:
            print(f"WARNING: Invalid annotation in {filename}: {line}")
            continue


        # int() converts the first value from text into an integer
        # so it can be compared with the numeric IDs in the mappings.
        old_id = int(parts[0])


        # If the old class still exists in the new dataset,
        # replace its old ID with the correct new ID.
        if old_id in ID_MAPPING:

            new_id = ID_MAPPING[old_id]

            parts[0] = str(new_id)

            # join() puts the annotation values back together with
            # spaces between them, recreating a valid YOLO line.
            new_lines.append(" ".join(parts) + "\n")


        # If the old class was deleted, do not add its annotation
        # to new_lines. Therefore that entire bounding-box
        # annotation disappears from the resulting file.
        elif old_id in DELETED_IDS:

            print(f"Removed old class {old_id} from {filename}")


        # Anything unexpected is reported instead of being
        # automatically changed or deleted.
        else:

            print(
                f"WARNING: Unknown class ID {old_id} "
                f"in {filename}"
            )


    # open(..., "w") opens the file in write mode.
    # Writing mode replaces the existing contents of the file.
    # The file is rewritten using only the corrected annotations
    # stored in new_lines.
    with open(file_path, "w") as file:
        file.writelines(new_lines)


    print(f"Updated: {filename}")


print("Done!")