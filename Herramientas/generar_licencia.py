from cryptography.fernet import Fernet

def generar_clave():
    # Generar una clave única
    clave = Fernet.generate_key()
    return clave.decode()

if __name__ == "__main__":
    # Generar y mostrar la clave
    clave_generada = generar_clave()
    print("Clave de licencia generada:", clave_generada)