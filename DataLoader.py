import csv
import io
import os
import pandas as pd
from glob import glob
from PIL import Image, ImageEnhance
import numpy as np
import shutil

os.chdir('D:/')
dir_src = ('D:/UE4 Image Source/Eval data/Abstract/')
DEPTH =   (dir_src + "/Depth/")
UNLIT = (dir_src + "/Unlit/")
PIC =     (dir_src + "/Picture/")
Processed = (dir_src + "/Cooked/")
Train = (Processed + "train/")
Test = (Processed + "test/")
Images = ("image/")
Depths = ("depth/")


try:
    os.mkdir(DEPTH)
    os.mkdir(UNLIT)
    os.mkdir(PIC)
    os.mkdir(Processed)
    os.mkdir(Train)
    os.mkdir(Train + Images)
    os.mkdir(Test)
    os.mkdir(Test + Images)
    os.mkdir(Train + Depths)
    os.mkdir(Test + Depths)

except OSError:
        print('Directory not created.')

counter = 1
for filename in os.listdir(dir_src):

    if counter == 1:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, PIC)
            print("moved " + filename)
            counter = counter+1

    elif counter == 2:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, UNLIT) #Unlit
            print("moved " + filename)
            counter = counter+1

    elif counter == 3:
        if filename.endswith('.png'):
            shutil.move(dir_src + filename, DEPTH) #Depth
            print("moved " + filename)
            counter = 1


i = 0
for filename in os.listdir(PIC):
    os.rename(PIC + '/' + filename, PIC + '/' + str(i) + '.png')
    i = i + 1
    print("renamed " + filename)

j = 0
for filename in os.listdir(DEPTH):
    os.rename(DEPTH + '/' + filename, DEPTH + '/' + str(j) + '.png')
    j = j + 1
    print("renamed " + filename)

k = 0
for filename in os.listdir(UNLIT):
    os.rename(UNLIT + '/' + filename, UNLIT + '/' + str(i) + '.png')
    i = i + 1
    print("renamed " + filename)


ImagePath = PIC
DepthPath = DEPTH

test_remaining = 50
with open(Processed + 'ue4_test.csv', 'w') as csvFile:
    for filename in os.listdir(ImagePath):
        if test_remaining > 0:
            row = 'test/image/' + str(filename) + ',' + 'test/depth/' + str(filename)
            img = Image.open(ImagePath + filename)
            img = img.convert('RGB')
            img.save(Processed + 'test/image/' + filename)
            print('saved Image ' + str(filename) + ' shape: ' + str(img.mode))
            depth = Image.open(DepthPath + filename)
            depth = depth.convert('L')
            depth.save(Processed + 'test/depth/' + filename, quality=100)
            print('saved Depth ' + str(filename) + ' shape: ' + str(depth.mode))
            print('------------------------------')
            csvFile.write(row)
            csvFile.write('\n')
            test_remaining -= 1


train_remaining = 0
with open(Processed + 'ue4_train.csv', 'w') as csvFile2:
    for chosen in os.listdir(ImagePath):
         if  os.path.isfile(Processed + 'test/image/' + chosen) == False and train_remaining > 0:  #
            print(os.path.isfile(Processed + 'test/image/' + chosen))
            train_row = 'train/image/' + str(chosen).replace('.png', '.jpg') + ',' + 'train/depth/' + str(chosen)
            im = Image.open(ImagePath + chosen)
            im = im.convert('RGB')
            im.save(Processed + 'train/image/' + str(chosen).replace('.png','.jpg'), quality=100)
            print('saved Image ' + str(chosen) + ' shape: ' + str(im.mode))
            train_depth = Image.open(DepthPath + chosen)
            train_depth = train_depth.convert('L')
            train_depth.save(Processed + 'train/depth/' + str(chosen), quality=100)
            print('saved Depth ' + str(chosen) + ' shape: ' + str(train_depth.mode))
            train_remaining -= 1
            print('------------------------------')
            csvFile2.write(train_row)
            csvFile2.write('\n')

