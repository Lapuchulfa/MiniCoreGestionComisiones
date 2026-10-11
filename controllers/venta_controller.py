from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import venta_model, vendedor_model, regla_model, comision_model

venta_model_bp = Blueprint("venta_model", __name__, url_prefix="/ventas") # url_prefix añade ese pedazo de URL a toda las rutas del blueprint  

@venta_model_bp.route("/")
def listar():
    ventas = venta_model.listar()
    return render_template("ventas/listar.html", ventas = ventas)

@venta_model_bp.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        vendedor_id = request.form["vendedor_id"]
        descripcion = request.form["descripcion"]
        monto = request.form["monto"]
        venta_id = venta_model.crear(vendedor_id, descripcion, monto)
        
        regla_aplicable = regla_model.obtener_aplicable(monto)
        if regla_aplicable:
            monto_comision = comision_model.calcular(monto, regla_aplicable["porcentaje_comision"])
            comision_model.crear(venta_id, regla_aplicable["porcentaje_comision"], monto_comision)
            flash(f"Venta registrada. Comisión generada: ${monto_comision}")
        else:
            flash("Venta registrada. No alcanza ningun tramo de comisión.")
            
        return redirect(url_for("venta_model.listar"))
    
    vendedores = vendedor_model.listar()
    return render_template("ventas/crear.html", vendedores = vendedores)


@venta_model_bp.route("/reporte")
def reporte():
    fecha_inicio = request.args.get("fecha_inicio")
    fecha_fin = request.args.get("fecha_fin")
    
    filas = []
    error = False
    
    if fecha_inicio and fecha_fin:
        if fecha_inicio > fecha_fin:
            flash("La fecha inicio debe suceder no puede ser posterior a la fehca fin.")
            error = True
        else:
            resultados = venta_model.reporte_por_periodo(fecha_inicio, fecha_fin)
            for fila in resultados:
                regla_aplicable = regla_model.obtener_aplicable(fila["total_ventas"])
                if regla_aplicable:
                    porcentaje = regla_aplicable["porcentaje_comision"]
                    monto_comision = comision_model.calcular(fila["total_ventas"], porcentaje)
                else:
                    porcentaje = 0
                    monto_comision = 0
                filas.append({
                    "vendedor_nombre": f"{fila['nombre']} {fila['apellido']}",
                    "total_ventas": fila["total_ventas"],
                    "porcentaje_comision": porcentaje,
                    "monto_comision": monto_comision,
                })
    return render_template(
        "ventas/reporte.html",
        filas =filas,
        fecha_inicio = fecha_inicio,
        fecha_fin = fecha_fin,
        error=error,
    )