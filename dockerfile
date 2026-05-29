#paso 1 buscar una imagen base
FROM python:3.12-alpine

#paso 2 crear un directorio de trabajo
WORKDIR /app

#paso 3 copiar el archivo de dependencias
COPY requirements.txt /app

#paso 4 instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

#paso 5 copiar el código fuente
COPY . app.py/app

#paso 6 exponer el puerto
EXPOSE 5000

#paso 7 ejecutar la aplicación
CMD ["python", "app.py"]