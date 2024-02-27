# AI-Enhanced-Rover

AI-Enhanced-Rover is a machine learning project aimed at developing an intelligent rover using artificial intelligence techniques. The project focuses on enhancing the rover's capabilities through machine learning algorithms, enabling it to perform various tasks autonomously such as hole detection in Industrial pipelines and object identification in unknown terrain or planetary missions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Acknowledgements](#acknowledgements)

## Introduction

This project aims to showcase the pivotal role of an autonomous rover in overcoming limitations inherent in traditional industrial inspection techniques. By integrating YOLOv5s and the Arduino Nano microcontroller, this research project demonstrates how such innovative integration can significantly enhance precision, mitigate downtime, reduce labor costs, and elevate safety standards in wear and tear inspection processes. In industrial settings, meticulous wear and tear inspection of machinery and pipelines is crucial for preemptive measures against potential failures. However, current inspection methodologies face challenges such as lack of adaptability in large robotic systems and safety concerns associated with manual interventions. The AI-Enhanced-Rover addresses these issues by introducing an autonomous rover capable of navigating intricate industrial terrains and executing sophisticated image analysis.

## Features

- **Versatility:** The AI-Enhanced-Rover is designed to navigate diverse industrial terrains, showcasing its adaptability across varied sectors, from manufacturing plants to energy facilities.

- **Precision Inspection:** By incorporating YOLOv5s, the rover achieves high precision in wear and tear detection, surpassing the limitations of traditional inspection methods.

- **Arduino Nano Microcontroller Integration:** The integration of the Arduino Nano microcontroller elevates the rover's capabilities, enabling advanced machine learning analysis in a compact and versatile form factor.

- **Cost Efficiency:** With reduced downtime and labor costs, the AI-Enhanced-Rover offers a cost-effective solution for industrial inspection.

**Areas of the project include:**

- Object detection and recognition
- Remote control capabilities
- Machine learning model training

## Getting Started

To get started, clone this Gitrep on your local machine. The code is compiled using CUDA, and you can utilize it on a CUDA-enabled device.

```bash
git clone https://github.com/pushparajanrahul/AI.Enhanced.Rover-YOLOv5s-ArduinoNano.git

```

After completing the above task, clone the Github repository of YOLOv5 inside this repository.

```bash
git clone https://github.com/ultralytics/yolov5.git

```

## Installation

To set up the project, create a virtual environment inside the Gitrep and install the required dependencies using the following command:

```bash

#Python 3.8.10 was set for the environment

# Creating virtual environment 
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Installing torch and torchvision
pip install torch==2.1.0 torchvision==0.16.0 --index-url https://download.pytorch.org/whl/cu121

# Installing other dependencies
pip install -r requirements.txt
```

## Usage

Run the following scripts in the given order to train the model.

To generate the raw synthetic dataset, the below script is used. The images are generated in the naming philosophy synthetic_image_xxx.jpg, and the labels are generated as separate text files with the same naming philosophy.

```bash
python user_synthticdata.py

```

To see a sample of the image generated with a bounding box, the below script is used.

```bash
python user_displaybbox.py

```

To make the dataset into the YOLOv5 format, run the below utility script. 

```bash
python user_utils.py

```

After running the above script, the directories should be available in the below fashion.

![tree](https://github.com/pushparajanrahul/AI.Enhanced.Rover-YOLOv5s-ArduinoNano/assets/124497777/b5cb26c3-95ef-4c25-96a1-895487dec8c8)



Now start the training by running the below script. You can modify the hyperparameters for varied performances. This script calls the native YOLOv5 training script and loads the hyperparameters as defined.

```bash
python user_train.py

```

On successful completion of the script, the new model weights are generated inside './yolov5/run/train/exp/weights'

After successful training, run the below predefined script to generate an export of the tflite version of the model weights.

```bash
python yolov5/export.py --weights yolov5/runs/train/exp/weights/best.pt --int8 --include tflite

```

Now move push the results into Edge Impulse and generate the export to load into the ArduinoNano module.


## Results

Below are the results obtained on training the model.

1. A snippet of the training results based on epoch runs.

| Epoch | Train Box Loss | Train Object Loss | Train Class Loss | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 | Validation Box Loss | Validation Object Loss | Validation Class Loss | Learning Rate 0 | Learning Rate 1 | Learning Rate 2 |
|-------|-----------------|-------------------|------------------|-----------|--------|---------|--------------|----------------------|------------------------|-----------------------|------------------|------------------|------------------|
| 0     | 0.11201         | 0.034021          | 0                | 0.12512   | 0.25   | 0.25825 | 0.061079     | 0.089727             | 0.021944               | 0                     | 0.070833         | 0.0032407         | 0.0032407         |
| 1     | 0.090303        | 0.033315          | 0                | 0.22146   | 0.25   | 0.21254 | 0.046375     | 0.06471              | 0.019151               | 0                     | 0.040768         | 0.006509          | 0.006509          |
| 2     | 0.083893        | 0.02547           | 0                | 0.046619  | 0.25   | 0.034776| 0.0090582    | 0.074776             | 0.017544               | 0                     | 0.010637         | 0.0097112         | 0.0097112         |
| ...   | ...             | ...               | ...              | ...       | ...    | ...     | ...          | ...                  | ...                    | ...                   | ...              | ...              | ...              |
| 97    | 0.019378        | 0.0098779         | 0                | 0.9875    | 1      | 0.995   | 0.92041      | 0.010113             | 0.0035527              | 0                     | 0.000496         | 0.000496          | 0.000496          |
| 98    | 0.018121        | 0.010828          | 0                | 0.98734   | 1      | 0.995   | 0.93728      | 0.010215             | 0.0035791              | 0                     | 0.000397         | 0.000397          | 0.000397          |
| 99    | 0.016924        | 0.0095128         | 0                | 0.98691   | 1      | 0.995   | 0.94557      | 0.010214             | 0.0035625              | 0                     | 0.000298         | 0.000298          | 0.000298          |


2. Prediction results on training with YOLOv5s

![val_batch0_pred](https://github.com/pushparajanrahul/AI.Enhanced.Rover-YOLOv5s-ArduinoNano/assets/124497777/a086fc04-a186-459d-aa64-c0ad52d2594d)

3. F1-score noted on trainng the Model

![F1_curve](https://github.com/pushparajanrahul/AI.Enhanced.Rover-YOLOv5s-ArduinoNano/assets/124497777/be29cf26-942a-4b50-aba7-cf9de5139c67)

4. Loss Results

![results](https://github.com/pushparajanrahul/AI.Enhanced.Rover-YOLOv5s-ArduinoNano/assets/124497777/e4ae32df-cbaf-4013-ab56-ff14b487bb4e)




## Acknowledgements

I extend my gratitude to the open-source community and the contributors who make projects like this possible.

Happy exploring with the AI-Enhanced-Rover!


