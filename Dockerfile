# Usar una imagen oficial de Python ligera
FROM python:3.10-slim

# Evitar que Python genere archivos .pyc y asegurar salida en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecer directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código y archivos del proyecto al contenedor
COPY . .

# Exponer el puerto para JupyterLab (opcional, si usas notebooks)
EXPOSE 8888

# Comando predeterminado: Iniciar JupyterLab o ejecutar tu script principal
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]