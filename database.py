import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Carga las variables secretas desde tu archivo .env
load_dotenv()

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
HOST = os.getenv("POSTGRES_HOST", "localhost")

# 2. Construye la dirección de conexión (Connection String)
# Formato: postgresql://usuario:contraseña@localhost:5432/nombre_bd
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DB_NAME}"

# 3. Crea el motor (engine) que abre y administra la conexión con PostgreSQL
engine = create_engine(DATABASE_URL)

# 4. Fábrica de sesiones (cada petición HTTP a la API usará su propia sesión)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Clase base de la que heredarán nuestras 5 tablas en el siguiente paso
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        # Completa aquí: entrega la sesión 'db' usando la palabra clave yield
        yield db
    finally:
        # Completa aquí: cierra la sesión llamando al método .close() de db
        db.close()
