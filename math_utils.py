# math_utils.py
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
from plotly.subplots import make_subplots
import plotly.graph_objs as go

# Placeholder for the trained model
trained_model = None

def df():
    excel = pd.ExcelFile("cdc.xlsx")

    sheet_names = excel.sheet_names
    dataframes = []

    for sheet_name in sheet_names:
        df = excel.parse(sheet_name)
        dataframes.append(df)

    df_d, df_o, df_i = dataframes[0], dataframes[1], dataframes[2]

    df_d.drop(columns=["YEAR", "COUNTY", "STATEW"], inplace=True)
    merge_df_do = pd.merge(df_d, df_o, on='FIPS', how='inner')
    merge_df_do.drop(columns=["YEAR", "COUNTY", "STATE"], inplace=True)

    de_new_f = df_i.rename(columns={'FIPDS': 'FIPS'})

    merge_df_all = pd.merge(merge_df_do, de_new_f, on='FIPS', how='inner')
    merge_df_all.drop(columns=["YEAR", "COUNTY", "STATE"], inplace=True)
    return merge_df_all, merge_df_all.columns.tolist()

def getinfo(merge_df_all):
    columns = merge_df_all.columns.tolist()
    matplotlib.use('agg')
    plt.ioff()

    # Pair plot
    pairplot_img = io.BytesIO()
    sns.pairplot(merge_df_all.iloc[:, -3:])
    plt.savefig(pairplot_img, format='png')
    plt.close()
    pairplot_img_base64 = base64.b64encode(pairplot_img.getvalue()).decode('utf-8')
    matplotlib.use(matplotlib.get_backend())

    # Histograms
    hist_plots_img = io.BytesIO()
    fig, ax = plt.subplots(1, len(columns), figsize=(15, 5))

    for i in range(len(columns)):
        sns.histplot(merge_df_all[columns[i]], ax=ax[i], kde=True)

    plt.tight_layout()
    plt.savefig(hist_plots_img, format='png')
    plt.close()

    hist_plots_img_base64 = base64.b64encode(hist_plots_img.getvalue()).decode('utf-8')

    # Skewness
    skewness_table_img = io.BytesIO()
    skewness = merge_df_all.iloc[:, -3:].skew()
    skewness_df = skewness.to_frame().reset_index()     

    # Convert skewness table to HTML and write to BytesIO
    skewness_table_img.write(skewness_df.to_html(index=False, justify='center', classes='table table-bordered table-condensed table-striped').encode('utf-8'))
    skewness_table_img.seek(0)
    skewness_table_html = skewness_table_img.read().decode('utf-8')  # Convert BytesIO to string

    # Correlation Matrix
    correlation_matrix_table_img = io.BytesIO()
    correlation_matrix = merge_df_all.iloc[:, -3:].corr()

    # Convert correlation matrix table to HTML and write to BytesIO
    correlation_matrix_table_img.write(correlation_matrix.to_html(index=True, justify='center', classes='table table-bordered table-condensed table-striped').encode('utf-8'))
    correlation_matrix_table_img.seek(0)
    correlation_matrix_table_img_base64 = base64.b64encode(correlation_matrix_table_img.read()).decode('utf-8')

    # Heat map
    corr_matrix_heatmap_img = io.BytesIO()
    axis_corr = sns.heatmap(correlation_matrix, vmin=-1, vmax=1, center=0, annot=True, annot_kws={'size': 12})
    cbar = axis_corr.collections[0].colorbar
    cbar.ax.tick_params(labelsize=12)
    plt.savefig(corr_matrix_heatmap_img, format='png')
    plt.close()
    corr_matrix_heatmap_img_base64 = base64.b64encode(corr_matrix_heatmap_img.getvalue()).decode('utf-8')

    return {
        'pairplot_img_base64': pairplot_img_base64,
        'hist_plots_img_base64': hist_plots_img_base64,
        'skewness_table_html': skewness_table_html,
        'corr_matrix_heatmap_img_base64': corr_matrix_heatmap_img_base64,
        'data_table': skewness_df.to_html(index=False, justify='center', classes='table table-bordered table-condensed table-striped'),
        'correlation_matrix_table': correlation_matrix.to_html(index=True, justify='center', classes='table table-bordered table-condensed table-striped'),
        'summary_stats': merge_df_all.describe().to_html(classes='table table-bordered table-condensed table-striped')
    }


def model():
    merge_df_all, columns = df()

    X = merge_df_all[['% OBESE', '% INACTIVE']]
    y = merge_df_all[['% DIABETIC']]    

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   

    model = LinearRegression()
    model.fit(X_train, y_train)  

    y_predict = model.predict(X_test)  

    scatter_plot_data = {
        'x': X_test['% OBESE'].tolist(),
        'y': X_test['% INACTIVE'].tolist(),
        'z': y_test['% DIABETIC'].tolist(),
    }

    return {
        'model': model,
        'scatter_plot_data': scatter_plot_data,
    }


def plot_scatter_3d(model, merge_df_all, z_data):
    X_test = merge_df_all[['% OBESE', '% INACTIVE']]
    
    # Predict the values using the trained model
    y_predict = model.predict(X_test)

    # Create 3D scatter plot
    trace_actual = go.Scatter3d(
        x=X_test['% OBESE'],
        y=X_test['% INACTIVE'],
        z=z_data,
        mode='markers',
        marker=dict(size=5, color='blue'),
        name='Actual Data'
    )

    trace_predict = go.Scatter3d(
        x=X_test['% OBESE'],
        y=X_test['% INACTIVE'],
        z=y_predict,
        mode='markers',
        marker=dict(size=5, color='red'),
        name='Predicted Values'
    )

    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
    fig.add_trace(trace_actual)
    fig.add_trace(trace_predict)

    fig.update_layout(
        scene=dict(
            xaxis=dict(title='% OBESE'),
            yaxis=dict(title='% INACTIVE'),
            zaxis=dict(title='% DIABETIC'),
        ),
        title='Scatter Plot with Multilinear Regression',
        showlegend=True,
    )

    # Convert the plot to base64 string
    model_plot_img_base64 = fig.to_image(format='png')
    model_plot_img_base64 = base64.b64encode(model_plot_img_base64).decode('utf-8')

    return model_plot_img_base64

def predict(model, obese, inactive):
    # Placeholder for prediction logic
    # You should use the provided model to make predictions based on the input features
    # Replace the following line with the actual prediction code
    predicted_diabetic = model.predict([[obese, inactive]])[0]
    print(predicted_diabetic)
    return predicted_diabetic


# # Load the model during the startup
# trained_model_results = model()
# trained_model = trained_model_results['model']

# # Print the predicted value for the initial values (12, 34)
# initial_obese = 12
# initial_inactive = 34
# predicted_diabetic_initial = predict_diabetic(trained_model, initial_obese, initial_inactive)
# print(f"Predicted diabetic value for (12, 34): {predicted_diabetic_initial}")


# Uncomment the following lines to test the functions
# df()
# getinfo()
# model()
# predict()

trained_model_results = model()
trained_model = trained_model_results['model']
predicted_diabetic = predict(trained_model, 12, 34)