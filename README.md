<div align="center">

# 🩺 Breast Cancer Detection Using Artificial Neural Network

**An end-to-end Machine Learning project that classifies breast tumors as Benign or Malignant using an Artificial Neural Network (ANN), with an interactive Streamlit web application.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange?logo=tensorflow&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Purpose-Educational-green)

</div>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-objectives)
- [Features](#-features)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Technologies Used](#️-technologies-used)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Data Preprocessing](#-data-preprocessing)
- [Model Development](#-model-development)
- [Model Evaluation](#-model-evaluation)
- [Streamlit Web Application](#-streamlit-web-application)
- [How to Run the Project](#-how-to-run-the-project)
- [Key Learning Outcomes](#-key-learning-outcomes)
- [Future Improvements](#-future-improvements)
- [Disclaimer](#️-disclaimer)
- [Author](#-author)

---

## 📌 Project Overview

This project uses an **Artificial Neural Network (ANN)** to analyze breast tumor-related features and predict whether a tumor is **Benign** or **Malignant**.

It covers the complete Machine Learning workflow: data preprocessing, feature scaling, ANN model development, model evaluation, and deployment of the trained model in an interactive **Streamlit** web application.

> 🎓 This project was developed for **educational and academic purposes** to demonstrate an end-to-end Machine Learning pipeline.

---

## 🎯 Objectives

- Analyze and prepare breast cancer-related data for Machine Learning.
- Apply feature scaling using **StandardScaler**.
- Build an **Artificial Neural Network** for binary classification.
- Evaluate the trained model using standard classification metrics.
- Save the trained model and scaler for future predictions.
- Create a simple **Streamlit** interface for obtaining predictions.

---

## ✨ Features

- 🧹 Data loading, inspection, and preprocessing
- 📏 Feature scaling with `StandardScaler`
- 🤖 ANN-based classification using TensorFlow/Keras
- 📊 Evaluation using Accuracy, Confusion Matrix, and Classification Report
- 💾 Saved model (`.keras`) and saved scaler (`.pkl`) for reuse
- 🌐 Interactive Streamlit app for entering feature values and viewing the predicted class

---

## 🧠 Machine Learning Workflow

```text
Dataset (B_Cancer.xlsx)
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Feature Scaling (StandardScaler)
        ↓
Artificial Neural Network (TensorFlow / Keras)
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Save Trained Model & Scaler
        ↓
Streamlit Application
        ↓
Prediction: Benign / Malignant
```

---

## 🛠️ Technologies Used

| Category | Tools / Libraries |
|----------|-------------------|
| **Programming Language** | Python |
| **Data Handling** | Pandas, NumPy, OpenPyXL |
| **Machine Learning** | Scikit-learn |
| **Deep Learning** | TensorFlow, Keras |
| **Web Application** | Streamlit |
| **Model / Object Saving** | Pickle |
| **Development Environment** | Jupyter Notebook / Google Colab |

---

## 📂 Project Structure

```text
Breast_Cancer_Project/
│
├── B_Cancer.xlsx
├── app.py
├── breast_cancer_ann.keras
├── scaler.pkl
├── untitled8.py
└── README.md
```

| File | Description |
|------|-------------|
| `B_Cancer.xlsx` | Dataset used for training and evaluation |
| `untitled8.py` | Python code for data processing and model development |
| `breast_cancer_ann.keras` | Trained Artificial Neural Network model |
| `scaler.pkl` | Saved `StandardScaler` used for feature preprocessing |
| `app.py` | Streamlit application for making predictions |
| `README.md` | Project documentation |

---

## 📊 Dataset

The project uses a breast cancer dataset containing **numerical features related to breast tumor characteristics**. The data is loaded from `B_Cancer.xlsx` and processed before being passed to the ANN.

The target variable classifies each tumor into one of two categories:

| Class | Meaning |
|-------|---------|
| **Benign** | Non-cancerous tumor |
| **Malignant** | Cancerous tumor |

---

## 🔄 Data Preprocessing

The following preprocessing steps are performed:

1. Load the dataset.
2. Inspect and clean the data.
3. Select the required input features.
4. Separate input features and the target variable.
5. Split the data into training and testing sets.
6. Apply feature scaling using `StandardScaler`.

The scaler fitted during training is saved as **`scaler.pkl`**. The same scaler is loaded in the Streamlit app so that new user input is processed in the same way as the training data.

---

## 🤖 Model Development

An **Artificial Neural Network (ANN)** built with **TensorFlow/Keras** is used as the main classification model. During training, the ANN learns patterns from the input features and uses them to classify new observations as Benign or Malignant.

The trained model is saved as **`breast_cancer_ann.keras`** and loaded by the Streamlit application to make predictions.

---

## 📈 Model Evaluation

The trained model was evaluated using:

- ✅ Accuracy
- ✅ Confusion Matrix
- ✅ Classification Report

### Result

| Metric | Result |
|--------|--------|
| **Accuracy** | Approximately **88%** |

> 📝 **Note:** Model performance may vary depending on the train-test split, preprocessing steps, and training configuration.

---

## 🌐 Streamlit Web Application

To make the model easy to use, a **Streamlit** web application (`app.py`) was developed. Users can enter the required tumor-related feature values and receive a prediction from the trained ANN model.

### How the Application Works

```text
User Input
    ↓
Feature Scaling (scaler.pkl)
    ↓
Trained ANN Model (breast_cancer_ann.keras)
    ↓
Prediction
    ↓
Benign / Malignant
```

### Example Workflow

1. Open the Streamlit application.
2. Enter the required tumor feature values.
3. The input values are scaled using the saved scaler.
4. The processed data is passed to the trained ANN model.
5. The model generates a prediction.
6. The predicted class is displayed in the application.

---

## 🚀 How to Run the Project

### Prerequisites

- Python installed on your system
- `pip` (Python package manager)
- Git (to clone the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Vaishnavi5544/BreastCancer_AI_Project.git
```

### Step 2: Open the Project Folder

```bash
cd BreastCancer_AI_Project
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy scikit-learn tensorflow streamlit openpyxl
```

### Step 4: Run the Streamlit Application

```bash
streamlit run app.py
```

After running the command, Streamlit will display a local URL in the terminal. Open that URL in your web browser to use the application.

---

## 📚 Key Learning Outcomes

Through this project, I learned how to:

- Work with a real-world Machine Learning dataset
- Perform data preprocessing
- Separate features and target variables
- Split data into training and testing sets
- Apply feature scaling using `StandardScaler`
- Build an Artificial Neural Network using TensorFlow/Keras
- Train and evaluate a classification model
- Save and load Machine Learning models
- Save preprocessing objects using Pickle
- Build an interactive Machine Learning application using Streamlit
- Connect a trained model with a web interface
- Develop an end-to-end Machine Learning project

---

## 🔮 Future Improvements

- Perform hyperparameter tuning
- Compare ANN performance with other Machine Learning algorithms
- Add more detailed model evaluation visualizations
- Show prediction probability / confidence information
- Improve the Streamlit user interface
- Add input validation
- Deploy the Streamlit application online
- Add model explainability techniques
- Improve overall model performance

---

## ⚠️ Disclaimer

This project is developed **for educational and academic purposes only**. It is **not a medical diagnosis tool** and must not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for any medical concerns.

---

## 👩‍💻 Author

**Vaishnavi Jadhav**
MCA Student | Aspiring Data Analyst

---

<div align="center">

⭐ If you found this project helpful, consider giving it a star on GitHub!

</div>
