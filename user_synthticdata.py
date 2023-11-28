from PIL import Image, ImageDraw
import random
import numpy as np
import os

# Function to create a synthesized image and its label
def create_synthesized_image(image_width, image_height, num_dots_range, dot_size_range, noise_scale):
    synthesized_image = Image.new("RGB", (image_width, image_height), color=(0, 0, 0))
    draw = ImageDraw.Draw(synthesized_image)

    num_dots = random.randint(*num_dots_range)

    labels = []

    for _ in range(num_dots):
        x = random.randint(0, image_width - 1)
        y = random.randint(0, image_height - 1)
        dot_size = random.randint(*dot_size_range)
        draw.ellipse((x, y, x + dot_size, y + dot_size), fill=(255, 255, 255))

        # Calculate label values
        center_x = (x + x + dot_size) / (2.0 * image_width)
        center_y = (y + y + dot_size) / (2.0 * image_height)
        width = dot_size / image_width
        height = dot_size / image_height

        labels.append(f"0 {center_x} {center_y} {width} {height}")

    # Convert image to array and add noise
    synthesized_image_array = np.array(synthesized_image)
    noise = np.random.normal(loc=0, scale=noise_scale, size=(image_height, image_width, 3)).astype(np.uint8)
    synthesized_image_array = np.clip(synthesized_image_array + noise, 0, 255)

    # Save image
    synthesized_image_with_noise = Image.fromarray(synthesized_image_array)
    return synthesized_image_with_noise, labels

# Directory to save the synthesized images
root_directory = "./dataset/synthetic_dataset"
image_directory = root_directory+'./images/'
label_directory = root_directory+'./labels/'

# Ensure the output directory exists
os.makedirs(image_directory, exist_ok=True)
os.makedirs(label_directory, exist_ok=True)


# Parameters
image_width = 640
image_height = 480
num_dots_range = (0, 5)
dot_size_range = (15, 250)
noise_scale = 1.0

# Create 100 images
for i in range(2500):
    synthesized_image, labels = create_synthesized_image(image_width, image_height, num_dots_range, dot_size_range, noise_scale)

    # Save image
    image_path = os.path.join(image_directory, f"synthesized_image_{i + 1}.png")
    synthesized_image.save(image_path)

    # Save label
    label_path = os.path.join(label_directory, f"synthesized_image_{i + 1}.txt")
    with open(label_path, "w") as label_file:
        label_file.write("\n".join(labels))

    print(f"Image {i + 1} created and saved successfully with {len(labels)} dots.")

print("Images and labels created and saved successfully.")