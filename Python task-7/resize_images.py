import os
from PIL import Image

# Folder containing images
input_folder = 'input_folder'
output_folder = 'output_folder'
target_size = (256, 256)  # Desired size, e.g., 256x256

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        resized_img = img.resize(target_size)
        # Change format if needed, e.g., PNG
        base, ext = os.path.splitext(filename)
        save_path = os.path.join(output_folder, base + '.png')
        resized_img.save(save_path)
        print(f'Resized and saved image: {save_path}')
