from flask import Flask
# from waitress import serve
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello_world():
    return 'Hello, Jaydeep!'

if __name__ == "__main__":
    app.run(debug=True)
    # serve(app, port=5000)