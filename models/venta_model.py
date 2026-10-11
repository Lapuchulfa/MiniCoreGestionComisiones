from database import obtener_conexion

def listar():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary = True)
    cursor.execute("""
        Select ventas.*,
               vendedores.nombre As vendedor_nombre,
               vendedores.apellido as vendedor_apellido
        From ventas
        Join vendedores on ventas.vendedor_id = vendedores.id
        order by ventas.fecha_venta Desc
    """)
    ventas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return ventas

def crear(vendedor_id, descripcion, monto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "Insert into ventas (vendedor_id, descripcion, monto) values (%s, %s, %s)",
        (vendedor_id, descripcion, monto)
    )
    conexion.commit()
    venta_id = cursor.lastrowid
    cursor.close()
    conexion.close()
    return venta_id

def reporte_por_periodo(fecha_inicio, fecha_fin):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary = True)
    cursor.execute("""
        Select vendedores.id as vendedor_id,
               vendedores.nombre,
               vendedores.apellido,
               sum(ventas.monto) as total_ventas
        From ventas
        Join vendedores on ventas.vendedor_id = vendedores.id
        where DATE (ventas.fecha_venta) between %s and %s
        Group by vendedores.id, vendedores.nombre, vendedores.apellido
        Order by vendedores.nombre               
    """, (fecha_inicio, fecha_fin))
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return filas