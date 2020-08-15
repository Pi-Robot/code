# flask server
from flask import Flask
import sys
import pin
import control
import os
app = Flask(__name__)
print(__name__)

filename = "index2_simple.html"

pin.load("config1.json")
control.load("config1.json")

@app.route("/")
def init():       
    with open(filename, "r") as file:
        return file.read()

@app.route("/move/<left>/<right>")
def moveTo(left,right):
    print(left,right)
    control.move(int(left),int(right))         
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
