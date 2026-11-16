# 1. Imagen base ligera con Python 3.12
FROM python:3.12-slim

# 2. Carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar e instalar dependencias primero para aprovechar la caché de capas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código de la API
COPY . .

# 5. Crear un usuario sin privilegios de administrador y cambiar a él
RUN  useradd --create-home appuser
USER  appuser

# 6. Documentar el puerto que usa FastAPI
EXPOSE 8000

# 7. Comando para iniciar Uvicorn escuchando en todas las interfaces de red
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]