# main.py
import sys
import os
from tkinter import Tk, Label, Entry, Button, messagebox
from config import LICENCIA_VALIDA

# Agregar la ruta del proyecto al sys.path
ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ruta_proyecto)

from Vistas.InicioSesion import ventana  # Importar la ventana de inicio de sesión

def validar_licencia(clave_ingresada):
    """
    Función para validar la clave de lic.
    """
    return clave_ingresada == LICENCIA_VALIDA

def centrar_ventana(ventana):
    """
    Centra una ventana de Tkinter en la pantalla.
    """
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"+{x}+{y}")

def mostrar_ventana_licencia():
    """
    Muestra una ventana para que el usuario ingrese su clave de licencia.
    """
    def on_validar_click():
        clave_usuario = entrada_clave.get()  # Obtener la clave ingresada
        if validar_licencia(clave_usuario):
            ventana_licencia.destroy()  # Cerrar la ventana de validación
            ventana.deiconify()  # Mostrar la ventana de inicio de sesión
        else:
            messagebox.showerror("Error", "Licencia inválida. Saliendo...")
            ventana_licencia.destroy()  # Cerrar la ventana de validación
            sys.exit()  # Salir de la aplicación

    # Crear la ventana de validación de licencia
    ventana_licencia = Tk()
    ventana_licencia.title("Validación de Licencia")

    # Etiqueta y campo de entrada para la clave
    Label(ventana_licencia, text="Ingrese su clave de licencia:").pack(pady=10)
    entrada_clave = Entry(ventana_licencia, width=40)
    entrada_clave.pack(pady=10)

    # Botón para validar
    Button(ventana_licencia, text="Validar", command=on_validar_click).pack(pady=20)

    # Centrar la ventana en la pantalla
    centrar_ventana(ventana_licencia)

    # Iniciar el bucle de la ventana
    ventana_licencia.mainloop()

if __name__ == "__main__":
    # Ocultar la ventana de inicio de sesión inicialmente
    ventana.withdraw()

    # Mostrar la ventana de validación de licencia
    mostrar_ventana_licencia()