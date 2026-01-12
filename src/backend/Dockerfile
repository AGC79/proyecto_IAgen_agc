# Imagen base ligera de Python 3.11
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copia requirements
COPY requirements.txt .

# Instala dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Instala dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la app
COPY . .

# Copia wait-for-it.sh
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Expone puerto Flask
EXPOSE 5000

# Comando: espera a la DB y luego arranca Flask
CMD ["wait-for-it.sh", "iagen_db:5432", "--", "python", "main.py"]
