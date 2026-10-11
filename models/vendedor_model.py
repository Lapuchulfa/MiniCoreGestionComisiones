from database import obtener_conexion

def listar():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary = True)
    cursor.execute("Select * from vendedores order by nombre")
    vendedores = cursor.fetchall()
    cursor.close()
    conexion.close()
    return vendedores


def obtener_por_id(vendedor_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary = True)
    cursor.execute("Select * from vendedores where id = %s", (vendedor_id,))
    vendedor = cursor.fetchone()
    cursor.close()
    conexion.close()
    return vendedor

def crear(nombre, apellido, correo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "Insert into vendedores (nombre, apellido, correo) values (%s, %s, %s)",
        (nombre, apellido, correo)
    )
    conexion.commit()
    nuevo_id = cursor.lastrowid # en esta parte nos da la id que MySQL asino automaticamente a la fila que insertamos
    cursor.close()
    conexion.close()
    return nuevo_id

def editar(vendedor_id, nombre, apellido, correo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "Update vendedores set nombre = %s, apellido = %s, correo = %s where id = %s",
        (nombre, apellido, correo, vendedor_id)
    )
    conexion.commit()
    cursor.close()
    conexion.close()
    