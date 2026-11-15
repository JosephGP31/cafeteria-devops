from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict


# --- CATEGORÍAS ---
class CategoriaCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)


class CategoriaResponse(BaseModel):
    id: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)


# --- PRODUCTOS ---
class ProductoCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=150)
    precio: Decimal = Field(..., gt=0)
    stock: int = Field(default=0, ge=0)
    categoria_id: int


class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio: Decimal
    stock: int
    categoria_id: int

    model_config = ConfigDict(from_attributes=True)


# --- CLIENTES ---
class ClienteCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=150)
    email: str = Field(..., min_length=5, max_length=150)


class ClienteResponse(BaseModel):
    id: int
    nombre: str
    email: str

    model_config = ConfigDict(from_attributes=True)


# --- VENTAS Y DETALLE DE VENTA ---
class DetalleVentaCreate(BaseModel):
    producto_id: int
    cantidad: int = Field(..., gt=0)


class DetalleVentaResponse(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    precio_unitario: Decimal

    model_config = ConfigDict(from_attributes=True)


class VentaCreate(BaseModel):
    cliente_id: int | None = None
    detalles: list[DetalleVentaCreate] = Field(..., min_length=1)


class VentaResponse(BaseModel):
    id: int
    fecha: datetime
    cliente_id: int | None
    total: Decimal

    model_config = ConfigDict(from_attributes=True)