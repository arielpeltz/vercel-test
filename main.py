from flask import Flask, render_template_string

# Initialize Flask application
app = Flask(__name__)


@app.route('/')
def index():
    # Render the value in the template
    return render_template_string('<h1>{{ value1 }}</h1>',
                                  value1="Hello World")


if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
