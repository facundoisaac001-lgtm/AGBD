from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine, and_, or_
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    categoria = Column(String, nullable=False)

engine = create_engine("sqlite:///tienda.db", echo=True)

Base.metadata.create_all(engine)

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

 # 2. Inserción de los 10 productos iniciales
with Session(engine) as session:
    productos_iniciales = [
        Producto(nombre="Teclado mecanico", categoria="perifericos", precio=8500.0, stock=15),
        Producto(nombre="Mouse inalambrico", categoria="perifericos", precio=4200.0, stock=30),
        Producto(nombre="Monitor 24 pulgadas", categoria="monitores", precio=62000.0, stock=8),
        Producto(nombre="Auriculares bluetooth", categoria="audio", precio=12300.0, stock=20),
        Producto(nombre="Webcam Full HD", categoria="perifericos", precio=9800.0, stock=12),
        Producto(nombre="SSD 1TB", categoria="almacenamiento", precio=18500.0, stock=25),
        Producto(nombre="RAM 16GB", categoria="componentes", precio=15600.0, stock=18),
        Producto(nombre="Mousepad XL", categoria="perifericos", precio=2100.0, stock=40),
        Producto(nombre="Hub USB-C", categoria="accesorios", precio=5400.0, stock=6, activo=False),
        Producto(nombre="Cable HDMI", categoria="accesorios", precio=1800.0, stock=50),
    ]
    session.add_all(productos_iniciales)
    session.commit()

    total = session.query(Producto).count()
    print(f"EJ 2: Productos insertados correctamente. Total en BD: {total}\n")
    # Ejercicios de Consulta (3 a 11)

with Session(engine) as session:
    # 3. Categoría 'perifericos'
    print("--- EJ 3: Periféricos ---")
    perifericos = session.query(Producto).filter(Producto.categoria == "perifericos").all()
    for p in perifericos:
        print(f"- {p.nombre}: ${p.precio}")

    # 4. Precio > $10000 ordenado de mayor a menor
    print("\n--- EJ 4: Precio > $10000 (Mayor a Menor) ---")
    caros = session.query(Producto).filter(Producto.precio > 10000).order_by(Producto.precio.desc()).all()
    for p in caros:
        print(f"- {p.nombre}: ${p.precio}")

    # 5. Stock <= 12 y activos
    print("\n--- EJ 5: Stock <= 12 y Activos ---")
    poco_stock = session.query(Producto).filter(Producto.stock <= 12, Producto.activo == True).all()
    for p in poco_stock:
        print(f"- {p.nombre} (Stock: {p.stock})")
    # RESPUESTA PREGUNTA 5: El Hub USB-C no aparece porque su campo `activo` es False.

    # 6. Precio entre $5000 y $20000
    print("\n--- EJ 6: Precio entre $5000 y $20000 ---")
    rango_precio = session.query(Producto).filter(
        and_(Producto.precio >= 5000, Producto.precio <= 20000)
    ).all()
    for p in rango_precio:
        print(f"- {p.nombre}: ${p.precio}")


    # 7. Producto más caro
    mas_caro = session.query(Producto).order_by(Producto.precio.desc()).first()
    print(f"\n--- EJ 7: Producto más caro --- \n- {mas_caro.nombre}: ${mas_caro.precio}")

    # 8. Productos inactivos
    print("\n--- EJ 8: Productos Inactivos ---")
    inactivos = session.query(Producto).filter(Producto.activo == False).all()
    for p in inactivos:
        print(f"- {p.nombre}")


    # 9. Categoría audio o componentes
    print("\n--- EJ 9: Audio o Componentes ---")
    audio_comp = session.query(Producto).filter(
        or_(Producto.categoria == "audio", Producto.categoria == "componentes")
    ).all()
    for p in audio_comp:
        print(f"- {p.nombre} ({p.categoria})")


    















with Session(engine) as session:
    print("\n--- Productos con precio menor a $500 ---")
    productos_baratos = session.query(Producto)\
                               .filter(Producto.precio < 500)\
                               .all()

    for p in productos_baratos:
        print(f"ID: {p.id} | Nombre: {p.nombre} | Precio: ${p.precio} | Stock: {p.stock} | Categoría: {p.categoria}")