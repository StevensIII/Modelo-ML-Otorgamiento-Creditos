# Vistas/solicitud_credito.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Clases.afiliado import Afiliado  # Importar la clase Afiliado
from Modelo.modelo_ml import predecir_aprobacion  # Importar la función de predicción
from Logica.afiliado_dao import insertar_afiliado  # Importar la función para guardar en la base de datos
from Vistas.ReporteSolicitudes import ReporteSolicitudes

class SolicitudCredito:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Solicitud de Crédito")
        self.ventana.geometry("400x500")

        # Centrar la ventana en la pantalla
        self.center_window(400, 500)  # Llamar a la función para centrar la ventana

        # Variables
        self.resultado = tk.StringVar()

        # Crear la interfaz gráfica
        self.crear_interfaz()

    def center_window(self, width, height):
        # Obtener las dimensiones de la pantalla
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Establecer la geometría de la ventana
        self.ventana.geometry(f'{width}x{height}+{x}+{y}')

    def crear_interfaz(self):
        # Nombre
        tk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.grid(row=0, column=1)

        # Edad
        tk.Label(self.ventana, text="Edad:").grid(row=1, column=0)
        self.entry_edad = tk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(self.validar_numero_entero), "%P"))
        self.entry_edad.grid(row=1, column=1)

        # Ingresos Anuales
        tk.Label(self.ventana, text="Ingresos Anuales:").grid(row=2, column=0)
        self.entry_ingresos_anuales = tk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(self.validar_numero_decimal), "%P"))
        self.entry_ingresos_anuales.grid(row=2, column=1)

        # Monto del Préstamo
        tk.Label(self.ventana, text="Monto del Préstamo:").grid(row=3, column=0)
        self.entry_monto_prestamo = tk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(self.validar_numero_decimal), "%P"))
        self.entry_monto_prestamo.grid(row=3, column=1)
        self.entry_monto_prestamo.bind("<KeyRelease>", lambda event: self.calcular_relacion_deuda_ingresos())

        # Puntaje de Crédito
        tk.Label(self.ventana, text="Puntaje de Crédito:").grid(row=4, column=0)
        self.entry_puntaje_credito = tk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(self.validar_numero_decimal), "%P"))
        self.entry_puntaje_credito.grid(row=4, column=1)

        # Meses Empleado
        tk.Label(self.ventana, text="Meses Empleado:").grid(row=5, column=0)
        self.entry_meses_empleado = tk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(self.validar_numero_entero), "%P"))
        self.entry_meses_empleado.grid(row=5, column=1)

        # Cantidad de Líneas de Crédito
        tk.Label(self.ventana, text="Cantidad de Líneas de Crédito:").grid(row=6, column=0)
        self.entry_cantidad_lineas_credito = tk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(self.validar_numero_entero), "%P"))
        self.entry_cantidad_lineas_credito.grid(row=6, column=1)

        # Tasa de Interés e Impuesto
        tk.Label(self.ventana, text="Tasa de Interés e Impuesto:").grid(row=7, column=0)
        self.entry_tasa_interes_impuesto = tk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(self.validar_numero_decimal), "%P"))
        self.entry_tasa_interes_impuesto.grid(row=7, column=1)

        # Duración del Préstamo en Meses
        tk.Label(self.ventana, text="Duración del Préstamo en Meses:").grid(row=8, column=0)
        self.entry_duracion_prestamo_meses = tk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(self.validar_numero_entero), "%P"))
        self.entry_duracion_prestamo_meses.grid(row=8, column=1)

        # Relación Deuda-Ingresos
        tk.Label(self.ventana, text="Relación Deuda-Ingresos:").grid(row=9, column=0)
        self.entry_relacion_deuda_ingresos = tk.Entry(self.ventana, textvariable=self.resultado, state='readonly')
        self.entry_relacion_deuda_ingresos.grid(row=9, column=1)





        # Vincular la función a los eventos KeyRelease de los campos relevantes
        self.entry_ingresos_anuales.bind("<KeyRelease>", lambda event: self.calcular_relacion_deuda_ingresos())
        self.entry_monto_prestamo.bind("<KeyRelease>", lambda event: self.calcular_relacion_deuda_ingresos())
        self.entry_duracion_prestamo_meses.bind("<KeyRelease>", lambda event: self.calcular_relacion_deuda_ingresos())
        self.entry_tasa_interes_impuesto.bind("<KeyRelease>", lambda event: self.calcular_relacion_deuda_ingresos())




        '''
        # Comboboxes
        self.combo_nivel_educacion = self.crear_combobox("Nivel de Educación:", 10, ["Licenciatura", "Preparatoria", "Maestría", "Doctorado"])
        self.combo_estado_laboral = self.crear_combobox("Estado Laboral:", 11, ["Tiempo Completo", "Desempleado", "Autónomo", "Tiempo Parcial"])
        self.combo_estado_civil = self.crear_combobox("Estado Civil:", 12, ["Divorciado", "Casado", "Soltero"])
        self.combo_tiene_hipoteca = self.crear_combobox("Tiene Hipoteca:", 13, ["Si", "No"])
        self.combo_tiene_dependientes = self.crear_combobox("Tiene Dependientes:", 14, ["Si", "No"])
        self.combo_proposito_prestamo = self.crear_combobox("Propósito del Préstamo:", 15, ["Otro", "Automóvil", "Negocio", "Casa", "Educación"])
        self.combo_tiene_cofirmante = self.crear_combobox("Tiene Co-Firmante:", 16, ["Si", "No"])
        '''
        
        # Comboboxes
        self.combo_nivel_educacion = self.crear_combobox("Nivel de Educación:", 10, ["Bachelor's", "Master's", 'High School', 'PhD'])
        self.combo_estado_laboral = self.crear_combobox("Estado Laboral:", 11, ['Full-time', 'Unemployed', 'Self-employed', 'Part-time'])
        self.combo_estado_civil = self.crear_combobox("Estado Civil:", 12, ['Divorced', 'Married', 'Single'])
        self.combo_tiene_hipoteca = self.crear_combobox("Tiene Hipoteca:", 13, ["Yes", "No"])
        self.combo_tiene_dependientes = self.crear_combobox("Tiene Dependientes:", 14, ["Yes", "No"])
        self.combo_proposito_prestamo = self.crear_combobox("Propósito del Préstamo:", 15, ['Other', 'Auto', 'Business', 'Home', 'Education'])
        self.combo_tiene_cofirmante = self.crear_combobox("Tiene Co-Firmante:", 16, ["Yes", "No"])


        # Botón de Enviar
        tk.Button(self.ventana, text="Enviar Solicitud", command=self.enviar_solicitud).grid(row=17, column=0, columnspan=2)

        # Botón para abrir el reporte de solicitudes
        tk.Button(self.ventana, text="Ver Reporte de Solicitudes", command=self.abrir_reporte).grid(row=18, column=0, columnspan=2, pady=10)

    def abrir_reporte(self):
        # Abrir la ventana de reporte
        ReporteSolicitudes(self.ventana)

    def crear_combobox(self, texto, fila, opciones):
        tk.Label(self.ventana, text=texto).grid(row=fila, column=0)
        combo = ttk.Combobox(self.ventana, values=opciones, state="readonly")
        combo.grid(row=fila, column=1)
        return combo

    def validar_numero_entero(self, text):
        return text.isdigit()

    def validar_numero_decimal(self, text):
            if text.count(".") > 1:
                return False
            partes = text.split(".")
            if len(partes) == 1:
                return partes[0].isdigit()
            return partes[0].isdigit() and partes[1].isdigit()
    
    
    def calcular_relacion_deuda_ingresos(self):
        try:
            # Obtener los valores de ingresos anuales, monto del préstamo, duración del préstamo en meses y tasa de interés
            ingresos = self.entry_ingresos_anuales.get()
            monto = self.entry_monto_prestamo.get()
            duracion_meses = self.entry_duracion_prestamo_meses.get()
            tasa_interes_entero = self.entry_tasa_interes_impuesto.get()

            # Verificar si todos los campos están llenos
            if not ingresos or not monto or not duracion_meses or not tasa_interes_entero:
                self.resultado.set("")  # Limpiar el campo de la relación si algún campo está vacío
                return

            # Convertir los valores a números
            ingresos = float(ingresos)
            monto = float(monto)
            duracion_meses = float(duracion_meses)
            tasa_interes_entero = float(tasa_interes_entero)

            # Convertir la tasa de interés de entero a porcentaje decimal
            tasa_interes_anual = tasa_interes_entero / 10000  # Convertir a porcentaje (1813 -> 18.13%)
            tasa_interes_mensual = tasa_interes_anual / 12    # Convertir a tasa mensual

            # Calcular el pago mensual usando la fórmula de amortización
            if duracion_meses != 0 and tasa_interes_mensual != 0:  # Evitar división por cero
                pago_mensual = (monto * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual) ** (-duracion_meses))
            else:
                self.resultado.set("Error: Duración o tasa de interés no pueden ser 0")
                return

            # Calcular la Relación Deuda-Ingresos (DTI) como un porcentaje
            if ingresos != 0:  # Evitar división por cero
                dti = (pago_mensual * 12 / ingresos) * 100
                self.resultado.set(f"{int(dti)}")  # Mostrar el resultado como un entero
            else:
                self.resultado.set("Error: Ingresos no pueden ser 0")
        except ValueError:
            self.resultado.set("Error")

    def validar_campos(self):
        campos = [self.entry_nombre.get(), self.entry_edad.get(), self.entry_ingresos_anuales.get(),
                  self.entry_monto_prestamo.get(), self.entry_puntaje_credito.get(), self.entry_meses_empleado.get(),
                  self.entry_cantidad_lineas_credito.get(), self.entry_tasa_interes_impuesto.get(),
                  self.entry_duracion_prestamo_meses.get(), self.combo_nivel_educacion.get(),
                  self.combo_estado_laboral.get(), self.combo_estado_civil.get(), self.combo_tiene_hipoteca.get(),
                  self.combo_tiene_dependientes.get(), self.combo_proposito_prestamo.get(),
                  self.combo_tiene_cofirmante.get()]
        if "" in campos:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return False
        return True

    def enviar_solicitud(self):
        if self.validar_campos():
            # Crear una instancia de Afiliado con los datos del formulario
            afiliado = Afiliado(
                nombre=self.entry_nombre.get(),
                edad=int(self.entry_edad.get()),
                ingresos_anuales=float(self.entry_ingresos_anuales.get()),
                monto_prestamo=float(self.entry_monto_prestamo.get()),
                puntaje_credito=float(self.entry_puntaje_credito.get()),
                meses_empleado=int(self.entry_meses_empleado.get()),
                cantidad_lineas_credito=int(self.entry_cantidad_lineas_credito.get()),
                tasa_interes_impuesto=float(self.entry_tasa_interes_impuesto.get()),
                duracion_prestamo_meses=int(self.entry_duracion_prestamo_meses.get()),
                relacion_deuda_ingresos=float(self.resultado.get()),
                nivel_educacion=self.combo_nivel_educacion.get(),
                estado_laboral=self.combo_estado_laboral.get(),
                estado_civil=self.combo_estado_civil.get(),
                tiene_hipoteca=self.combo_tiene_hipoteca.get(),
                tiene_dependientes=self.combo_tiene_dependientes.get(),
                proposito_prestamo=self.combo_proposito_prestamo.get(),
                tiene_cofirmante=self.combo_tiene_cofirmante.get()
            )

            # Hacer la predicción con el modelo de machine learning
            datos_para_modelo = [
                afiliado.edad,
                afiliado.ingresos_anuales,
                afiliado.monto_prestamo,
                afiliado.puntaje_credito,
                afiliado.meses_empleado,
                afiliado.cantidad_lineas_credito,
                afiliado.tasa_interes_impuesto,
                afiliado.duracion_prestamo_meses,
                afiliado.relacion_deuda_ingresos,
                afiliado.nivel_educacion,
                afiliado.estado_laboral,
                afiliado.estado_civil,
                afiliado.tiene_hipoteca,
                afiliado.tiene_dependientes,
                afiliado.proposito_prestamo,
                afiliado.tiene_cofirmante,
                # Aquí debes convertir las variables categóricas a numéricas si es necesario
            ]

            aprobado = predecir_aprobacion(datos_para_modelo)

            # Convertir el resultado de la predicción a "SI" o "NO"
            estado_solicitud = "SI" if aprobado else "NO"

            # Guardar el afiliado en la base de datos
            insertar_afiliado(afiliado,estado_solicitud)

            # Mostrar el resultado de la predicción
            if aprobado:
                messagebox.showinfo("Éxito", "Solicitud aprobada")
            else:
                messagebox.showinfo("Denegado", "Solicitud denegada")

    def mainloop(self):
        self.ventana.mainloop()