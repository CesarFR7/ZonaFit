from flask import Flask, render_template, redirect, url_for
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


@app.route("/guardar", methods=["POST"])
def guardar():
    # Creamos los objetos de cliente, inicialmente objetos vacíos
    cliente = Cliente()
    cliente_form = ClienteForma(obj=cliente)
    if cliente_form.validate_on_submit():
        # Llenamos el objeto cliente con los valores de formulario
        cliente_form.populate_obj(cliente)
        # Guardamos el nuevo cliente en la BD
        ClienteDAO.insertar(cliente)
    # Redireccionar a la pagína de inicio
    return redirect(url_for("inicio"))


@app.route("/limpiar")
def limpiar():
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)
