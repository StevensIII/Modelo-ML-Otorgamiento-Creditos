# Logica/conexion.py
import pyodbc

def conectar_bd():
    """
    Conecta a la base de datos SQL Server y devuelve la conexión.
    """
    try:
        conexion = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=LAPTOP-TRDGCHNL\\SQLEXPRESS;'  # Cambia esto por tu servidor
            'DATABASE=MLIAsolicitudes;'            # Cambia esto por tu base de datos
            'UID=admin;'                           # Cambia esto por tu usuario
            'PWD=admin;'                           # Cambia esto por tu contraseña
        )
        print("✅ Conexión a la base de datos exitosa.")
        return conexion
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None