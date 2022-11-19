
from flask import Flask

app = Flask(__name__)

@app.route("/")
def add(x, y):
    return x + y

def product(x, y=2):
    return x * y

if __name__ == "__main__":
    app.run()

