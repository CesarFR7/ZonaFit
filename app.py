from flask import Flask

app = Flask(__name__)


@app.route("/")  # url: http://127.0.0.1:5000
def inicio():
    app.logger.debug("Entramos al path de inicio /")
    return "<p>Inicio del proyecto</p>"


if __name__ == "__main__":
    app.run(debug=True)
