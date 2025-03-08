class Afiliado:
    def __init__(self, nombre, edad, ingresos_anuales, monto_prestamo, puntaje_credito,
                 meses_empleado, cantidad_lineas_credito, tasa_interes_impuesto,
                 duracion_prestamo_meses, relacion_deuda_ingresos, nivel_educacion,
                 estado_laboral, estado_civil, tiene_hipoteca, tiene_dependientes,
                 proposito_prestamo, tiene_cofirmante, cumplimiento=None):
        self.nombre = nombre
        self.edad = edad
        self.ingresos_anuales = ingresos_anuales
        self.monto_prestamo = monto_prestamo
        self.puntaje_credito = puntaje_credito
        self.meses_empleado = meses_empleado
        self.cantidad_lineas_credito = cantidad_lineas_credito
        self.tasa_interes_impuesto = tasa_interes_impuesto
        self.duracion_prestamo_meses = duracion_prestamo_meses
        self.relacion_deuda_ingresos = relacion_deuda_ingresos
        self.nivel_educacion = nivel_educacion
        self.estado_laboral = estado_laboral
        self.estado_civil = estado_civil
        self.tiene_hipoteca = tiene_hipoteca
        self.tiene_dependientes = tiene_dependientes
        self.proposito_prestamo = proposito_prestamo
        self.tiene_cofirmante = tiene_cofirmante
        self.cumplimiento = cumplimiento
