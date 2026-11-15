# Cafetería Aroma: sistema de inventario y ventas

Proyecto de práctica para aprender DevOps construyendo un sistema de inventario y ventas para una cafetería ficticia. Lo desarrollo mientras estudio Ingeniería de Software.

## Estado
Fase 2 completada: base de datos PostgreSQL en Docker y API CRUD de inventario y ventas.

## Tecnologías
- Python y FastAPI
- WSL2 (Ubuntu 24.04) y VS Code
- Planeadas: PostgreSQL, Docker, Nginx, GitHub Actions, Prometheus/Grafana, AWS y Terraform

## Cómo correrlo
```bash
git clone https://github.com/JosephGP31/cafeteria-devops.git
cd cafeteria-devops
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
docker compose up -d justo antes de uvicorn main:app --reload
```
Abre http://127.0.0.1:8000 y la documentación automática en http://127.0.0.1:8000/docs

## Hoja de ruta
- [x] Fase 1: entorno y API "hola mundo"
- [x] Fase 2: base de datos (PostgreSQL) y CRUD
- [ ] Fase 3: contenedores con Docker
- [ ] Fase 4: CI/CD con GitHub Actions
- [ ] Fase 5: monitoreo y respaldos
- [ ] Fase 6: despliegue en la nube
