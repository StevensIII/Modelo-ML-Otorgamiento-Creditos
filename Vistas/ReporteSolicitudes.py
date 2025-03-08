import tkinter as tk
from tkinter import ttk
import pyodbc

class ReporteSolicitudes:
    def __init__(self, parent):
        self.ventana = tk.Toplevel(parent)  # Crear una nueva ventana
        self.ventana.title("Reporte de Solicitudes de Crédito")
        self.ventana.geometry("1200x400")  # Ajustar el tamaño de la ventana

        # Centrar la ventana en la pantalla
        self.center_window(1200, 400)  # Llamar a la función para centrar la ventana

        # Crear un Frame para contener el Treeview y el Scrollbar
        self.frame = tk.Frame(self.ventana)
        self.frame.pack(fill="both", expand=True)

        # Crear un Treeview para mostrar los datos
        self.tree = ttk.Treeview(self.frame, columns=(
            "ID_Prestamo", "Nombre", "Edad", "Ingresos_Anuales", "Monto_Prestamo", 
            "Puntaje_Credito", "Meses_Empleado", "Cantidad_Lineas_Credito", 
            "Tasa_Interes_Impuesto", "Duracion_Prestamo_Meses", "Relacion_Deuda_Ingresos", 
            "Nivel_Educacion", "Estado_Laboral", "Estado_Civil", "Tiene_Hipoteca", 
            "Tiene_Dependientes", "Proposito_Prestamo", "Tiene_CoFirmante", 
            "Cumplimiento", "Estado_Solicitud"
        ), show="headings")

        # Configurar las columnas
        columnas = [
            ("ID_Prestamo", "ID Prestamo"),
            ("Nombre", "Nombre"),
            ("Edad", "Edad"),
            ("Ingresos_Anuales", "Ingresos Anuales"),
            ("Monto_Prestamo", "Monto Prestamo"),
            ("Puntaje_Credito", "Puntaje Credito"),
            ("Meses_Empleado", "Meses Empleado"),
            ("Cantidad_Lineas_Credito", "Cantidad Lineas Credito"),
            ("Tasa_Interes_Impuesto", "Tasa Interes Impuesto"),
            ("Duracion_Prestamo_Meses", "Duracion Prestamo Meses"),
            ("Relacion_Deuda_Ingresos", "Relacion Deuda Ingresos"),
            ("Nivel_Educacion", "Nivel Educacion"),
            ("Estado_Laboral", "Estado Laboral"),
            ("Estado_Civil", "Estado Civil"),
            ("Tiene_Hipoteca", "Tiene Hipoteca"),
            ("Tiene_Dependientes", "Tiene Dependientes"),
            ("Proposito_Prestamo", "Proposito Prestamo"),
            ("Tiene_CoFirmante", "Tiene CoFirmante"),
            ("Cumplimiento", "Cumplimiento"),
            ("Estado_Solicitud", "Estado Solicitud")
        ]

        for col, heading in columnas:
            self.tree.heading(col, text=heading)
            self.tree.column(col, width=100, anchor="center")

        # Agregar un Scrollbar horizontal
        self.scrollbar_x = ttk.Scrollbar(self.frame, orient="horizontal", command=self.tree.xview)
        self.scrollbar_y = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(xscrollcommand=self.scrollbar_x.set,yscrollcommand=self.scrollbar_y)

        # Empaquetar el Treeview y el Scrollbar
        self.tree.pack(side="top", fill="both", expand=True)
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.scrollbar_y.pack(side="right", fill="y")    # Scrollbar vertical a la derecha

        # Cargar los datos de la base de datos
        self.cargar_datos()

    def center_window(self, width, height):
        """
        Centra la ventana en la pantalla.
        """
        # Obtener las dimensiones de la pantalla
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Establecer la geometría de la ventana
        self.ventana.geometry(f"{width}x{height}+{x}+{y}")

    def cargar_datos(self):
        # Conectar a la base de datos
        conexion = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=LAPTOP-TRDGCHNL\\SQLEXPRESS;'
            'DATABASE=MLIAsolicitudes;'
            'UID=admin;'
            'PWD=admin;'
        )
        cursor = conexion.cursor()

        # Consultar todos los registros de la tabla Afiliado
        cursor.execute("SELECT * FROM Afiliado")
        registros = cursor.fetchall()

        # Insertar los registros en el Treeview
        for registro in registros:
            # Formatear los datos para eliminar comas, comillas, paréntesis, etc.
            valores = [str(valor).strip("()'\"") if valor is not None else "" for valor in registro]
            self.tree.insert("", "end", values=valores)

        # Cerrar la conexión
        conexion.close()