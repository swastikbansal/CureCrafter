from torch.utils.data import Dataset, DataLoader
import torch
from torchvision import transforms
from PIL import Image
import pandas as pd
import os as os

class CustomDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.data = pd.read_csv(csv_file)[:3000]
        self.root_dir = root_dir
        self.transform = transform
    
        self.data = pd.DataFrame(self.data.loc['Image Index', 'Finding Labels'])
        
        #One Hot Encoding
        label = [w.plit('|') for w in self.data['Finding Labels']]
        unieque_olabels = list(set([w for sublist in label for w in sublist]))
        df = pd.DataFrame(0, index = range(len(self.data)), columns = unieque_olabels)

        pd.concat([self.data, df])
        
        print(self.data)        
        
        self.classes = ['Atelectasis' , 'Cardiomegaly', 'Effusion', 'Infiltration' , 'Mass', 'Nodule' , 'Pneumonia' ,
            'Pneumothorax' , 'Consolidation' , 'Edema', 'Emphysema' , 'Fibrosis' ,'Pleural_Thickening','Hernia','No Finding']

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, f"{self.data['ID'][idx]}.png")
        # image = Image.open(img_name).convert("RGB")
        image = Image.open(img_name)

        labels = torch.tensor(self.data.loc[idx, self.classes].values.astype(float))

        if self.transform:
            image = self.transform(image)

        return image, labels





