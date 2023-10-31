from flask import Flask

# Create a Flask web server
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello():
    # Return "Hello, World!" as the response
    return 'Hello, World!'

# Run the Flask app if this script is executed
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=000)
