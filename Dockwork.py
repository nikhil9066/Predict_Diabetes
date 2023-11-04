from flask import Flask, render_template
from math_utils import df
import random


app = Flask(__name__)

@app.route('/')
def home():
    return "What you want to do"

@app.route('/pdf')
def display_random_data():
    Newdataframes = df()
    
    # Get a random sample of 30 rows from the DataFrame
    random_sample = Newdataframes.sample(n=30, random_state=random.seed())
    
    # Convert the random sample DataFrame to a list of lists for rendering in the template
    random_data = random_sample.values.tolist()
    
    # Extract column names for the headers
    column_names = random_sample.columns.tolist()
    
    return render_template('dataframe.html', data=random_data, headers=column_names)

@app.route('/getinfo')
def getinfo():
    print()
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080)