from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import vendedor_model

vendedor_model_bp = Blueprint("vendedor_model", __name__, url_prefix="/vendedores")

@vendedor_model_bp.route("/")
def listar():
    vendedores = vendedor_model.listar()
    return render_template("vendedores/listar.html", vendedores=vendedores)

@vendedor_model_bp.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo = request.form["correo"]
        vendedor_model.crear(nombre, apellido, correo)
        flash("Vendedor creado correctamente.")
        return redirect(url_for("vendedor_model.listar"))
    return render_template("vendedores/crear.html")

@vendedor_model_bp.route("/<int:vendedor_id>/editar", methods=["GET", "POST"])
def editar(vendedor_id):
    v = vendedor_model.obtener_por_id(vendedor_id)
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        correo = request.form["correo"]
        vendedor_model.editar(vendedor_id, nombre, apellido, correo)
        flash("Vendedor actualizado.")
        return redirect(url_for("vendedor_model.listar"))
    return render_template("vendedores/editar.html", vendedor=v)