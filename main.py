from decimal import Decimal
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cafetería Aroma API", version="0.2.0")


@app.get("/")
def leer_raiz():
    return {"mensaje": "¡Bienvenido a Cafetería Aroma!", "estado": "activo"}


# --- CATEGORÍAS ---
@app.post("/categorias/", response_model=schemas.CategoriaResponse, status_code=status.HTTP_201_CREATED)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    existe = db.query(models.Categoria).filter(models.Categoria.nombre == categoria.nombre).first()
    if existe:
        raise HTTPException(status_code=400, detail="Esa categoría ya existe")

    nueva_categoria = models.Categoria(nombre=categoria.nombre)
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria


@app.get("/categorias/", response_model=list[schemas.CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(models.Categoria).all()


# --- PRODUCTOS ---
@app.post("/productos/", response_model=schemas.ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter(models.Categoria.id == producto.categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="La categoría indicada no existe")

    nuevo_producto = models.Producto(**producto.model_dump())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto


@app.get("/productos/", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(models.Producto).all()


# --- CLIENTES ---
@app.post("/clientes/", response_model=schemas.ClienteResponse, status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    existe = db.query(models.Cliente).filter(models.Cliente.email == cliente.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="Ese correo ya está registrado")

    nuevo_cliente = models.Cliente(**cliente.model_dump())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente


@app.get("/clientes/", response_model=list[schemas.ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(models.Cliente).all()


# --- VENTAS ---
@app.post("/ventas/", response_model=schemas.VentaResponse, status_code=status.HTTP_201_CREATED)
def registrar_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    if venta.cliente_id is not None:
        cliente = db.query(models.Cliente).filter(models.Cliente.id == venta.cliente_id).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="El cliente indicado no existe")

    nueva_venta = models.Venta(cliente_id=venta.cliente_id, total=Decimal("0.00"))
    db.add(nueva_venta)
    db.flush()  # Obtiene el ID de la venta sin confirmar aún la transacción

    total_venta = Decimal("0.00")

    for item in venta.detalles:
        producto = db.query(models.Producto).filter(models.Producto.id == item.producto_id).first()
        if not producto:
            db.rollback()
            raise HTTPException(status_code=404, detail=f"Producto ID {item.producto_id} no existe")

        if producto.stock < item.cantidad:
            db.rollback()
            raise HTTPException(
                status_code=400,
                detail=f"Stock insuficiente para '{producto.nombre}' (disponible: {producto.stock})"
            )

        subtotal = producto.precio * item.cantidad
        total_venta += subtotal
        producto.stock -= item.cantidad

        detalle = models.DetalleVenta(
            venta_id=nueva_venta.id,
            producto_id=producto.id,
            cantidad=item.cantidad,
            precio_unitario=producto.precio,
        )
        db.add(detalle)

    nueva_venta.total = total_venta
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta


@app.get("/ventas/", response_model=list[schemas.VentaResponse])
def listar_ventas(db: Session = Depends(get_db)):
    return db.query(models.Venta).all()


@app.get("/ventas/{venta_id}/detalles", response_model=list[schemas.DetalleVentaResponse])
def obtener_detalles_venta(venta_id: int, db: Session = Depends(get_db)):
    venta = db.query(models.Venta).filter(models.Venta.id == venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return db.query(models.DetalleVenta).filter(models.DetalleVenta.venta_id == venta_id).all()