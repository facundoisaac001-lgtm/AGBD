
from sqlalchemy import create_engine, text

# Datos de la base de datos
USUARIO = "pamilu"
CONTRASENA = "pam123456"
HOST = "10.9.120.5"
PUERTO = 3306
BASE_DATOS = "PAMILU"

# Crear la conexión
from sqlalchemy.engine import URL

url = URL.create(
    drivername="mysql+pymysql",
    username=USUARIO,
    password=CONTRASENA,
    host=HOST,
    port=PUERTO,
    database=BASE_DATOS
)

engine = create_engine(url)

# Probar la conexión
try:
    with engine.connect() as conexion:
        conexion.execute(text("SELECT 1"))
        print("¡Conexión exitosa con PAMILU!")

except Exception as error:
    print("Error al conectar con la base de datos.")
    print(error)
