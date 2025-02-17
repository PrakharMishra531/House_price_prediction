from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
data=pd.read_csv('Cleaned_Data.csv')
pipe = pickle.load(open('pipe.pkl', 'rb')) 

@app.route('/')
def home():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations = locations)

@app.route('/predict',methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bathroom')
    sqft = request.form.get('sqft')

    input = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction = pipe.predict(input)[0] * 1e5
    return str(np.round(prediction,2))


if __name__ == '__main__':
    app.run(debug=True)
