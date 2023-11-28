import os
import numpy as np
import shutil
import glob

def get_filenames(folder):
    filenames = set()
    
    for path in glob.glob(os.path.join(folder, '*.png')):
        # Extract the filename
        filename = os.path.split(path)[-1]        
        filenames.add(filename)

    return filenames

def fldr_strt():
    if not os.path.exists('data'):
        for folder in ['images', 'labels']:
            for split in ['train', 'val', 'test']:
                os.makedirs(f'data/{folder}/{split}')


def split_dataset(dataset_type, image_names, train_size, val_size):
    for i, image_name in enumerate(image_names):
        # Label filename
        label_name = image_name.replace('.png', '.txt')
        
        # Split into train, val, or test
        if i < train_size:
            split = 'train'
        elif i < train_size + val_size:
            split = 'val'
        else:
            split = 'test'
        
        # Source paths
        source_image_path = f'dataset/{dataset_type}/images/{image_name}'
        source_label_path = f'dataset/{dataset_type}/labels/{label_name}'

        # Destination paths
        target_image_folder = f'data/images/{split}'
        target_label_folder = f'data/labels/{split}'

        # Copy files
        shutil.copy(source_image_path, target_image_folder)
        shutil.copy(source_label_path, target_label_folder)


if __name__ == '__main__':
    
    #Create a folder structure for YOLOv5 training
    fldr_strt()

    #Get filenames
    syn_images = get_filenames('dataset/synthetic_dataset/images')
    #real_images = get_filenames('dataset/real_dataset/images')

    #Shuffle the images

    # Synthetic dataset
    split_dataset('synthetic_dataset', syn_images, train_size=2400, val_size=90)

    # Real dataset
    #split_dataset('real_dataset', real_images, train_size=399, val_size=49)