import os
from PIL import Image

# Define directories
changed_dir = "data/changed"
reduced_dir = "data/reduced"

# Ensure the output directory exists
os.makedirs(reduced_dir, exist_ok=True)

# Target size in bytes (2MB)
MAX_SIZE = 2 * 1024 * 1024

# Function to reduce image size
def compress_image(input_path, output_path, max_size=MAX_SIZE):
    with Image.open(input_path) as img:
        img = img.convert("RGB")  # Convert to RGB to ensure compatibility
        
        # Initial quality and resize settings
        quality = 90
        width, height = img.size
        
        while True:
            # Save with current quality
            img.save(output_path, "PNG", optimize=True, quality=quality)
            file_size = os.path.getsize(output_path)

            # If file is under max size, we're done
            if file_size <= max_size:
                break

            # Reduce image size by scaling down
            width = int(width * 0.9)  # Reduce width by 10%
            height = int(height * 0.9)  # Reduce height by 10%
            img = img.resize((width, height), Image.LANCZOS)

            # Reduce quality step by step
            quality -= 5
            if quality < 10:  # Stop if quality is too low
                break

    print(f"Reduced: {input_path} -> {output_path} ({file_size / 1024:.2f} KB)")

# Process all PNG files in the changed directory
for filename in os.listdir(changed_dir):
    if filename.lower().endswith(".png"):
        changed_path = os.path.join(changed_dir, filename)
        reduced_path = os.path.join(reduced_dir, filename)
        compress_image(changed_path, reduced_path)

print("All images reduced successfully.")
