import glob
from pathlib import Path
import random
import os


# Define paths to image folders
image_path = '/content/images/all/ECUSTFD/ImagesWithXml'
train_path = '/content/images/train'
val_path = '/content/images/validation'
test_path = '/content/images/test'

# Get list of all images
jpg_file_list = [path for path in Path(image_path).rglob('*.jpg')]
JPG_file_list = [path for path in Path(image_path).rglob('*.JPG')]
png_file_list = [path for path in Path(image_path).rglob('*.png')]
bmp_file_list = [path for path in Path(image_path).rglob('*.bmp')]

file_list = jpg_file_list + JPG_file_list + png_file_list + bmp_file_list
file_num = len(file_list)
print('Total images: %d' % file_num)

# Determine number of files to move to each folder
train_percent = 0.8  # 80% of the files go to train
val_percent = 0.1    # 10% go to validation
test_percent = 0.1   # 10% go to test
train_num = int(file_num*train_percent)
val_num = int(file_num*val_percent)
test_num = file_num - train_num - val_num
print('Images moving to train: %d' % train_num)
print('Images moving to validation: %d' % val_num)
print('Images moving to test: %d' % test_num)

# Select 80% of files randomly and move them to train folder
for i in range(train_num):
    move_me = random.choice(file_list) #Choose randomly one file from file list
    fn = move_me.name #store file name in fn
    base_fn = move_me.stem #store file name without extension
    parent_path = move_me.parent #get root path from move_me
    xml_fn = base_fn + '.xml' #add extension xml
    os.rename(move_me, train_path+'/'+fn) #move file move_me to train folder
    #move xml from choosen file to train folder
    os.rename(os.path.join(parent_path,xml_fn),os.path.join(train_path,xml_fn))
    file_list.remove(move_me) #remove choosen file from file list to avoid it will choosen again

# Select 10% of remaining files and move them to validation folder
for i in range(val_num):
    move_me = random.choice(file_list)
    fn = move_me.name
    base_fn = move_me.stem
    parent_path = move_me.parent
    xml_fn = base_fn + '.xml'
    os.rename(move_me, val_path+'/'+fn)
    os.rename(os.path.join(parent_path,xml_fn),os.path.join(val_path,xml_fn))
    file_list.remove(move_me)

# Move remaining files to test folder
for i in range(test_num):
    move_me = random.choice(file_list)
    fn = move_me.name
    base_fn = move_me.stem
    parent_path = move_me.parent
    xml_fn = base_fn + '.xml'
    os.rename(move_me, test_path+'/'+fn)
    os.rename(os.path.join(parent_path,xml_fn),os.path.join(test_path,xml_fn))
    file_list.remove(move_me)
