import os
from PIL import Image

# Define directories
raw_dir = "data/raw"
changed_dir = "data/changed"

# Ensure the output directory exists
os.makedirs(changed_dir, exist_ok=True)

# Process each .webp file in the raw directory
for filename in os.listdir(raw_dir):
    if filename.lower().endswith(".webp"):
        raw_path = os.path.join(raw_dir, filename)
        changed_path = os.path.join(changed_dir, filename.replace(".webp", ".png"))

        # Open and convert the image
        with Image.open(raw_path) as img:
            img.save(changed_path, "PNG")

        print(f"Converted: {raw_path} -> {changed_path}")

print("All images converted successfully.")
