# darknet-yolo
For car and pedestrain recognition.

![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

This repository is forked from https://github.com/pjreddie/darknet. More information about the yolo see from https://pjreddie.com/darknet/yolo/.

Setting and training information see from https://github.com/AlexeyAB/darknet.

The dataset is from the Pascal VOC Data and the KITTI Vision Benchmark Suite. 

First, it need to generate the label files for the dataset.

How to generate the label files for the dataset:

Because the Pascal VOC Data and the dataset from the KITTI Vision Benchmark Suite already have the label files, it just can use these files to generate the new label files for this project.

For the Pascal VOC Data, it can use [scripts/voc_label.py](https://github.com/peterliu1991/darknet-yolo/scripts/voc_label.py) to convert existing VOC annotations to darknet format. I just need the three categories which are bus, car and person from the label files and generate the new label filesbuild by using [scripts/generate_voc_label.py](https://github.com/peterliu1991/darknet-yolo/scripts/generate_voc_label.py]).


For the KITTI Vision Benchmark Suite, I just need the four categories whcih are Car, Truck, Van, Pedestrain and Person_sitting and generate the new label files by using [scripts/generate_kitti_label.py](https://github.com/peterliu1991/darknet-yolo/scripts/generate_kitti_label.py).

Second, I create the yolo-car-voc.cfg and car-voc.data in the cfg folder. In the data folder, I add the car-voc.name, car-voc_training.txt and car-voc_validation.txt.

The pre-trained weights for the training part: http://pjreddie.com/media/files/darknet19_448.conv.23.

