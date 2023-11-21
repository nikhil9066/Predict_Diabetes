from flask import Flask, render_template, redirect, url_for
from math_utils import *
import plotly.express as px
import random
from pandas.errors import EmptyDataError, ParserError

app = Flask(__name__)

@app.route('/')
def home():
    return "What you want to do"

@app.route('/pdf')
def display_random_data():
    try:
        Newdataframes,_ = df()
        print("-------------------------")
        print(type(Newdataframes))
        random_sample = Newdataframes.sample(n=30, random_state=random.seed())
        random_data = random_sample.values.tolist()
        column_names = random_sample.columns.tolist()
        return render_template('dataframe.html', data=random_data, headers=column_names)
    except Exception as e:
        return render_template('error.html', error_message=str(e))

@app.route('/getinfo')
def index():
    try:
        results_info = getinfo()
        results_model = model()
        combined_results = {**results_info, **results_model}
        return render_template('index.html', results=combined_results)
    except Exception as e:
        return render_template('error.html', error_message=str(e))


if __name__ == '__main__':
    app.run(debug=True, port=8080)