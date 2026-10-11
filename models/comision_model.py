from database import obtener_conexion
from decimal import Decimal

def calcular(monto_venta, porcentaje_fraccion):
    return (Decimal(monto_venta) * Decimal(porcentaje_fraccion)).quantize(Decimal("0.01"))

def crear(venta_id, porcentaje_aplicado, monto_comision):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "Insert into comisiones (venta_id, porcentaje_aplicado, monto_comision) values (%s, %s, %s)",
        (venta_id, porcentaje_aplicado, monto_comision)
    )
    conexion.commit()
    cursor.close()
    conexion.close()
    
def listar(estado=None):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary = True)
    sql = """
        Select comisiones.*,
               ventas.descripcion as venta_descripcion,
               vendedores.nombre as vendedor_nombre,
               vendedores.apellido as vendedor_apellido
        From comisiones
        Join ventas on comisiones.venta_id = ventas.id
        Join vendedores on ventas.vendedor_id = vendedores.id
    """
    parametros = ()
    if estado in ("pendiente", "pagada"):
        sql += " where comisiones.estado = %s"
        parametros = (estado,)
    sql += " order by comisiones.id Desc"
    
    cursor.execute(sql, parametros)
    comisiones = cursor.fetchall()
    cursor.close()
    conexion.close()
    return comisiones
    
def marcar_pagada(comision_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("Update comisiones set estado = 'pagada' where id = %s", (comision_id,))
    conexion.commit()
    cursor.close()
    conexion.close()