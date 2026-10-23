# VocaSee
VocaSee is a Voice-Guided Indoor Object Finder Android Application for Visually Impaired Users. 
The Android application code is made by [Cyrelle Kristin Gapit](https://github.com/tunasai/Vocasee). 

The ***data preprocessing folder*** contains the python scripts used to prepare the dataset.

The ***colab folder*** contains the .ipynb files used to train the models in Google Colab.

The ***yolo26n folder*** contains the weights and default training settings of the selected model in the Android application.

## Dataset Information

A custom dataset was used for this project consisting of researcher-taken images captured under varying lighting conditions and was combined with supplementary images from Kaggle and Roboflow Universe. The dataset was split into **70% train, 20% validation and 10% test** and **80% train, 10% validation and 10% test** sets. 

All YOLO Nano models were trained using this dataset with the following default YOLO configurations: images were resized to 640×640, a batch size of 16 was used, and training was conducted for 100 epochs. The experimentation of this project is conducted through the data splitting, epoch changes (150 epoch retraining on the best model), and model results comparison (to choose model for epoch retraining and select which model for deployment in the Android application).

> [!NOTE]
> **The data listed on the table below is the final dataset classes and image counts** <br>
> Each class has 300 images which totals to 7,200 images.
> An additional 720 unlabled images (10% of 7,200) is included in the final dataset count. <br>
> **The total dataset image count is: 7,920**

The dataset includes the following:

|Class Name    | Class Number |
|--------------|--------------|
| backpack     |0             |
| book         |1             |
| cup          |2             |
| glasses      |3             |
| headset      |4             |
| key          |5             |
| phone        |6             |
| remote       |7             |
| wallet       |8             |
| water bottle |9             |
| body spray   |10            |
| card         |11            |
| charger      |12            |
| comb         |13            |
| flashlight   |14            |
| glasses case |15            |
| medicine     |16            |
| nail clipper |17            |
| shoe         |18            |
| watch        |19            |
| body scrub   |20            |
| cane         |21            |
| lighter      |22            |
| towel        |23            |

<br>

> [!IMPORTANT]
> **body scrub class is not to be confused with skin care moisturizing products. body scrubs in this context means body scrubbers used to clean (usually the back) the body. <br>
> headset class includes headphones as well as earphones and earbuds. <br>
> In the total composition of the dataset images, 50 partially occluded images were included hence why the number of images were 300 per class like before.**

## Data Split Image Distributions
**70% Train, 20% Valid, 10% Test Data Split**

| Folder              | Number of Images    |
|---------------------|---------------------|
|Train                |5,544                |
|Validation           |1,584                |
|Test                 |792                  |

<br>

**80% Train, 10% Valid, 10% Test Data Split**
| Folder              | Number of Images    |
|---------------------|---------------------|
|Train                |6,336                |
|Validation           |792                  |
|Test                 |792                  |

> [!NOTE]
> The test split of both data splits contain the same images. As for training settings, the args.yaml file is the same for all models (see the yolo26n folder).

## Data Sources
We used our own custom images as well as the supplementary data sources below.

### Supplementary Data Sources
1. [Body Scrub from the Roboflow Universe Platform by @red-spong](https://universe.roboflow.com/red-spong/sponge-kl0nz)
2. [Body Sprays from the Roboflow Universe Platform by MARIJOY S VILLAR](https://universe.roboflow.com/marijoy-s-villar/perfume-adhjk)
[Chargers from the Roboflow Universe Platform by Nikhilai](https://universe.roboflow.com/nikhilai-anmh1/shop-ai-v1)
3. Books from the Roboflow Universe Platform specifically made by:
   * [@book-ywepn](https://universe.roboflow.com/book-ywepn/book-wuuk7)
   * [@test-qcuam](https://universe.roboflow.com/test-qcuam/books-uqkzq)
4. [Cane from the Roboflow Universe Platform by @nodongjaeteam-g1pbo](https://universe.roboflow.com/nodongjaeteam-g1pbo/white-cane-hyjat)
5. [Cards from the Roboflow Universe Platform by Efe Efesefe](https://universe.roboflow.com/efe-efesefe-gvfaz/credit-cards-n4hrw)
6. [Chargers from the Roboflow Universe Platform by Nikhilai](https://universe.roboflow.com/nikhilai-anmh1/shop-ai-v1)
7. Combs from the Roboflow Universe Platform specifically made by:
   * [@Thiyada](https://universe.roboflow.com/thiyada-g1bzx/comb-lipstick-marshmallow)
   * [@pp-mfp9z](https://universe.roboflow.com/pp-mfp9z/comb-glasses-pen)
   * [@HAZARD](https://universe.roboflow.com/hazard-qjwxm/sharp-objects-detection-i)
   * [@annimal](https://universe.roboflow.com/annimal/powder-comb-treatment)
   * [Combs and Water Bottles from @Artificial intelligence tools Assignment](https://universe.roboflow.com/artificial-intelligence-tools-assignment/bottle-phone-comb)
8. [Cups from Samuel Ayman](https://www.kaggle.com/datasets/samuelayman/cup-dataset)
9. [Flashlights from OORT DataHub](https://www.kaggle.com/datasets/oortdatahub/diverse-tools-image-dataset-for-machine-learning)
10. [Glasses Cases from the Roboflow Universe Platform by s Workspace](https://universe.roboflow.com/s-workspace-lzvrl/glasses-case-detection)
11. [Lighter from the Roboflow Universe Platform by Hwang Sung Min](https://universe.roboflow.com/hwang-sung-min/lighter-nvtss)
12. Remotes from the Roboflow Universe Platform specifically made by:
    * [@Tahsin](https://universe.roboflow.com/tahsin/tv-remote)
    * [@Efe Efesefe](https://universe.roboflow.com/efe-efesefe-gvfaz/remotes)
13. [Towel from the Roboflow Universe Platform by @zezamii](https://universe.roboflow.com/zezamii/towel-detection-1xa8w)
14. [Wallets from the Roboflow Universe Platform by Valuable Object Detection](https://universe.roboflow.com/valuable-object-detection/wallet-mjzrc)
15. [Watches from Ahed Jneed](https://www.kaggle.com/datasets/ahedjneed/fancy-watche-images)
16. [Water Bottles from the Roboflow Universe Platform by waterbottles](https://universe.roboflow.com/waterbottles/water-bottles-0dgex)

## Experiments
1. The **Experiment 1** file contains code for training the **70% train, 20% validation and 10% test dataset split** tested at **100 epochs**.
2. The **Experiment 2** file contains code for training the **80% train, 20% validation and 10% test dataset split** tested at **100 epochs**.
3. The **Experiment 3** file contains code for the model refinement of the **most suitable dataset split evaluated from Experiment 1 and Experiment 2** refined at **150 epochs**.

> [!NOTE]
> **The Jupyter Notebook or ipynb file contains the code for the model training as well as the interpretation of results and model export. <br>
> It was originally hosted in Google Colab before downloaded in a local machine. The file can be imported back into Google Colab for
> model training using Google Colab's GPUs.**

## Created By
Amazing Grace O. Cabiles - Computer Vision Developer <br>
Cyrelle Kristin P. Gapit - Android Developer <br>
Francen P. Manalo - Documenter

## Tech Stack
1. LabelImg v1.8.1 for Image Annotations
2. Python v3.12.13 from Google Colab
3. Ultralytics YOLO Nano versions
4. Java v11 for the Android Application
5. Android Studio for Android Application Development and Testing
