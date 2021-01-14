import os
import numpy as np
import shutil
import random

# # Creating Train / Val / Test folders (One time use)
root_dir = '../data/main'
train_dir = '../data/train'
test_dir = '../data/test'
val_dir = '../data/validation'

classes_dir = ['/buy', 'sell']

val_ratio = 0.20
test_ratio = 0.05

for cls in classes_dir:
    #os.makedirs(root_dir +'/train' + cls)
    #os.makedirs(root_dir +'/val' + cls)
    #os.makedirs(root_dir +'/test' + cls)


    # Creating partitions of the data after shuffeling
    src = root_dir + cls # Folder to copy images from
    print("source directory : "+src)
    
    allFileNames = os.listdir(src)
    np.random.shuffle(allFileNames)
    train_FileNames, val_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                              [int(len(allFileNames)* (1 - val_ratio + test_ratio)), 
                                                               int(len(allFileNames)* (1 - test_ratio))])


    train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
    val_FileNames = [src+'/' + name for name in val_FileNames.tolist()]
    test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

    print('Total images: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    print('Validation: ', len(val_FileNames))
    print('Testing: ', len(test_FileNames))
    
    
    # Copy-pasting images
    print("copying training images")
    for name in train_FileNames:
        shutil.copy(name, train_dir + cls)
        
    print("copying validation images")
    for name in val_FileNames:
        shutil.copy(name, val_dir + cls)

    print("copying test images")
    for name in test_FileNames:
        shutil.copy(name, test_dir + cls)
