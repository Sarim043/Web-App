from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    """Homepage route displaying welcome message."""
    return render_template('index.html')


@app.route('/hello')
def hello():
    """
    Personalized greeting route.
    Takes a 'name' query parameter and returns a personalized greeting.
    Example: /hello?name=John
    """
    name = request.args.get('name', 'Guest')
    return render_template('hello.html', name=name)


@app.route('/about')
def about():
    """About page route."""
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
