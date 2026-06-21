# VocaSee
VocaSee is a Voice-Guided Indoor Object Finder Android Application for Visually Impaired Users

## Created By
Amazing Grace O. Cabiles <br>
Cyrelle Kristin P. Gapit <br>
Francen P. Manalo

## Dataset
A custom dataset was used for this project consisting of images captured under varying lighting conditions and was combined with supplementary images from Kaggle and Roboflow. The dataset was split into **70% train, 20% validation and 10% test** and **80% train, 10% validation and 10% test** sets. All YOLO models were trained using this dataset with the following default YOLO configurations: images were resized to 640×640, a batch size of 16 was used, and training was conducted for 100 epochs. The experimentation of this are conducted trhough the data splitting, epoch changes, and model results comparison.

**[The dataset source can be found here](https://drive.google.com/drive/folders/1jwQUXeVuitPZA2yQ5qw2U9-SQvqCeRwC?usp=sharing)**

> [!NOTE]
> **The data listed on the table below is subject to change and was last updated in June 22, 2026.
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
|remotes      |7             |remote      |300               |
|wallets      |8             |wallet      |300               |
|waterbottles |9             |water bottle|300               |
|bodysprays   |10            |body spray  |300               |
|cards        |11            |card        |300               |
|chargers     |12            |charger     |300               |
|combs        |13            |comb        |300               |
|flashlights  |14            |flashlight  |300               |
|glassescases |15            |glasses case|300               |
|medicines    |16            |medicine    |300               |
|nailclippers |17            |nail clipper|300               |
|shoes        |18            |shoe        |300               |
|watches      |19            |watch       |300               |

<br>

## Supplementary Data Sources
1. [Flashlights from OORT DataHub](https://www.kaggle.com/datasets/oortdatahub/diverse-tools-image-dataset-for-machine-learning)
2. [Watches from Ahed Jneed](https://www.kaggle.com/datasets/ahedjneed/fancy-watche-images)
3. [Cups from Samuel Ayman](https://www.kaggle.com/datasets/samuelayman/cup-dataset)
4. Headphones from the Roboflow Universe Platform specifically made by:
   * [@CVAI Project](https://universe.roboflow.com/headphones-9uy0k/headphones-fwhbt)
   * [@headphones](https://universe.roboflow.com/headphones/headphones-3i2fi)
   * [@headphones-crjvh](https://universe.roboflow.com/headphones-crjvh/headphones-zrumj)

5. Books from the Roboflow Universe Platform specifically made by:
   * [@book-ywepn](https://universe.roboflow.com/book-ywepn/book-wuuk7)
   * [@test-qcuam](https://universe.roboflow.com/test-qcuam/books-uqkzq)
  
6. [Chargers from the Roboflow Universe Platform by Nikhilai](https://universe.roboflow.com/nikhilai-anmh1/shop-ai-v1)
7. Combs from the Roboflow Universe Platform specifically made by:
   * [@Newwy22](https://universe.roboflow.com/newwy22/comb-uqoir)
   * [@Thiyada](https://universe.roboflow.com/thiyada-g1bzx/comb-lipstick-marshmallow)
   * [@pp-mfp9z](https://universe.roboflow.com/pp-mfp9z/comb-glasses-pen)
   * [@HAZARD](https://universe.roboflow.com/hazard-qjwxm/sharp-objects-detection-i)
   * [@annimal](https://universe.roboflow.com/annimal/powder-comb-treatment)
   * ***[Combs and Water Bottles from @Artificial intelligence tools Assignment](https://universe.roboflow.com/artificial-intelligence-tools-assignment/bottle-phone-comb)***
8. [Water Bottles from the Roboflow Universe Platform by waterbottles](https://universe.roboflow.com/waterbottles/water-bottles-0dgex)
9. Remotes from the Roboflow Universe Platform specifically made by:
    * [@Tahsin](https://universe.roboflow.com/tahsin/tv-remote)
    * [@Efe Efesefe](https://universe.roboflow.com/efe-efesefe-gvfaz/remotes)
10. [Body Sprays from the Roboflow Universe Platform by MARIJOY S VILLAR](https://universe.roboflow.com/marijoy-s-villar/perfume-adhjk)
11. [Glasses Cases from the Roboflow Universe Platform by s Workspace](https://universe.roboflow.com/s-workspace-lzvrl/glasses-case-detection)
12. [Cards from the Roboflow Universe Platform by Efe Efesefe](https://universe.roboflow.com/efe-efesefe-gvfaz/credit-cards-n4hrw)
13. [Wallets from the Roboflow Universe Platform by Valuable Object Detection](https://universe.roboflow.com/valuable-object-detection/wallet-mjzrc)

<br>
<br>

## Experiments
The **Experiment 1** file contains code for training the **70% train, 20% validation and 10% test dataset split tested at 100 epochs**. 
The **Experiment 2** file contains code for training the **80% train, 20% validation and 10% test dataset split tested at 100 epochs**. 
The **Experiment 3** file contains code for training the **best dataset split evaluated from Experiment 1 and Experiment 2 tested at 150 epochs**. 
The **Experiment 4** file contains code for training the **best dataset split evaluated from Experiment 1 and Experiment 2 tested at 200 epochs**. 

> [!NOTE]
> **The Jupyter Notebook or ipynb file contains the code for the model training as well as the interpretation of results and model export.
> It was originally hosted in Google Colab before downloaded in a local machine. The file can be imported back into Google Colab for
> model training using Google Colab's GPUs.**

## Tech Stack
1. LabelImg v1.8.1 for Image Annotations
2. Python v3.12.13 from Google Colab
3. Ultralytics YOLO Nano versions
4. Java v11 for the Android Application
5. Android Studio for Android Application Development and Testing
