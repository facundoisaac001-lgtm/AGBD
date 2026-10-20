from datetime import datetime
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# 1. TABLA USUARIOS
class Usuario(Base):
  __tablename__ = "usuarios"

  id = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(100), nullable=False)
  email = Column(String(100), unique=True, nullable=False)
  password_hash = Column(String(255), nullable=False)
  telefono = Column(String(20), nullable=True)
  direccion = Column(String(200), nullable=True)
  rol = Column(String(20), default="cliente")
  fecha_registro = Column(DateTime, default=datetime.utcnow)

  pedidos = relationship("Pedido", back_populates="usuario")

  def __repr__(self):
    return f"<Usuario(id={self.id}, nombre='{self.nombre}')>"


# 2. TABLA CATEGORIAS (Nueva tabla independiente)
class Categoria(Base):
  __tablename__ = "categorias"

  id = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(50), nullable=False, unique=True)

  productos = relationship("Producto", back_populates="categoria")

  def __repr__(self):
    return f"<Categoria(id={self.id}, nombre='{self.nombre}')>"


# 3. TABLA PRODUCTOS
class Producto(Base):
  __tablename__ = "productos"

  id = Column(Integer, primary_key=True, autoincrement=True)
  nombre = Column(String(100), nullable=False)
  categoria_id = Column(
      Integer, ForeignKey("categorias.id"), nullable=False
  )  # Relación con Categoria
  talle = Column(String(10), nullable=False)
  color = Column(String(30), nullable=False)
  precio = Column(Float, nullable=False)
  stock = Column(Integer, default=0, nullable=False)
  imagen_url = Column(String(255), nullable=True)
  descripcion = Column(Text, nullable=True)
  fecha_creacion = Column(DateTime, default=datetime.utcnow)

  categoria = relationship("Categoria", back_populates="productos")
  detalles_pedido = relationship("DetallePedido", back_populates="producto")

  def __repr__(self):
    return f"<Producto(nombre='{self.nombre}', precio=${self.precio})>"


# 4. TABLA PEDIDOS
class Pedido(Base):
  __tablename__ = "pedidos"

  id = Column(Integer, primary_key=True, autoincrement=True)
  usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
  fecha_pedido = Column(DateTime, default=datetime.utcnow)
  estado = Column(String(30), default="Pendiente")
  total = Column(Float, nullable=False)

  usuario = relationship("Usuario", back_populates="pedidos")
  detalles = relationship("DetallePedido", back_populates="pedido")


# 5. TABLA DETALLE DE PEDIDO
class DetallePedido(Base):
  __tablename__ = "detalles_pedido"

  id = Column(Integer, primary_key=True, autoincrement=True)
  pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
  producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
  cantidad = Column(Integer, nullable=False, default=1)
  precio_unitario = Column(Float, nullable=False)

  pedido = relationship("Pedido", back_populates="detalles")
  producto = relationship("Producto", back_populates="detalles_pedido")