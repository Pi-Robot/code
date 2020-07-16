# flask server
from flask import Flask
app = Flask(__name__)
print(__name__)

filename = "index1.html"

@app.route("/")
def showIndex():       
    with open(filename, "r") as file:
        return file.read()  

@app.route("/<direction>")
def moveTo(direction):    
    print(direction)    
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
