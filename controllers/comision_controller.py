from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import comision_model

comision_model_bp = Blueprint("comision_model", __name__, url_prefix="/comisiones")

@comision_model_bp.route("/")
def listar():
    estado = request.args.get("estado")
    comisiones = comision_model.listar(estado)
    return render_template("comisiones/listar.html", comisiones = comisiones, estado= estado)

@comision_model_bp.route("/<int:comision_id>/pagar", methods=["POST"])
def pagar(comision_id):
    comision_model.marcar_pagada(comision_id)
    flash("Comisión marcada como pagada.")
    return redirect(url_for("comision_model.listar"))