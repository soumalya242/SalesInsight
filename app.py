from flask import Flask, render_template
from config import Config
from database.db import db
from database.models import SalesRecord, Upload
from routes.dashboard import dashboard_bp

# Create Flask application
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

#db.init_app(app)
#register dashboard api
app.register_blueprint(dashboard_bp)

# Initialize database
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Welcome to SalesInsight Dashboard!"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/products")
def products():
    return render_template("products.html")



if __name__ == "__main__":
    app.run(debug=True)