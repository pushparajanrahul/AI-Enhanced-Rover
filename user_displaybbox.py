# Import necessary modules
from PIL import Image, ImageDraw

# Function to display bounding boxes on an image using label information
def display_bounding_boxes(image_path):
    # Convert image path to label path by replacing paths and extensions
    label_path = image_path.replace('/images/', '/labels/')
    label_path = label_path.replace('.png', '.txt')

    # Open the image and create an ImageDraw object for drawing on the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Open the corresponding label file and read lines
    with open(label_path, 'r') as label_file:
        # Iterate through each line in the label file
        for line in label_file.readlines():
            # Split the line into five values: label, x, y, w, h
            label, center_x, center_y, width, height = line.split(' ')

            # Convert string values into floats
            center_x = float(center_x)
            center_y = float(center_y)
            width = float(width)
            height = float(height)

            # Convert center position, width, height into the
            # top-left and bottom-right coordinates relative to the image size
            img_width, img_height = img.size
            x1 = (center_x - width / 2) * img_width
            y1 = (center_y - height / 2) * img_height
            x2 = (center_x + width / 2) * img_width
            y2 = (center_y + height / 2) * img_height

            # Draw the bounding box with red lines on the image
            draw.rectangle((x1, y1, x2, y2),
                           outline=(255, 0, 0),  # Red in RGB
                           width=5)              # Line width

    # Show the image with bounding boxes
    img.show()

# Example usage: Display bounding boxes on a specific image
display_bounding_boxes('./dataset/synthetic_dataset/images/synthesized_image_6.png')
