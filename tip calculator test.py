import py3Dmol
import matplotlib as plt
import pandas as pd
import cv2

def convert_image_id_2_path(image_id: str) -> str:
    return "../input/bms-molecular-translation/train/{}/{}/{}/{}.png".format(
        image_id[0], image_id[1], image_id[2], image_id
    )


def visualize_train_image(image_id, label):
    plt.figure(figsize=(10, 8))

    image = cv2.imread(convert_image_id_2_path(image_id))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image)
    plt.title(f"{label}", fontsize=14)
    plt.axis("off")

    plt.show()
'''
train_labels = pd.read_csv("../input/bms-molecular-translation/train_labels.csv")
index = 1
molecule_image_id = train_labels["image_id"].iloc[index]
molecule_InChI = train_labels["InChI"].iloc[index]

visualize_train_image(molecule_image_id, molecule_InChI)

'''