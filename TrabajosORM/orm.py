from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

# 1. Definimos la base y el modelo Producto con 4 atributos
class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    categoria = Column(String, nullable=False)

# 2. Creación del Engine
# (Desafío) Activamos echo=True para ver el SQL generado en consola
engine = create_engine("sqlite:///tienda.db", echo=True)

# Creamos las tablas en la base de datos
Base.metadata.create_all(engine)

# 3. Insertar 5 productos usando el ORM
with Session(engine) as session:
    productos_iniciales = [
        Producto(nombre="Teclado Mecánico", precio=450.0, stock=15, categoria="Periféricos"),
        Producto(nombre="Mouse Gamer", precio=250.0, stock=30, categoria="Periféricos"),
        Producto(nombre="Monitor 24''", precio=1200.0, stock=8, categoria="Monitores"),
        Producto(nombre="Auriculares Bluetooth", precio=350.0, stock=20, categoria="Audio"),
        Producto(nombre="Silla Ergonómica", precio=850.0, stock=5, categoria="Muebles")
    ]
    
    session.add_all(productos_iniciales)
    session.commit()

# 4. Consultar los productos con precio menor a $500
with Session(engine) as session:
    print("\n--- Productos con precio menor a $500 ---")
    productos_baratos = session.query(Producto)\
                               .filter(Producto.precio < 500)\
                               .all()

    for p in productos_baratos:
        print(f"ID: {p.id} | Nombre: {p.nombre} | Precio: ${p.precio} | Stock: {p.stock} | Categoría: {p.categoria}")