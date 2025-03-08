import joblib
import numpy as np
import pandas as pd

# Cargar modelo y columnas usadas en el entrenamiento
modelo = joblib.load("Modelo/modelo_lightgbm_tunado.joblib")
columnas_modelo = joblib.load("Modelo/columnas_modelo.joblib")  # Cargar las columnas usadas en el modelo

def predecir_aprobacion(datos_afiliado):
    try:
        # Convertir los datos en un DataFrame
        df = pd.DataFrame([datos_afiliado])

        # Asegurar que tenga las mismas columnas que el modelo espera
        df = df.reindex(columns=columnas_modelo, fill_value=0)

        # Convertir a NumPy array y predecir
        datos_np = df.to_numpy()
        prediccion = modelo.predict(datos_np)[0]

        return "SI" if prediccion == 0 else "NO"
    except Exception as e:
        print(f"❌ Error en la predicción: {e}")
        return None
