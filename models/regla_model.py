from database import obtener_conexion

def obtener_aplicable(monto):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary = True)
    cursor.execute(
        "Select * from reglas where monto_minimo <= %s order by monto_minimo desc limit 1",
        (monto,)
    )
    regla = cursor.fetchone()
    cursor.close()
    conexion.close()
    return regla

def listar():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary = True)
    cursor.execute("Select * from reglas order by monto_minimo desc")
    reglas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return reglas