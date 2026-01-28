from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model.pkl')
class_names = ['setosa', 'versicolor', 'virginica']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    features = np.array([[
        data['sepal_length'],
        data['sepal_width'],
        data['petal_length'],
        data['petal_width']
    ]])
    
    prediction_id = model.predict(features)[0]
    prediction_name = class_names[prediction_id]
    
    return jsonify({
        'prediction': prediction_name,
        'class_id': int(prediction_id)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)