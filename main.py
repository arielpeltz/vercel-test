from flask import Flask, render_template_string
from dotenv import load_dotenv
import redis
import os

load_dotenv('.env.local')

redis = redis.Redis.from_url(os.getenv("redis_connection_string"))


# Initialize Flask application
app = Flask(__name__)


@app.route('/')
def index():
    val = redis.get("headline")

    # Render the value in the template
    return render_template_string('<h1>{{ value1 }}</h1>',
                                  value1=val.decode())


if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
