import numpy as np
from keras.models import model_from_json
from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
import h5py

app = Flask(__name__)
json_file = open('D:\Flask\Customer Churn Flask\model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("D:\Flask\Customer Churn Flask\model.h5")


@app.route('/')
def home():
    print("Hello app")
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    print("Hello")
    #For rendering results on HTML GUI

    int_features = [float(x) for x in request.form.values()]
    print(int_features)
    for i in int_features:
        print("---",i,"-----")
    prediction = loaded_model.predict([int_features])
    print("-------------prediction--------------------",prediction)
    if prediction[0][0]<0.5:
        prediction = "Good Relation Maintained"
    else:
        prediction = "Need to Focus on the Customer"
    return render_template('index.html', prediction_text='{}'.format(prediction))

@app.route('/predict1',methods=['POST'])
def predict1():
    '''
    For direct API calls trought request
    '''
    data = request.files['file']
    cust_df = pd.read_csv(data)
    X = cust_df.iloc[:, 3:13]
    labelencoder_X_1 = LabelEncoder()
    print(X.columns)
    X.Geography = labelencoder_X_1.fit_transform(X.Geography)
    labelencoder_x_2 = LabelEncoder()
    X.Gender = labelencoder_x_2.fit_transform(X.Gender)
    print(X.head())
    prediction = loaded_model.predict(X)
    for l in range(len(prediction)):
        print(prediction[l][0])
        #if prediction[l][0]<0.5:
        #    prediction[l][0] = "Loyal Customer"
        #else:
        #    prediction[l][0] = "Not Loyal"
    l1= list(range(1,100001))

    z1 = zip(l1,prediction)
    print(len(z1))
    print(X.shape)
    for i in z1:
        print(i)
    return render_template('multiple.html',result=z1)

if __name__ == "__main__":
    app.run(debug=True)