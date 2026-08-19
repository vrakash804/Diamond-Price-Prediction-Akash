# 💎 Diamond Price Prediction

An end-to-end Machine Learning web application that predicts the estimated price of a diamond based on its physical characteristics and quality attributes.

The project uses Machine Learning regression algorithms, automated preprocessing, model evaluation, and a Flask web application to provide diamond price predictions through a simple and professional user interface.

---

## 📌 About the Project

Diamond prices depend on several factors such as carat, cut, color, clarity, depth, table, and the physical dimensions of the diamond.

This project aims to build a Machine Learning regression system that learns the relationship between these features and diamond prices.

The trained model is integrated with a Flask web application where users can enter diamond characteristics and receive an estimated diamond price.

### Key Highlights

- End-to-end Machine Learning pipeline
- Data ingestion and preprocessing
- Numerical and categorical feature transformation
- Multiple regression model comparison
- Automatic selection of the best-performing model
- Model and preprocessing object serialization
- Flask-based prediction application
- Professional responsive user interface
- Input validation
- MLflow experiment tracking support
- Jupyter notebooks for data analysis and experimentation

---

# 🎯 Project Objective

The main objective of this project is to predict the price of a diamond based on its characteristics.

The project follows this Machine Learning workflow:

```text
Dataset
   ↓
Data Ingestion
   ↓
Data Transformation
   ↓
Feature Encoding
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Model Serialization
   ↓
Flask Web Application
   ↓
Diamond Price Prediction

---

# 📈 Model Performance

The project evaluates multiple regression models and automatically selects the model with the best R² score.

| Model | R² Score |
|---|---:|
| Linear Regression | 0.9363 |
| Lasso Regression | **0.9364** |
| Ridge Regression | 0.9363 |
| Elastic Net | 0.8553 |

### 🏆 Best Model

**Lasso Regression**

R² Score:

```text
0.9364

##🛠️ Technology Stack
Python
Pandas
NumPy
Scikit-learn
Flask
Matplotlib
Seaborn
Jupyter Notebook
MLflow
DVC
HTML
CSS
Git & GitHub

##🌐 Web Application

The Flask web application allows users to enter:

Diamond Characteristics
Carat
Depth
Table
X dimension
Y dimension
Z dimension
Cut
Color
Clarity

The entered values are processed using the saved preprocessing pipeline and passed to the trained Machine Learning model.

The predicted diamond price is then displayed to the user.

##📊 Dataset

The project uses the Diamond Price Prediction dataset from Kaggle.

Features
Feature	Description
carat	Weight of the diamond
cut	Quality of diamond cut
color	Diamond color grade
clarity	Diamond clarity grade
depth	Total depth percentage
table	Width of the diamond's top facet
x	Length in millimeters
y	Width in millimeters
z	Depth in millimeters
price	Target variable

Dataset:

https://www.kaggle.com/competitions/playground-series-s3e8/data

##⚙️ Installation

Clone the repository:

git clone https://github.com/vrakash804/Diamond-Price-Prediction-Akash.git

Navigate to the project:

cd Diamond-Price-Prediction-Akash

Create a virtual environment:

python -m venv .venv

Activate it on Windows:

.\.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

##▶️ Run the Application

Start the Flask application:

python app.py

Open the application in your browser:

http://localhost:8080

Diamond-Price-Prediction-Akash/
│
├── Artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── Notebook_Experiments/
│   ├── Exploratory_Data_Analysis.ipynb
│   └── Model_Training.ipynb
│
├── src/
│   └── DiamondPricePrediction/
│       ├── components/
│       ├── pipelines/
│       └── utils/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── form.html
│   └── result.html
│
├── app.py
├── requirements.txt
├── setup.py
├── Dockerfile
├── .gitignore
└── README.md

##👨‍💻 Author
Akash V R

AI/ML Student

GitHub:https://github.com/vrakash804
