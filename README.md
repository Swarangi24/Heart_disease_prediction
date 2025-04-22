# Heart Disease Prediction using Flask

This project is a web-based application built using **Flask** that predicts the likelihood of heart disease based on user-input medical parameters. It uses a trained machine learning model to evaluate health metrics and provide real-time predictions.

## Features

- Predicts heart disease based on health inputs like age, sex, chest pain type, resting blood pressure, cholesterol, and more.
- Simple and intuitive web interface for user interaction.
- Integrates a machine learning model trained on a public heart disease dataset.
- Provides quick and interpretable results with a risk label (e.g., "At Risk" or "Not at Risk").
- Lightweight, responsive, and easy to deploy.

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn
- **Data**: UCI Heart Disease dataset

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Swarangi24/Heart_disease_prediction.git
   cd Heart_disease_prediction
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask application:

bash
Copy
Edit
python app.py
Open your browser and go to http://localhost:5000
