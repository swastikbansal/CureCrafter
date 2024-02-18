# %%
import torch
from torch import nn
import torchvision.models as models
from torchvision import transforms
from PIL import Image
import os

import random
from matplotlib import pyplot as plt


class DenseNet169(nn.Module):

    def __init__(self, num_classes):
        super(DenseNet169, self).__init__()

        # Load pre-trained DenseNet-169 model
        self.densenet169 = models.densenet169(weights=True)

        # Modify the classifier to match the number of classes
        # model.features.conv0 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
        in_features = self.densenet169.classifier.in_features
        self.densenet169.classifier = nn.Linear(in_features, num_classes)
        self.densenet169.features.conv0 = nn.Conv2d(
            1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False
        )

    def forward(self, x):
        x = self.densenet169(x)
        return x


class XRayPrediction:
    def predict(self, img_path):
        # %%
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # %%
        # Denesnet Model
        model = DenseNet169(15)

        # model = model.load_state_dict(torch.load('Model/XRayresenet5k.pth'))

        model.to(device)

        # %%
        img = Image.open(img_path)
        img = img.resize((224, 224))
        img = transforms.ToTensor()(img)
        img.to(device)

        # %%
        model.eval()
        with torch.inference_mode():
            pred = model(img.unsqueeze(0))
            _, predicted = torch.max(pred, 1)
            predicted = predicted.item()

        # %%
        classes = [
            "Atelectasis",
            "Cardiomegaly",
            "Effusion",
            "Infiltration",
            "Mass",
            "Nodule",
            "Pneumonia",
            "Pneumothorax",
            "Consolidation",
            "Edema",
            "Emphysema",
            "Fibrosis",
            "Pleural_Thickening",
            "Hernia",
            "No Finding",
        ]
        label_idx = dict(enumerate(classes, start=0))

        return label_idx[predicted]

    # plt.imshow(img.permute(1, 2, 0))
    # plt.title(label_idx[predicted])
    # plt.axis('off');

    # %%
