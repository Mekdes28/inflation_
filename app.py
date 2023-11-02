# app.py

from flask import Flask, render_template, request

# Importing the linear regression model (using scikit-learn as an example)
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Example data (you would use your actual historical data)
last_month_data = [[1], [2], [3], [4], [5]]  # Features of last month
inflation = [1.5, 2.0, 2.5, 2.8, 3.0]  # Inflation for corresponding months

# Train the model
model = LinearRegression()
model.fit(last_month_data, inflation)

@app.route('/')
def index():
    return render_template('index.html', prediction="")

@app.route('/predict', methods=['POST'])
def predict():
    user_input = float(request.form['last_month_inflation'])
    user_input = [[user_input]]  # Reshaping for prediction
    predicted_inflation = model.predict(user_input)
    return render_template('index.html', prediction=f"Predicted inflation for this month: {predicted_inflation[0]:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
