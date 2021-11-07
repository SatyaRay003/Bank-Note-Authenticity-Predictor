"""
This Flask application is made to serve 
the classification model as an API &
Test it in local host server @ http://127.0.0.1:5000

In this Application, we have integrated the 
basic frontend with our predictor API

We have used Docker to Containerize the Flask Application 
Then Deployed in Heroku Using Heroku Container Registry

The application is available @ 
URL: https://bank-note-authentication-model.herokuapp.com

Date:- 31-10-2021
Author: Satyabrata Roy

"""

from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

try:
    pickle_in = open('classifier.pkl', 'rb')
    classifier = pickle.load(pickle_in)
finally:
    pickle_in.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    input_feature_values = [i for i in request.form.values()]

    prediction = classifier.predict([input_feature_values])[0]
    prediction_probability = classifier.predict_proba([input_feature_values])[0]


    if prediction == 1:
        result = 'There is {}% chance for the Bank Note to be Original'.format(prediction_probability[1]*100)
    else:
        result = 'There is {}% chance for the Bank Note to be Fake'.format(prediction_probability[0]*100)

    print(f'Input_Feature_Values: {input_feature_values}\nPrediction: {prediction} \
    \nPrediction_Probability: {prediction_probability}\nResult: {result}')

    return render_template('index.html', pred='EXpected Result: {}'.format(result))

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=False ,host='0.0.0.0', port=port)