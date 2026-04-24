from flask import Flask, render_template
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma

app = Flask(__name__)

app.config["SECRET_KEY"] = "llave_secreta"

titulo_app = "Zona Fit (GYM)"


@app.route("/")  # url: http://127.0.0.1:5000
def inicio():
    app.logger.debug("Entramos al path de inicio /")
    # Recuperamos los clientes de la BD
    clientes_db = ClienteDAO.seleccionar()
    # Creamos un objeto de cliente form vacío
    cliente = Cliente()
    cliente_form = ClienteForma(obj=cliente)
    return render_template(
        "index.html", titulo=titulo_app, clientes=clientes_db, forma=cliente_form
    )


if __name__ == "__main__":
    app.run(debug=True)
