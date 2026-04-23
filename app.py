from flask import Flask, render_template
from cliente_dao import ClienteDAO

app = Flask(__name__)

titulo_app = "Zona Fit (GYM)"


@app.route("/")  # url: http://127.0.0.1:5000
def inicio():
    # Recuperamos los clientes de la BD
    clientes_db = ClienteDAO.seleccionar()
    app.logger.debug("Entramos al path de inicio /")
    return render_template("index.html", titulo=titulo_app, clientes=clientes_db)


if __name__ == "__main__":
    app.run(debug=True)
