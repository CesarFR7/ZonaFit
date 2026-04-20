from flask import Flask, render_template

app = Flask(__name__)

titulo_app = "Zona Fit (GYM)"


@app.route("/")  # url: http://127.0.0.1:5000
def inicio():
    app.logger.debug("Entramos al path de inicio /")
    return render_template("index.html", titulo=titulo_app)


if __name__ == "__main__":
    app.run(debug=True)
