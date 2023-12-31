# app.py
from flask import Flask, render_template, redirect, url_for, request
from math_utils import *
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pdf')
def display_random_data():
    try:
        merge_df_all, columns = df()
        random_sample = merge_df_all.sample(n=20, random_state=random.seed())
        random_data = random_sample.values.tolist()
        column_names = random_sample.columns.tolist()
        return render_template('dataframe.html', data=random_data, headers=column_names)
    except Exception as e:
        return render_template('error.html', error_message=str(e))

@app.route('/getinfo')
def index():
    try:
        merge_df_all, _ = df()
        results_info = getinfo(merge_df_all)
        results_model = model()
        trained_model = results_model['model']
        scatter_plot_data = results_model['scatter_plot_data']  # Fix the key to 'scatter_plot_data'
        model_plot_img_base64 = plot_scatter_3d(trained_model, merge_df_all, scatter_plot_data['z'])
        combined_results = {**results_info, 'model_plot_img_base64': model_plot_img_base64, 'scatter_plot_data': scatter_plot_data}
        return render_template('index.html', results=combined_results)
    except Exception as e:
        return render_template('error.html', error_message=str(e)) 
    
#    return render_template('index.html', results=your_results_data)

# Load the model during the startup
trained_model_results = model()
trained_model = trained_model_results['model']

@app.route('/predict', methods=['GET', 'POST'])
def predict_route():
    if request.method == 'POST':
        try:
            # Get user inputs from the form
            obese = float(request.form['obese'])
            inactive = float(request.form['inactive'])

            # Perform prediction using the loaded model
            predicted_diabetic = predict(trained_model, obese, inactive)
            # print("-------------------------------")
            # print(predicted_diabetic)

            # Render the result on the predict.html page
            return render_template('predict.html', predicted_diabetic=predicted_diabetic)
        except Exception as e:
            return render_template('error.html', error_message=str(e))

    # Render the initial form on GET request
    return render_template('predict.html')

# if __name__ == '__main__':
#     app.run(debug=True, port=8080)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
