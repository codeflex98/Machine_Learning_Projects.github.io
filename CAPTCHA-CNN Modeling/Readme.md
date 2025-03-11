# Automated CAPTCHA Recognition Using Convolutional Neural Networks (CNNs): A Deep Learning Approach
## Project Overview
This project focuses on developing a deep learning-based CAPTCHA recognition system using **Convolutional Neural Networks (CNNs)**. CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is a widely used security measure to distinguish humans from bots. By utilizing **deep learning**, this project aims to automate the recognition and decoding of CAPTCHA images.

## Repository Structure
```
CAPTCHA-CNN-Project/
│-- CAPTCHA-CNN_Report.html  # Project Report (Quarto markdown file)
│-- CAPTCHA-CNN_project.ipynb  # Jupyter Notebook with model training and testing
│-- README.md  # Project documentation (this file)
```

## Prerequisites
Before running the project, ensure that you have the following dependencies installed:

- Python 3.x
- Jupyter Notebook
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib
- OpenCV

You can install the necessary packages using:
```bash
pip install tensorflow numpy pandas matplotlib opencv-python
```

## How to Run the Project
### Step 1: Load the Dataset
Ensure that the CAPTCHA dataset is stored in the `dataset/` directory. The dataset consists of images labeled with their corresponding CAPTCHA text.

### Step 2: Run the Jupyter Notebook
Execute `CAPTCHA-CNN_project.ipynb` step-by-step to:
- Preprocess the images (resizing, grayscale conversion, etc.)
- Train the CNN model on the dataset
- Evaluate the model’s performance

### Step 3: View the Results
Model predictions and evaluation metrics (accuracy, loss, etc.) are stored in the `results/` directory.

## Project Report
The report (`CAPTCHA-CNN_Report.qmd`) contains detailed documentation on:
- Project objectives
- Data preprocessing techniques
- CNN architecture and training process
- Evaluation results
- Future improvements

## Future Enhancements
- Implement **Recurrent Neural Networks (RNNs)** or **Transformer models** for improved accuracy
- Expand dataset to include various CAPTCHA styles
- Deploy the model as a web service for real-time CAPTCHA recognition
