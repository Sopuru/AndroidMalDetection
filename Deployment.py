# serve.py

from flask import Flask, render_template, flash, request, url_for, redirect
from flask import render_template
import os.path
import os
import joblib
import pandas as pd

# creates a Flask application, named app
app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
# a route where we will display a welcome message via an HTML template
@app.route('/', methods=['GET', 'POST'])
def hello():

    message = ""
    result = "Upload an excel file with 7 flow features to get result"
    p1 = "none"
    df = ""
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'backImg.png')
    fe2 = os.path.join(app.config['UPLOAD_FOLDER'], '1.gif')
    if request.method == 'POST':
        p1 = (request.form['data8'])
        df = pd.read_excel(r'.\experiments' + '\\' + p1)

        print(df)
        url1 = df.iloc[0, df.columns.get_loc('F1')]
        url2 = df.iloc[0, df.columns.get_loc('F2')]
        url3 = df.iloc[0, df.columns.get_loc('F3')]
        url4 = df.iloc[0, df.columns.get_loc('F4')]
        url5 = df.iloc[0, df.columns.get_loc('F5')]
        url6 = df.iloc[0, df.columns.get_loc('F6')]
        url7 = df.iloc[0, df.columns.get_loc('F7')]

        url1 = float(url1)
        url2 = float(url2)
        url3 = float(url3)
        url4 = float(url4)
        url5 = float(url5)
        url6 = float(url6)
        url7 = float(url7)
        # feature_array = request.get_json()['dataR']
        # load the model from disk
        X = [[url1], [url2], [url3], [url4], [url5], [url6], [url7]]

        Y = ['Benign', 'Adware', 'Benign', 'Adware', 'Benign', 'Adware', 'Genmal']
        # loaded_model = KNeighborsClassifier(n_neighbors=3)
        loaded_model = joblib.load("RNNFINAL4_model.sav")
        loaded_model.fit(X, Y)

        ynew = loaded_model.predict(X)
        result = ("X=%s, Predicted=%s" % (X[0:7], ynew[0]))
        print(loaded_model.predict_proba([[0.9]]))

        # sending our response object back as json
        # return flask.jsonify(response)

    return render_template('index.html', message=message, result=result, full_filename=full_filename, fe2=fe2, p1=p1,
                         df=df)

# run the application


if __name__ == "__main__":
    app.run(debug=True)

