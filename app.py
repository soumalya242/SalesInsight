from flask import Flask
from config import Config
from database.db import db

# Create Flask application
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize database
db.init_app(app)


@app.route("/")
def home():
    return "Welcome to SalesInsight Dashboard!"


if __name__ == "__main__":
    app.run(debug=True)