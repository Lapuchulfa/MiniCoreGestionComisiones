from flask import Flask
from config import config
from flask import redirect, url_for
from controllers.vendedor_controller import vendedor_model_bp
from controllers.venta_controller import venta_model_bp
from controllers.comision_controller import comision_model_bp
from controllers.regla_controller import regla_model_bp


app= Flask(__name__, template_folder="views")
app.secret_key = config.SECRET_KEY

app.register_blueprint(vendedor_model_bp)
app.register_blueprint(venta_model_bp)
app.register_blueprint(comision_model_bp)
app.register_blueprint(regla_model_bp)

@app.route("/")
def inicio():
    return redirect(url_for("vendedor_model.listar"))


if __name__ == '__main__': 
    app.run(debug=True)

