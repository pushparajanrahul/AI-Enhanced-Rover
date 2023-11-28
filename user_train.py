import os

def run_yolov5(data_file, weights_file, epochs, batch_size, freeze):
    command = f"python yolov5/train.py --data {data_file} --weights {weights_file} --epochs {epochs} --batch {batch_size} --freeze {freeze}"
    os.system(command)

if __name__ == "__main__":
    # Replace these values with your actual file paths and parameters
    data_file = "holes.yaml"
    weights_file = "yolov5s.pt"
    epochs = 1
    batch_size = 4
    freeze = 10

    run_yolov5(data_file, weights_file, epochs, batch_size, freeze)
