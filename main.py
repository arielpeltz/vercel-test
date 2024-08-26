from flask import Flask, render_template_string
import redis
import os
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv('.env.local')

# Initialize Flask application
app = Flask(__name__)

redis1 = redis.Redis.from_url(os.getenv('REDIS_connection_string'))


def val(client, key):
    value = client.get(key)

    # If key does not exist, set a default value
    if value is None:
        value = f"Key '{key}' does not exist in Redis."
    else:
        value = value.decode('utf-8')  # Decode the byte value

    return value


@app.route('/')
def index():
    print(val(redis1, 'mykey'))

    # Render the value in the template
    return render_template_string('<h1>{{ value1 }}</h1>',
                                  value1=val(redis1, 'headline'))


if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
