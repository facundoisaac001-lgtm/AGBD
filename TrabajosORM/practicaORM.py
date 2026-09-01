from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine, and_, or_
from sqlalchemy.orm import DeclarativeBase, Session


# 1. MODELO PRODUCTO

class Base(DeclarativeBase):
    pass


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    categoria = Column(String, nullable=True)
    precio = Column(Float, nullable=True)
    stock = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True)


engine = create_engine("sqlite:///tienda.db", echo=True)

Base.metadata.create_all(engine)



# 2. INSERTAR LOS 10 PRODUCTOS


with Session(engine) as session:

    productos_iniciales = [
        Producto(
            nombre="Teclado mecanico",
            categoria="perifericos",
            precio=8500.0,
            stock=15
        ),

        Producto(
            nombre="Mouse inalambrico",
            categoria="perifericos",
            precio=4200.0,
            stock=30
        ),

        Producto(
            nombre="Monitor 24 pulgadas",
            categoria="monitores",
            precio=62000.0,
            stock=8
        ),

        Producto(
            nombre="Auriculares bluetooth",
            categoria="audio",
            precio=12300.0,
            stock=20
        ),

        Producto(
            nombre="Webcam Full HD",
            categoria="perifericos",
            precio=9800.0,
            stock=12
        ),

        Producto(
            nombre="SSD 1TB",
            categoria="almacenamiento",
            precio=18500.0,
            stock=25
        ),

        Producto(
            nombre="RAM 16GB",
            categoria="componentes",
            precio=15600.0,
            stock=18
        ),

        Producto(
            nombre="Mousepad XL",
            categoria="perifericos",
            precio=2100.0,
            stock=40
        ),

        Producto(
            nombre="Hub USB-C",
            categoria="accesorios",
            precio=5400.0,
            stock=6,
            activo=False
        ),

        Producto(
            nombre="Cable HDMI",
            categoria="accesorios",
            precio=1800.0,
            stock=50
        )
    ]

    session.add_all(productos_iniciales)
    session.commit()

    total = session.query(Producto).count()

    print("\n--- EJ 2 ---")
    print(f"Productos insertados: {total}")




