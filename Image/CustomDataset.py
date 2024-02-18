from torch.utils.data import Dataset, DataLoader
import torch
from torchvision import transforms
from PIL import Image
import pandas as pd
import os as os

class CustomDataset(Dataset):
    def one_hot_encode(self,data):
                """Function to one hot encode the labels."""
                 #Spliting the labels
                labels = [i.split('|') for i in data['Finding Labels']]

                #Get unique labels
                unieque_labels = list(set(j for i in labels for j in i))

                #Creating Dataframe
                df = pd.DataFrame(0, index = range(len(data)), columns= unieque_labels)

                #Assigning 1 in corresponding colunms 
                for i,label in enumerate(labels):
                    df.loc[i, label] = 1
                    
                df = pd.concat([data['Image Index'], df], axis = 1)
                
                return df
            
    def show(self):
        print(self.data)
        
    def __init__(self, csv_file, root_dir, transform=None):
        self.data = pd.read_csv(csv_file)[:3000]
        self.root_dir = root_dir
        self.transform = transform
    
        self.data = pd.DataFrame(self.data[['Image Index', 'Finding Labels']])
        
        self.data = self.one_hot_encode(self.data)
        
        self.classes = ['Atelectasis' , 'Cardiomegaly', 'Effusion', 'Infiltration' , 'Mass', 'Nodule' , 'Pneumonia' ,
            'Pneumothorax' , 'Consolidation' , 'Edema', 'Emphysema' , 'Fibrosis' ,'Pleural_Thickening','Hernia','No Finding']
        self.label_idx = enumerate(self.classes,start=1)
        
    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, f"{self.data['Image Index'][idx]}")
        # image = Image.open(img_name).convert("RGB")
        image = Image.open(img_name)
        
        labels = torch.tensor(self.data.loc[idx, self.classes].values.astype(float))
        # print(labels)
        
        if self.transform:
            image = self.transform(image)

        return image, labels





