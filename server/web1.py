# flask server
from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route("/")
def showIndex():
    return "INDEX"

if __name__ == "__main__":
    app.run()
