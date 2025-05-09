
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
        return 'Hello, From DevOps'

    # Run the application
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

