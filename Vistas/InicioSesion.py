# InicioSesion.py
import tkinter as tk
from tkinter import messagebox
import pyodbc
from Vistas.solicitud_credito import SolicitudCredito  # Importar la ventana de solicitud de crédito

# Configuración de la conexión a SQL Server
conexion = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=LAPTOP-TRDGCHNL\\SQLEXPRESS;'
    'DATABASE=MLIAsolicitudes;'
    'UID=admin;'
    'PWD=admin;'
)
cursor = conexion.cursor()

def center_window(window, width, height):
    # Obtener las dimensiones de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular la posición x e y para centrar la ventana
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Establecer la geometría de la ventana
    window.geometry(f'{width}x{height}+{x}+{y}')

def verificar_credenciales():
    usuario = entry_usuario.get()
    clave = entry_clave.get()

    # Consulta a la base de datos
    cursor.execute("SELECT * FROM Usuarios WHERE Nombre_Usuario = ? AND Clave = ?", (usuario, clave))
    resultado = cursor.fetchone()

    if resultado:
        messagebox.showinfo("Inicio de sesión", "Acceso concedido")
        ventana.destroy()  # Cerrar la ventana de inicio de sesión
        abrir_solicitud_credito()  # Abrir la ventana de solicitud de crédito
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def abrir_solicitud_credito():
    # Crear una instancia de la ventana de solicitud de crédito
    ventana_solicitud = SolicitudCredito()
    ventana_solicitud.mainloop()

# Creación de la ventana de inicio de sesión
ventana = tk.Tk()
ventana.title("Inicio de sesión")
#ventana.geometry("300x200")

# Establecer el tamaño de la ventana de inicio de sesión
window_width = 300
window_height = 200
center_window(ventana, window_width, window_height)  # Centrar la ventana

tk.Label(ventana, text="Usuario:").pack()
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

tk.Label(ventana, text="Contraseña:").pack()
entry_clave = tk.Entry(ventana, show="*")
entry_clave.pack()

tk.Button(ventana, text="Ingresar", command=verificar_credenciales).pack(pady=10)

# Permitir que main.py acceda a la ventana
if __name__ == "__main__":
    ventana.mainloop()