from flask import Blueprint, render_template
from models import regla_model

regla_model_bp = Blueprint("regla_model", __name__, url_prefix="/reglas")

@regla_model_bp.route("/")
def listar():
    reglas = regla_model.listar()
    return render_template("reglas/listar.html", reglas = reglas)