from conexion import engine
from modelo import Categoria, Producto
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

try:
  # Función auxiliar para buscar o crear la categoría si no existe
  def obtener_o_crear_categoria(nombre_cat):
    cat = session.query(Categoria).filter_by(nombre=nombre_cat).first()
    if not cat:
      cat = Categoria(nombre=nombre_cat)
      session.add(cat)
      session.commit()
    return cat

  # Obtenemos las categorías necesarias
  cat_remeras = obtener_o_crear_categoria("Remeras")
  cat_buzos = obtener_o_crear_categoria("Buzos")
  cat_pantalones = obtener_o_crear_categoria("Pantalones")
  cat_camperas = obtener_o_crear_categoria("Camperas")
  cat_calzado = obtener_o_crear_categoria("Calzado")
  cat_accesorios = obtener_o_crear_categoria("Accesorios")

  # Lista de productos reales vinculados a sus categorías correctas
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
          imagen_url="uploads/pantalon_cargo.jpg",
          descripcion="Pantalón cargo con múltiples bolsillos, corte holgado.",
      ),
      Producto(
          nombre="Campera Puffer Oversize",
          categoria=cat_camperas,
          talle="L",
          color="Verde Militar",
          precio=78000.0,
          stock=6,
          imagen_url="uploads/campera_puffer.jpg",
          descripcion="Campera inflable térmica impermeable con bolsillos.",
      ),
      Producto(
          nombre="Zapatillas Urban Chunky",
          categoria=cat_calzado,
          talle="41",
          color="Blanco/Negro",
          precio=65000.0,
          stock=12,
          imagen_url="uploads/zapatillas_chunky.jpg",
          descripcion="Zapatillas estilo urbano con suela chunky de alto confort.",
      ),
      Producto(
          nombre="Gorra Dad Hat Minimal",
          categoria=cat_accesorios,
          talle="Unico",
          color="Negro",
          precio=12500.0,
          stock=25,
          imagen_url="uploads/gorra_negra.jpg",
          descripcion="Gorra gabardina con hebilla metálica ajustable.",
      ),
  ]

  session.add_all(productos_pamilu)
  session.commit()
  print(
      f"¡Se insertaron con éxito {len(productos_pamilu)} productos reales en"
      " Pamilu!"
  )

except Exception as error:
  session.rollback()
  print("Ocurrió un error al insertar los productos:")
  print(error)

finally:
  session.close()