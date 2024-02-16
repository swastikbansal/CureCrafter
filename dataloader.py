import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import pandas as pd
import os as os

class EyeDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.data = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, f"{self.data['ID'][idx]}.png")
        image = Image.open(img_name).convert("RGB")

        # Extract labels from specified columns
        label_columns = ['DR', 'ARMD', 'MH', 'DN', 'MYA', 'BRVO', 'TSLN', 'ERM', 'LS', 'MS', 'CSR', 'ODC',
                         'CRVO', 'TV', 'AH', 'ODP', 'ODE', 'ST', 'AION', 'PT', 'RT', 'RS', 'CRS', 'EDN',
                         'RPEC', 'MHL', 'RP', 'CWS', 'CB', 'ODPM', 'PRH', 'MNF', 'HR', 'CRAO', 'TD', 'CME',
                         'PTCR', 'CF', 'VH', 'MCA', 'VS', 'BRAO', 'PLQ', 'HPED', 'CL']

        labels = self.data.loc[idx, label_columns].values.astype(float)

        if self.transform:
            image = self.transform(image)

        return image, labels

# Specify the paths to your train and test datasets
train_root_dir = r'E:\Downloads\rchive\Training_Set\Training_Set\Training'
test_root_dir = r'E:\Downloads\rchive\Test_Set\Test_Set\Test'

# Path to your train and test CSV files
train_csv_file = r'E:\Downloads\rchive\Training_Set\Training_Set\RFMiD_Training_Labels.csv'
test_csv_file = r'E:\Downloads\rchive\Test_Set\Test_Set\RFMiD_Testing_Labels.csv'


# Create datasets and loaders
train_dataset = EyeDataset(csv_file=train_csv_file, root_dir=train_root_dir)
test_dataset = EyeDataset(csv_file=test_csv_file, root_dir=test_root_dir)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

import random
import matplotlib.pyplot as plt

# Assuming you already have the EyeDataset class and train_loader defined

# Define the label columns
label_columns = ['DR', 'ARMD', 'MH', 'DN', 'MYA', 'BRVO', 'TSLN', 'ERM', 'LS', 'MS', 'CSR', 'ODC',
                 'CRVO', 'TV', 'AH', 'ODP', 'ODE', 'ST', 'AION', 'PT', 'RT', 'RS', 'CRS', 'EDN',
                 'RPEC', 'MHL', 'RP', 'CWS', 'CB', 'ODPM', 'PRH', 'MNF', 'HR', 'CRAO', 'TD', 'CME',
                 'PTCR', 'CF', 'VH', 'MCA', 'VS', 'BRAO', 'PLQ', 'HPED', 'CL']

# Get a random index from the training dataset
random_index = random.randint(0, len(train_dataset) - 1)

# Retrieve the image and labels for the random index
sample_image, sample_labels = train_dataset[random_index]

# Display the image
plt.imshow(sample_image)
plt.title(f"Image Index: {random_index + 1}")
plt.show()

# Print labels with value 1
print(f"Labels for Image Index {random_index + 1} with value 1:")
for column, value in zip(label_columns, sample_labels):
    if value == 1:
        print(f"{column}: {value}")





