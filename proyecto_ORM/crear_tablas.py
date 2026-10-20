from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text, func
fecha_creacion = Column(DateTime, server_default=func.now())
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# 1. TABLA USUARIOS (Clientes / Admins)
class Usuario(Base):
  __tablename__ = "usuarios"

  id = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(100), nullable=False)
  email = Column(String(100), unique=True, nullable=False)
  password_hash = Column(String(255), nullable=False)  # Contraseña encriptada
  telefono = Column(String(20), nullable=True)
  direccion = Column(String(200), nullable=True)
  rol = Column(String(20), default="cliente")  # 'cliente' o 'admin'
  fecha_registro = Column(DateTime, default=datetime.utcnow)

  # Relación con pedidos
  pedidos = relationship("Pedido", back_populates="usuario")

  def __repr__(self):
    return f"<Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}')>"


# 2. TABLA PRODUCTOS (Ropa: Talles, Colores, Categorías)
class Producto(Base):
  __tablename__ = "productos"

  id = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(100), nullable=False)  # Ej: "Remera Oversize"
  categoria = Column(
      String(50), nullable=False
  )  # Ej: "Remeras", "Pantalones", "Vestidos"
  talle = Column(String(10), nullable=False)  # Ej: "S", "M", "L", "XL", "42"
  color = Column(String(30), nullable=False)  # Ej: "Negro", "Blanco", "Azul"
  precio = Column(Float, nullable=False)  # Ej: 18500.00
  stock = Column(Integer, default=0, nullable=False)  # Cantidad disponible
  imagen_url = Column(
      String(255), nullable=True
  )  # Ruta o enlace de la imagen
  descripcion = Column(Text, nullable=True)
  fecha_creacion = Column(DateTime, default=datetime.utcnow)

  # Relación con ítems de pedidos
  detalles_pedido = relationship("DetallePedido", back_populates="producto")

  def __repr__(self):
    return (
        f"<Producto(nombre='{self.nombre}', talle='{self.talle}',"
        f" color='{self.color}', precio=${self.precio}, stock={self.stock})>"
    )


# 3. TABLA PEDIDOS (Cabecera de la venta)
class Pedido(Base):
  __tablename__ = "pedidos"

  id = Column(Integer, primary_key=True, autoincrement=True)
  usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
  fecha_pedido = Column(DateTime, default=datetime.now)
  estado = Column(
      String(30), default="Pendiente"
  )  # Ej: "Pendiente", "Pagado", "Enviado", "Cancelado"
  total = Column(Float, nullable=False)

  # Relaciones
  usuario = relationship("Usuario", back_populates="pedidos")
  detalles = relationship("DetallePedido", back_populates="pedido")

  def __repr__(self):
    return f"<Pedido(id={self.id}, usuario_id={self.usuario_id}, total=${self.total}, estado='{self.estado}')>"


# 4. TABLA DETALLE DE PEDIDO (Productos comprados en cada pedido)
class DetallePedido(Base):
  __tablename__ = "detalles_pedido"

  id = Column(Integer, primary_key=True, autoincrement=True)
  pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
  producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
  cantidad = Column(Integer, nullable=False, default=1)
  precio_unitario = Column(Float, nullable=False)

  # Relaciones
  pedido = relationship("Pedido", back_populates="detalles")
  producto = relationship("Producto", back_populates="detalles_pedido")

  def __repr__(self):
    return f"<DetallePedido(pedido_id={self.pedido_id}, producto_id={self.producto_id}, cantidad={self.cantidad})>"