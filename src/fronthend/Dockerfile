# Imagen base ligera
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del frontend (app.py y carpeta templates)
COPY . .

# Exponer el puerto del frontend
EXPOSE 3000

# Ejecutar la aplicación
CMD ["python", "app.py"]
