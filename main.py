from flask import Flask, render_template_string
import redis
import os
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv('.env.local')

# Initialize Flask application
app = Flask(__name__)

# Get Redis URL from environment variable
redis_url = os.getenv('REDIS_connection_string')

# Connect to Redis using the connection string
redis_client = redis.Redis.from_url(redis_url)


@app.route('/')
def index():
    # Try to get the value of "mykey" from Redis
    value = redis_client.get('mykey')

    # If key does not exist, set a default value
    if value is None:
        value = "Key 'mykey' does not exist in Redis."
    else:
        value = value.decode('utf-8')  # Decode the byte value

    # Render the value in the template
    return render_template_string('<h1>{{ value }}</h1>', value=value)


if __name__ == "__main__":
    # Run the application
    app.run(debug=True)