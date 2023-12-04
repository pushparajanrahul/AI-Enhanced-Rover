# Import necessary modules
import os
import numpy as np
import shutil
import glob

# Function to get a set of filenames in a folder with a specific extension
def get_filenames(folder):
    # Create an empty set to store unique filenames
    filenames = set()
    
    # Iterate over files in the specified folder with a PNG extension
    for path in glob.glob(os.path.join(folder, '*.png')):
        # Extract the filename from the path and add it to the set
        filename = os.path.split(path)[-1]        
        filenames.add(filename)

    return filenames

# Function to create a folder structure for YOLOv5 training
def fldr_strt():
    # Check if the 'data' folder exists, and if not, create the necessary subfolders
    if not os.path.exists('data'):
        for folder in ['images', 'labels']:
            for split in ['train', 'val', 'test']:
                os.makedirs(f'data/{folder}/{split}')

# Function to split the dataset into train, validation, and test sets
def split_dataset(dataset_type, image_names, train_size, val_size):
    for i, image_name in enumerate(image_names):
        # Derive the corresponding label filename
        label_name = image_name.replace('.png', '.txt')
        
        # Determine the split category (train, val, or test) based on the index
        if i < train_size:
            split = 'train'
        elif i < train_size + val_size:
            split = 'val'
        else:
            split = 'test'
        
        # Source paths for image and label
        source_image_path = f'dataset/{dataset_type}/images/{image_name}'
        source_label_path = f'dataset/{dataset_type}/labels/{label_name}'

        # Destination paths for copying files to the appropriate split folders
        target_image_folder = f'data/images/{split}'
        target_label_folder = f'data/labels/{split}'

        # Copy files from the source to the destination folders
        shutil.copy(source_image_path, target_image_folder)
        shutil.copy(source_label_path, target_label_folder)

# Entry point for the script
if __name__ == '__main__':
    # Create a folder structure for YOLOv5 training
    fldr_strt()

    # Get filenames for synthetic dataset images
    syn_images = get_filenames('dataset/synthetic_dataset/images')

    # Uncomment the following lines if there's a real dataset
    # real_images = get_filenames('dataset/real_dataset/images')

    # Shuffle the images if needed

    # Split the synthetic dataset into train, validation, and test sets
    split_dataset('synthetic_dataset', syn_images, train_size=240, val_size=5)

    # Uncomment the following lines if there's a real dataset
    # Split the real dataset into train, validation, and test sets
    # split_dataset('real_dataset', real_images, train_size=399, val_size=49)
