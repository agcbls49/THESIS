# **Data Preprocessing**

1. *requirements.txt*

This file contains the pip command needed for installing the **"split-folders"** library. This package is used to split the images into test, valid and train folders allowing it to be used for machine learning.

---

2. *1_img_renamer.py*

This file was used to mass rename the image files. It checks if the image file is prefixed with "IMG" and if so, it renames it.

---

3. *2_missing_checker.py*

This file was used to check if there are any missing labels inside a class folder. It checks all the images in the folder then checks if the files have a corresponding text file. If not, then it returns the missing file names appended with **".txt"**.

---

4. *3_split_dataset.py*

This file was used to split the dataset into 80% train, 10% valid and 10% test. It creates train, valid and test folders inside the output folders or directory. It then shuffles the images inside the source directory then copies it into the train, valid, and test folders inside the output directory. Lastly, it prints a summary of the split.

---

5. *4_verify_distribution.py*

This file checks if all the train, valid, and test folders have all the 20 classes inside after the split.
