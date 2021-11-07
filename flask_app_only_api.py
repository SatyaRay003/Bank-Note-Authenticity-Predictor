"""
This Flask application is made to serve 
the classification model as an API &
Test it in local host server @ http://127.0.0.1:5000

Date:- 31-10-2021
Author: Satyabrata Roy

"""

from flask import Flask, request
import pickle

app = Flask(__name__)

try:
    pickle_in = open('classifier.pkl', 'rb')
    classifier = pickle.load(pickle_in)
finally:
    pickle_in.close()

@app.route('/')
def home():
    return 'Welcom to my Flask Application'

@app.route('/predict', methods=['GET'])
def predict():

    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    input_feature_values = [variance, skewness, curtosis, entropy]

    prediction = classifier.predict([input_feature_values])[0]
    prediction_probability = classifier.predict_proba([input_feature_values])[0]


    if prediction == 1:
        result = 'There is {}% chance for the Bank Note to be Original'.format(prediction_probability[1]*100)
    else:
        result = 'There is {}% chance for the Bank Note to be Fake'.format(prediction_probability[0]*100)

    print(f'Input_Feature_Values: {input_feature_values}\nPrediction: {prediction} \
    \nPrediction_Probability: {prediction_probability}\nResult: {result}')

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)