#Imagen base de python ligera
FROM python:3.11-slim

#Evita que genere archivos .pyc en el contenedor
ENV PYTHONDONTWRITEBYTECODE=1

#Imprime directamente en stdout 
ENV PYTHONUNBUFFERED=1

# Instala dependencias del sistema necesarias para compilar algunas librerías
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia requirements.txt a /app/requirements.txt
COPY requirements.txt .

#Instala dependencias listadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]