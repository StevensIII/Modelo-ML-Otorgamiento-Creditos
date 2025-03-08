# Logica/afiliado_dao.py
from Logica.conexion import conectar_bd  # Importar la función de conexión

def insertar_afiliado(afiliado, estado_solicitud):
    """
    Inserta un afiliado en la base de datos.
    """
    conn = conectar_bd()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        query = """INSERT INTO Afiliado (Nombre, Edad, Ingresos_Anuales, Monto_Prestamo, Puntaje_Credito,
                                         Meses_Empleado, Cantidad_Lineas_Credito, Tasa_Interes_Impuesto,
                                         Duracion_Prestamo_Meses, Relacion_Deuda_Ingresos, Nivel_Educacion,
                                         Estado_Laboral, Estado_Civil, Tiene_Hipoteca, Tiene_Dependientes,
                                         Proposito_Prestamo, Tiene_CoFirmante, Estado_Solicitud)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        cursor.execute(query, (afiliado.nombre, afiliado.edad, afiliado.ingresos_anuales,
                               afiliado.monto_prestamo, afiliado.puntaje_credito, afiliado.meses_empleado,
                               afiliado.cantidad_lineas_credito, afiliado.tasa_interes_impuesto,
                               afiliado.duracion_prestamo_meses, afiliado.relacion_deuda_ingresos,
                               afiliado.nivel_educacion, afiliado.estado_laboral, afiliado.estado_civil,
                               afiliado.tiene_hipoteca, afiliado.tiene_dependientes,
                               afiliado.proposito_prestamo, afiliado.tiene_cofirmante, estado_solicitud))

        conn.commit()
        print("✅ Afiliado registrado con éxito.")
        return True
    except Exception as e:
        print(f"❌ Error al insertar afiliado: {e}")
        return False
    finally:
        conn.close()