with Session(engine) as session:

    
    # 3. PRODUCTOS DE CATEGORIA PERIFERICOS

    print("\n--- EJ 3: Periféricos ---")

    perifericos = session.query(Producto).filter(
        Producto.categoria == "perifericos"
    ).all()

    for p in perifericos:
        print(f"- {p.nombre}: ${p.precio}")


    # 4. PRECIO MAYOR A $10000

    print("\n--- EJ 4: Precio > $10000 ---")

    caros = session.query(Producto).filter(
        Producto.precio > 10000
    ).order_by(
        Producto.precio.desc()
    ).all()

    for p in caros:
        print(f"- {p.nombre}: ${p.precio}")


    # 5. STOCK <= 12 Y ACTIVOS

    print("\n--- EJ 5: Stock <= 12 y Activos ---")

    poco_stock = session.query(Producto).filter(
        Producto.stock <= 12,
        Producto.activo == True
    ).all()

    for p in poco_stock:
        print(f"- {p.nombre} | Stock: {p.stock}")

    print("El Hub USB-C no aparece porque está inactivo.")


    # 6. PRECIO ENTRE $5000 Y $20000

    print("\n--- EJ 6: Precio entre $5000 y $20000 ---")

    rango_precio = session.query(Producto).filter(
        Producto.precio >= 5000
    ).filter(
        Producto.precio <= 20000
    ).all()

    for p in rango_precio:
        print(f"- {p.nombre}: ${p.precio}")


    # 7. PRODUCTO MAS CARO

    print("\n--- EJ 7: Producto más caro ---")

    mas_caro = session.query(Producto).order_by(
        Producto.precio.desc()
    ).first()

    print(f"- {mas_caro.nombre}: ${mas_caro.precio}")


    # 8. PRODUCTOS INACTIVOS

    print("\n--- EJ 8: Productos inactivos ---")

    inactivos = session.query(Producto).filter(
        Producto.activo == False
    ).all()

    for p in inactivos:
        print(f"- {p.nombre}")


    # 9. AUDIO O COMPONENTES

    print("\n--- EJ 9: Audio o Componentes ---")

    audio_comp = session.query(Producto).filter(
        or_(
            Producto.categoria == "audio",
            Producto.categoria == "componentes"
        )
    ).all()

    for p in audio_comp:
        print(f"- {p.nombre} ({p.categoria})")


    # 10. NOMBRE QUE CONTENGA LA LETRA "a"

    print("\n--- EJ 10: Nombres que contienen 'a' ---")

    con_a = session.query(Producto).filter(
        Producto.nombre.contains("a")
    ).all()

    for p in con_a:
        print(f"- {p.nombre}")

    print(f"Cantidad: {len(con_a)}")


    # 11. NOMBRE QUE EMPIECE CON "M"

    print("\n--- EJ 11: Nombres que empiezan con 'M' ---")

    empiezan_m = session.query(Producto).filter(
        Producto.nombre.startswith("M")
    ).all()

    for p in empiezan_m:
        print(f"- {p.nombre}")


    # 12. PRODUCTO SIN CATEGORIA Y SIN PRECIO

    print("\n--- EJ 12: Producto sin categoría ---")

    nuevo_producto = Producto(
        nombre="Producto sin datos",
        categoria=None,
        precio=None,
        stock=10
    )

    session.add(nuevo_producto)
    session.commit()

    sin_categoria = session.query(Producto).filter(
        Producto.categoria == None
    ).all()

    for p in sin_categoria:
        print(f"- {p.nombre}")

    print("\nProductos sin precio:")

    sin_precio = session.query(Producto).filter(
        Producto.precio == None
    ).all()

    for p in sin_precio:
        print(f"- {p.nombre}")

    print("Aparece el mismo producto porque tiene categoria=None y precio=None.")


    # 13. ACTUALIZAR HUB USB-C

    print("\n--- EJ 13: Actualizar Hub USB-C ---")

    hub = session.query(Producto).filter(
        Producto.nombre == "Hub USB-C"
    ).first()

    hub.stock = 20
    hub.activo = True

    session.commit()

    hub_verificado = session.get(Producto, hub.id)

    print(f"- {hub_verificado.nombre}")
    print(f"  Stock: {hub_verificado.stock}")
    print(f"  Activo: {hub_verificado.activo}")


    # 14. AUMENTAR 10% A LOS PERIFERICOS

    print("\n--- EJ 14: Aumento del 10% ---")

    perifericos = session.query(Producto).filter(
        Producto.categoria == "perifericos"
    ).all()

    for p in perifericos:
        p.precio = p.precio * 1.10

    session.commit()

    for p in perifericos:
        print(f"- {p.nombre}: ${p.precio}")

    print("Teclado mecanico después del aumento: $9350")


    # 15. ELIMINAR CABLE HDMI

    print("\n--- EJ 15: Eliminar Cable HDMI ---")

    cable = session.query(Producto).filter(
        Producto.nombre == "Cable HDMI"
    ).first()

    session.delete(cable)
    session.commit()

    total = session.query(Producto).count()

    print(f"Cantidad de productos: {total}")


    # 16. ELIMINAR PRECIO < $2000 O INACTIVOS

    print("\n--- EJ 16: Eliminar productos ---")

    productos_eliminar = session.query(Producto).filter(
        or_(
            Producto.precio < 2000,
            Producto.activo == False
        )
    ).all()

    for p in productos_eliminar:
        print(f"- Eliminando: {p.nombre}")
        session.delete(p)

    cantidad = len(productos_eliminar)

    session.commit()

    print(f"Cantidad de productos borrados: {cantidad}")


    # EXTRA 1.

    print("\n--- EXTRA: Productos con 'USB' ---")

    usb = session.query(Producto).filter(
        Producto.nombre.contains("USB")
    ).all()

    for p in usb:
        print(f"- {p.nombre}")


    # EXTRA 2. 
    

    print("\n--- EXTRA: Ordenados por categoría y precio ---")

    ordenados = session.query(Producto).order_by(
        Producto.categoria,
        Producto.precio
    ).all()

    for p in ordenados:
        print(f"- {p.categoria} | {p.nombre} | ${p.precio}")


    
    # EXTRA 3. 
    

    print("\n--- EXTRA: Productos activos ---")

    activos = session.query(Producto).filter(
        Producto.activo == True
    ).count()

    print(f"Activos: {activos}")


    # EXTRA 4

    print("\n--- EXTRA: Productos inactivos ---")

    inactivos = session.query(Producto).filter(
        Producto.activo == False
    ).count()

    print(f"Inactivos: {inactivos}")