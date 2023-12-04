# AI-Enhanced-Rover

AI-Enhanced-Rover is a machine learning project aimed at developing an intelligent rover using artificial intelligence techniques. The project focuses on enhancing the rover's capabilities through machine learning algorithms, enabling it to perform various tasks autonomously such as hole detection in Industrial pipelines and object identification in unknown terrain or planetary missions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This project aims to showcase the pivotal role of an autonomous rover in overcoming limitations inherent in traditional industrial inspection techniques. By integrating YOLOv5s and the CAM32 microcontroller, this research project demonstrates how such innovative integration can significantly enhance precision, mitigate downtime, reduce labor costs, and elevate safety standards in wear and tear inspection processes. In industrial settings, meticulous wear and tear inspection of machinery and pipelines is crucial for preemptive measures against potential failures. However, current inspection methodologies face challenges such as lack of adaptability in large robotic systems and safety concerns associated with manual interventions. The AI-Enhanced-Rover addresses these issues by introducing an autonomous rover capable of navigating intricate industrial terrains and executing sophisticated image analysis.


## Features

- **Versatility:** The AI-Enhanced-Rover is designed to navigate diverse industrial terrains, showcasing its adaptability across varied sectors, from manufacturing plants to energy facilities.

- **Precision Inspection:** By incorporating YOLOv5s, the rover achieves high precision in wear and tear detection, surpassing the limitations of traditional inspection methods.

- **CAM32 Microcontroller Integration:** The integration of the CAM32 microcontroller elevates the rover's capabilities, enabling advanced machine learning analysis in a compact and versatile form factor.

- **Cost Efficiency:** With reduced downtime and labor costs, the AI-Enhanced-Rover offers a cost-effective solution for industrial inspection.

Area's of project include:

- Object detection and recognition
- Remote control capabilities
- Machine learning model training

## Getting Started

Include instructions on how to get started with your project. This may include prerequisites, hardware requirements, and any setup steps.

## Installation

To set up the project, create a virtual environment and install the required dependencies using the following command:

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




