import pandas as pd
import traceback

from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)
model = None


@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            json_ = request.json
            query = pd.get_dummies(pd.DataFrame(json_))

            prediction = list(model.predict(query))

            return jsonify({"prediction": list(map(int, prediction))})

        except Exception as e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        return 'no model found'

if __name__ == '__main__':
    try:
        model = joblib.load('vinegar.pkl')
        print('model loaded')
    except Exception as e:
        print(str(e))
        model = None

    app.run(host='0.0.0.0', port=80)
