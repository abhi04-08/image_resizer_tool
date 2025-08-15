import os
from PIL import Image

# User inputs
source_folder = 'images'
output_folder = 'output'
image_width = 600
image_height = 800
output_format = "JPEG"

# if path not exists create a path
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each file from source_folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.webp', '.bmp', '.tiff')):
        img_path = os.path.join(source_folder, filename)

        try:
            img = Image.open(img_path)

            img = img.resize((image_width,image_height), Image.Resampling.LANCZOS)

            base_name = os.path.splitext(filename)[0]
            save_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img.save(save_path, output_format)

            print(f"Resize & saved: {save_path}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Batch resizing complete")