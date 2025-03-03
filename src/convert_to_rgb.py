from PIL import Image
import os

# Paths
source_dir = "/Users/ibergeland/Projects/art-generator/data/my_images/art_abstract/source_data"
destination_dir = "/Users/ibergeland/Projects/art-generator/data/my_images/art_abstract/converted_data/rgb_data"

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Convert images to RGB and save to the destination
for root, _, files in os.walk(source_dir):
    for file in files:
        if file.endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(root, file)
            img = Image.open(img_path).convert("RGB")
            
            # Preserve the relative folder structure
            relative_path = os.path.relpath(img_path, source_dir)
            save_path = os.path.join(destination_dir, relative_path)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            # Save the RGB image
            img.save(save_path)

print(f"All images have been converted to RGB format and saved in: {destination_dir}")