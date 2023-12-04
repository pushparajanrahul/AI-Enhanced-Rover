# Import the os module to execute system commands
import os

# Function to run YOLOv5 training using specified parameters
def run_yolov5(data_file, weights_file, epochs, batch_size, freeze):
    # Construct the command for YOLOv5 training using the provided parameters
    command = f"python yolov5/train.py --data {data_file} --weights {weights_file} --epochs {epochs} --batch {batch_size} --freeze {freeze}"

    # Execute the command using the os.system() function
    os.system(command)

# Entry point for the script
if __name__ == "__main__":
    # Replace these values with your actual file paths and training parameters

    # Path to the YAML file containing dataset configuration
    data_file = "holes.yaml"

    # Path to the initial weights file for the YOLOv5 model
    weights_file = "yolov5s.pt"

    # Number of training epochs
    epochs = 100

    # Batch size for training
    batch_size = 4

    # Number of initial layers to freeze during training
    freeze = 10

    # Call the function to run YOLOv5 training with the specified parameters
    run_yolov5(data_file, weights_file, epochs, batch_size, freeze)
