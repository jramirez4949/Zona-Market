# Zona-Market API

API simple desarrollada con FastAPI ejecutada dentro de Docker.

## Requisitos

- Docker Desktop instalado

## Cómo ejecutar el proyecto

Desde la carpeta del proyecto ejecutar:

docker compose up --build

## Acceso al servicio

Endpoint principal:

http://localhost:8000/

Respuesta:

hola mundo

Endpoint de salud:

http://localhost:8000/health

Respuesta:

{"status": "ok"}