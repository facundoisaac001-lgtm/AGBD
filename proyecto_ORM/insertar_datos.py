from conexion import engine
from modelo import Categoria, Producto, Usuario
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

try:
  # 1. Crear las Categorías
  cat_remeras = Categoria(nombre="Remeras")
  cat_buzos = Categoria(nombre="Buzos")
  cat_pantalones = Categoria(nombre="Pantalones")
  cat_camperas = Categoria(nombre="Camperas")
  cat_accesorios = Categoria(nombre="Accesorios")

  session.add_all([
      cat_remeras,
      cat_buzos,
      cat_pantalones,
      cat_camperas,
      cat_accesorios,
  ])
  session.commit()  # Guardamos para que tengan ID

  # 2. Crear Usuarios
  admin = Usuario(
      nombre="Facundo Admin",
      email="admin@pamilu.com",
      password_hash="admin_hash_123",
      rol="admin",
  )
  cliente = Usuario(
      nombre="Juan Pérez",
      email="juan@gmail.com",
      password_hash="cliente_hash_456",
      telefono="1122334455",
      direccion="Av. Corrientes 1234",
      rol="cliente",
  )
  session.add_all([admin, cliente])

  # 3. Crear Productos (asignando el OBJETIVO de categoría, no un texto)
  productos_pamilu = [
      Producto(
          nombre="Remera Oversize Basic",
          categoria=cat_remeras,
          talle="L",
          color="Negro",
          precio=18500.0,
          stock=20,
          imagen_url="uploads/remera_negra.jpg",
          descripcion="Remera 100% algodón peinado, corte oversize urbano.",
      ),
      Producto(
          nombre="Remera Boxy Fit White",
          categoria=cat_remeras,
          talle="M",
          color="Blanco",
          precio=19000.0,
          stock=15,
          imagen_url="uploads/remera_blanca.jpg",
          descripcion="Remera boxy fit pesada con estampado minimalista.",
      ),
      Producto(
          nombre="Buzo Hoodie Heavyweight",
          categoria=cat_buzos,
          talle="XL",
          color="Gris Topo",
          precio=45000.0,
          stock=10,
          imagen_url="uploads/buzo_gris.jpg",
          descripcion=(
              "Buzo con capucha frizado de alta densidad, super abrigado."
          ),
      ),
      Producto(
          nombre="Buzo Crewneck Vintage",
          categoria=cat_buzos,
          talle="L",
          color="Azul Marino",
          precio=38900.0,
          stock=12,
          imagen_url="uploads/buzo_azul.jpg",
          descripcion="Buzo cuello redondo sin capucha, estilo retro.",
      ),
      Producto(
          nombre="Pantalón Cargo Wide Leg",
          categoria=cat_pantalones,
          talle="42",
          color="Negro",
          precio=52000.0,
          stock=8,
          imagen_url="uploads/pantalon_cargo_negro.jpg",
          descripcion="Pantalón cargo con múltiples bolsillos, corte holgado.",
      ),
      Producto(
          nombre="Pantalón Jogger Streetwear",
          categoria=cat_pantalones,
          talle="40",
          color="Beige",
          precio=42500.0,
          stock=14,
          imagen_url="uploads/jogger_beige.jpg",
          descripcion=(
              "Jogger rústico de algodón con cintura elastizada y puños."
          ),
      ),
  ]

  session.add_all(productos_pamilu)
  session.commit()
  print("¡ÉXITO TOTAL! Categorías, usuarios y productos cargados correctamente.")

except Exception as error:
  session.rollback()
  print("Ocurrió un error al insertar los datos:")
  print(error)

finally:
  session.close()