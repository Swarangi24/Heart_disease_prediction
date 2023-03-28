# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, render_template

# Load dataset
df = pd.read_csv('heart.csv')

# Train model
X = df.drop('target', axis=1)
y = df['target']
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Create Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')




@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from request
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    cp = int(request.form['cp'])
    trestbps = int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs = int(request.form['fbs'])
    restecg = int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = int(request.form['slope'])
    ca = int(request.form['ca'])
    thal = int(request.form['thal'])

    # Create input data as a DataFrame
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })

    # Make prediction
    prediction = clf.predict(input_data)

    # Return result
    if prediction[0] == 0:
        result = "Healthy heart"
    else:
        result = "Defective Heart"
    return render_template('output.html', prediction=result)


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
