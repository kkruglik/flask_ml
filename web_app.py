from flask import Flask, jsonify, request
from model import make_churn_prediction

app = Flask('user_churn')

@app.route('/about', methods=['GET'])
def about():
    return 'App for user churn prediction'

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    result = make_churn_prediction(customer)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)