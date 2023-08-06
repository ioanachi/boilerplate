# -*- coding: utf-8 -*-
"""Kaggke_keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AholO1PJrpZ5UhRnKYohKGNPx_PHEhvm
"""

# ***
!pwd   - in order to check the directory that you are in run 
!ls    -lists all the folders and files in the current directory
# ***


from google.colab import files
files.upload()

"""#### A link with explenations can be found here https://www.analyticsvidhya.com/blog/2021/06/how-to-load-kaggle-datasets-directly-into-google-colab/
 and this
 https://www.kaggle.com/discussions/general/74235
"""

!pip install kaggle
!mkdir ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets list



# competition_name = "Alzheimer's Dataset ( 4 class of Images)"

dataset_name = "tourist55/alzheimers-dataset-4-class-of-images"


# !kaggle competitions download -c {competition_name}
!kaggle datasets download  {dataset_name}


# create a folder to unzip the dataset
folder_name = f"{dataset_name.split('/')[1]}.zip"
print(folder_name)

# unzip the dataset
!mkdir data_train
!unzip  $folder_name -d data_train

!pip install tensorflow==2.13.0 -q

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
import keras
from keras import layers


from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.layers import Dropout, Flatten, Dense , GlobalAveragePooling2DIMAGE_SIZE = [224, 224]

BATCH_SIZE = 100
EPOCHS = 3
COMP_PATH = "../input/alzheimermridataset/Alzheimer_s Dataset"

TRAIN_DIR = f"{COMP_PATH}/train"
TEST_DIR = f"{COMP_PATH}/test"
CLASSES = [ 'NonDemented',
            'VeryMildDemented',
            'MildDemented',
            'ModerateDemented']


/content/alzheimers-dataset-4-class-of-images.zip









