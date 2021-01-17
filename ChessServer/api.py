# Dependencies
from flask import Flask, request, jsonify, render_template, make_response
import joblib
import traceback
import pandas as pd
import json
import pandas as pd

app = Flask(__name__, template_folder="templates")


@app.route('/predict', methods=['POST'])
def predict():
    if lr:
        try:
            json_ = request.json
            print("Gelen veri:"+json.dumps(json_)+"\n")
            query = pd.get_dummies(pd.DataFrame(json_))

            query = query.reindex(columns=model_columns, fill_value=0)
            prediction = list(lr.predict(query))

            resp = jsonify({'prediction': str(prediction)})
            response = app.response_class(response=pd.Series(prediction).to_json(
                orient='values'), mimetype='application/json')

            print(str(prediction))

            return pd.Series(prediction).to_json(
                orient='values')

        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return ('No model here to use')


@app.route('/')
def home():
    return "Hello World"


if __name__ == '__main__':

    lr = joblib.load("chess-model.pkl")
    print('Model loaded')

    model_columns = joblib.load("chess-model-columns.pkl")

    print('Model columns loaded')

    app.run(debug=True)
