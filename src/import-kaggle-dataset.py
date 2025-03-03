import kagglehub
import shutil
import os

# Download the dataset
path = kagglehub.dataset_download("danielvalyano/abstract-paintings")

# Move the dataset to your desired folder
destination = os.path.expanduser("~/Projects/art-generator/data/my_images")
os.makedirs(destination, exist_ok=True)
shutil.move(path, destination)

print(f"Dataset moved to: {destination}")
