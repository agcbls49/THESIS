# VocaSee
VocaSee is a Voice-Guided Indoor Object Finder Android Application for Visually Impaired Users. This repository contains the Google Colab files used for training the YOLO Nano models used in our Thesis.

<br>

A custom dataset was used for this project consisting of images captured under varying lighting conditions and was combined with supplementary images from Kaggle and Roboflow. The dataset was split into **70% train, 20% validation and 10% test** and **80% train, 10% validation and 10% test** sets. All YOLO Nano models were trained using this dataset with the following default YOLO configurations: images were resized to 640×640, a batch size of 16 was used, and training was conducted for 100 epochs. The experimentation of this project is conducted through the data splitting, epoch changes, and model results comparison.

> [!NOTE]
> **The data listed on the table below is subject to change and was last updated in August 15, 2026.
> Annotation started in April 23, 2026.**

The current total of images in the dataset is images. The 300 added are unlabeled images.

The dataset includes the following:
| Class Number | Class Name | Number of Images |
|--------------|------------|------------------|
|0             |body scrub  |                  |
|1             |cane        |                  |
|2             |charger     |250               |
|3             |comb        |250               |
|4             |headset     |100               |
|5             |lighter     |                  |
|6             |medicine    |250               |
|7             |phone       |250               |
|8             |toys        |                  |
|9             |towel       |                  |

**headset class includes headphones as well as earphones. In the total composition of the dataset images, 50 partially occluded images were included hence why the number of images were 300 per class.**

## Data Split Image Distributions
**70% Train, 20% Valid, 10% Test Data Split**

| Folder              | Number of Images    |
|---------------------|---------------------|
|Train                |                     |
|Validation           |                     |
|Test                 |                     |

<br>

**80% Train, 10% Valid, 10% Test Data Split**
| Folder              | Number of Images    |
|---------------------|---------------------|
|Train                |                     |
|Validation           |                     |
|Test                 |                     |

<br>

## Data Sources
Our own custom data source as well as the supplementary data sources below.

### Supplementary Data Sources
1. Headphones from the Roboflow Universe Platform specifically made by:
   * [@CVAI Project](https://universe.roboflow.com/headphones-9uy0k/headphones-fwhbt)
   * [@headphones](https://universe.roboflow.com/headphones/headphones-3i2fi)
   * [@headphones-crjvh](https://universe.roboflow.com/headphones-crjvh/headphones-zrumj)
2. [Chargers from the Roboflow Universe Platform by Nikhilai](https://universe.roboflow.com/nikhilai-anmh1/shop-ai-v1)
3. Combs from the Roboflow Universe Platform specifically made by:
   * [@Newwy22](https://universe.roboflow.com/newwy22/comb-uqoir)
   * [@Thiyada](https://universe.roboflow.com/thiyada-g1bzx/comb-lipstick-marshmallow)
   * [@pp-mfp9z](https://universe.roboflow.com/pp-mfp9z/comb-glasses-pen)
   * [@HAZARD](https://universe.roboflow.com/hazard-qjwxm/sharp-objects-detection-i)
   * [@annimal](https://universe.roboflow.com/annimal/powder-comb-treatment)
   * ***[Combs and Water Bottles from @Artificial intelligence tools Assignment](https://universe.roboflow.com/artificial-intelligence-tools-assignment/bottle-phone-comb)***

<br>
<br>

## Experiments
1. The **Experiment 1** file contains code for training the **70% train, 20% validation and 10% test dataset split** tested at **100 epochs**.
2. The **Experiment 2** file contains code for training the **80% train, 20% validation and 10% test dataset split** tested at **100 epochs**.
3. The **Experiment 3** file contains code for training the **best dataset split evaluated from Experiment 1 and Experiment 2** tested at **150 epochs** and **200 epochs**.

> [!NOTE]
> **The Jupyter Notebook or ipynb file contains the code for the model training as well as the interpretation of results and model export.
> It was originally hosted in Google Colab before downloaded in a local machine. The file can be imported back into Google Colab for
> model training using Google Colab's GPUs.**

## Created By
Amazing Grace O. Cabiles <br>
Cyrelle Kristin P. Gapit <br>
Francen P. Manalo

## Tech Stack
1. LabelImg v1.8.1 for Image Annotations
2. Python v3.12.13 from Google Colab
3. Ultralytics YOLO Nano versions
4. Java v11 for the Android Application
5. Android Studio for Android Application Development and Testing
