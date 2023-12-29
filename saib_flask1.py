from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/flowchart.html")
def sai():
    return render_template("flowchart.html")


if __name__ == "__main__":
    app.run(debug=True)