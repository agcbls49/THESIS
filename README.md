# Vocasee
Vocasee is a Voice-Guided Indoor Object Finder Android Application for Visually Impaired Users

## Created By
Amazing Grace O. Cabiles - Dataset Annotations and Machine Learning Model Training <br>
Cyrelle Kristin P. Gapit - <br>
Francen P. Manalo - <br>

## Dataset
A custom dataset was used for this project consisting of images captured under varying lighting conditions. The dataset was split into 80% train, 10% validation and 10% test sets. The YOLO model was trained using this dataset with the following configurations: images were resized to 640×640, a batch size of 16 was used, and training was conducted for 50 epochs.

**[The dataset source can be found here](https://drive.google.com/)**

> [!NOTE]
> **The data listed on the table below is subject to change and was updated in May 6, 2026.
> Annotation started in April 23, 2026. No synthetic data was used.**

The dataset includes the following:
| Folder Name | Class Number | Class Name | Number of Images |
|-------------|--------------|------------|------------------|
|backpacks    |0             |backpack    |100               |
|books        |1             |book        |100               |
|cups         |2             |cup         |100               |
|eyeglasses   |3             |glasses     |100               |
|headphones   |4             |headphone   |100               |
|keys         |5             |key         |100               |
|phones       |6             |phone       |100               |
|remotes      |7             |remote      |100               |
|wallets      |8             |wallet      |100               |
|waterbottles |9             |water bottle|100               |
|bodysprays   |10            |body spray  |                  |
|cards        |11            |card        |                  |
|chargers     |12            |charger     |                  |
|combs        |13            |comb        |                  |
|flashlights  |14            |flashlight  |                  |
|glassescases |15            |glasses case|                  |
|medicines    |16            |medicine    |                  |
|nailclippers |17            |nail clipper|                  |
|shoes        |18            |shoe        |                  |
|watches      |19            |watch       |100               |

## Model Used

## Tech Stack
1. LabelImg for image annotations
2. Python 3.12.13 from Google Colab
3. Ultralytics YOLO Nano versions
