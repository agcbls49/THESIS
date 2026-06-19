# **Data Preprocessing**

This contains the explanation of the files that were used for the data preprocessing of the images used as dataset in the project.

---

<br>

## *requirements.txt*

This file contains the pip command needed for installing the **split-folders** and **opencv** library. OpenCV is a computer vision library that was used to convert  the synthetic data image files into **LabelImg** compatible image files. Split-folders was used to split the images into test, valid and train folders allowing it to be used for machine learning. 

---

##  *check_duplicates.py*

This file contains code for comparing the hashes of images to check if there are duplicate images. 

>[!NOTE]
> The **images are still checked manually** to ensure that there are no duplicates. This file is used for the initial checking before manual checking is done.

---

## *img_renamer.py*

This file was used to mass rename the image files. 

---

## *jpg_format_converter.py*

This file was used to convert the supplementary data image files into **"JPG"** image files that are compatible with **LabelImg** allowing it to be annotated for machine learning training. 

---

## *empty_annotated_checker.py*

This file was used to check if the text files inside a folder is empty or not. If it is not empty then that means the file was annotated.

---

## *missing_txt_checker.py*

This file was used to check if there are any missing labels inside a class folder. It checks all the images in the folder then checks if the files have a corresponding text file. If not, then it returns the missing file names appended with **".txt"**.

---

## *null_renamer_maker.py*

This file was used to mass rename all null images and create their corresponding empty text files as YOLO requires null images to have empty text/annotation files.

---

## *split_dataset.py*

This file was used to split the dataset into **80% train, 10% valid and 10% test**. It creates train, valid and test folders inside the output folders or directory. It then shuffles the images inside the source directory then copies it into the train, valid, and test folders inside the output directory. Lastly, it prints a summary of the split.

---

## *verify_distribution.py*

This file checks if all the train, valid, and test folders have all the 20 classes inside after the split.
