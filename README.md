# VocaSee
VocaSee is a Voice-Guided Indoor Object Finder Android Application for Visually Impaired Users

## Created By
Amazing Grace O. Cabiles - Dataset Annotations and Machine Learning Model Training <br>
Cyrelle Kristin P. Gapit - Android Application Developer <br>
Francen P. Manalo - QA Tester <br>

## Dataset
A custom dataset was used for this project consisting of images captured under varying lighting conditions and was combined with supplementary images from Kaggle. The dataset was split into **80% train, 10% validation and 10% test** sets. All YOLO models were trained using this dataset with the following default YOLO configurations: images were resized to 640×640, a batch size of 16 was used, and training was conducted for 100 epochs. 

**[The dataset source can be found here](https://drive.google.com/drive/folders/1jwQUXeVuitPZA2yQ5qw2U9-SQvqCeRwC?usp=sharing)**

> [!NOTE]
> **The data listed on the table below is subject to change and was last updated in June 9, 2026.
> Annotation started in April 23, 2026.**

The current total of images in the dataset is 2000 images.

The dataset includes the following:
| Folder Name | Class Number | Class Name | Number of Images |
|-------------|--------------|------------|------------------|
|backpacks    |0             |backpack    |300               |
|books        |1             |book        |300               |
|cups         |2             |cup         |300               |
|eyeglasses   |3             |glasses     |300               |
|headphones   |4             |headphone   |300               |
|keys         |5             |key         |300               |
|phones       |6             |phone       |300               |
|remotes      |7             |remote      |100               |
|wallets      |8             |wallet      |100               |
|waterbottles |9             |water bottle|100               |
|bodysprays   |10            |body spray  |100               |
|cards        |11            |card        |100               |
|chargers     |12            |charger     |100               |
|combs        |13            |comb        |100               |
|flashlights  |14            |flashlight  |300               |
|glassescases |15            |glasses case|100               |
|medicines    |16            |medicine    |100               |
|nailclippers |17            |nail clipper|100               |
|shoes        |18            |shoe        |100               |
|watches      |19            |watch       |300               |

## Supplementary Data Sources
1. [Flashlights from OORT DataHub](https://www.kaggle.com/datasets/oortdatahub/diverse-tools-image-dataset-for-machine-learning)
2. [Watches from Ahed Jneed](https://www.kaggle.com/datasets/ahedjneed/fancy-watche-images)
3. [Cups from Samuel Ayman](https://www.kaggle.com/datasets/samuelayman/cup-dataset)
4. Headphones from the Roboflow Universe Platform specifically made by:
   * [@CVAI Project](https://universe.roboflow.com/headphones-9uy0k/headphones-fwhbt)
   * [@headphones](https://universe.roboflow.com/headphones/headphones-3i2fi/dataset/3)
   * [@headphones-crjvh](https://universe.roboflow.com/headphones-crjvh/headphones-zrumj)

5. Books from the Roboflow Universe Platform specifically made by:
   * [@book-ywepn](https://universe.roboflow.com/book-ywepn/book-wuuk7)
   * [@test-qcuam](https://universe.roboflow.com/test-qcuam/books-uqkzq/dataset/1)

> [!NOTE]
> **The Jupyter Notebook or ipynb file contains the code for the model training as well as the interpretation of results and model export.
> It was originally hosted in Google Colab before downloaded in a local machine. The file can be imported back into Google Colab for
> model training using Google Colab's GPUs.**

## Tech Stack
1. LabelImg for Image Annotations
2. Python 3.12.13 from Google Colab
3. Ultralytics YOLO Nano version 11
4. Java 11 for the Android Application
5. Android Studio for Android Application Simulation Testing
