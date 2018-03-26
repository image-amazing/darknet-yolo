# darknet-yolo-
For car and pedestrain recognition

This repository is based on https://github.com/pjreddie/darknet. More information about the yolo see from https://pjreddie.com/darknet/yolo/.

Setting and training information see from https://github.com/AlexeyAB/darknet.

The dataset is from the Pascal VOC Data and the KITTI Vision Benchmark Suite. 

First, it need to generate the label files for the dataset.

How to generate the label files for the dataset:

Because the Pascal VOC Data and the dataset from the KITTI Vision Benchmark Suite already have the label files, it just can use these files to generate the new label files for this project.

For the Pascal VOC Data, it can use scripts/voc_label.py to convert existing VOC annotations to darknet format. I just need the three categories which are bus, car and person from the label files.


For the KITTI Vision Benchmark Suite, I just need the four categories whcih are Car, Truck, Van, Pedestrain and Person_sitting.


