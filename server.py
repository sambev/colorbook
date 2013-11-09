from flask import Flask
from jconfig import render
app = Flask(__name__)


@app.route('/')
def main():
    return render(upload.html)

if __name__ == '__main__':
    app.run()