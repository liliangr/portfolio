from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def init():
    return render_template('./index.html')



# this allows to start flask using Play button
if __name__ == "__main__":
    app.run(debug=True)
