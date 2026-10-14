# Online Retail E-Commerce Analytics & Modeling

## 🎯 Objetivo del Proyecto
Analizar el comportamiento de ventas globales y la relación económica entre volumen de compra y precios unitarios en una tienda minorista online, aplicando un pipeline completo de Ciencia de Datos e Ingeniería.

## 📊 Dataset Utilizado
- **Fuente:** Dataset transaccional de e-commerce (541,909 registros).
- **Cobertura:** Transacciones globales (principalmente UK e internacional).

## 🔤 Variables Principales
- `InvoiceNo`: Número de factura (identificador de transacción; detecta devoluciones con 'C').
- `StockCode`: Código de producto.
- `Description`: Nombre del producto.
- `Quantity`: Cantidad de unidades adquiridas por transacción.
- `InvoiceDate`: Fecha y hora de la factura.
- `UnitPrice`: Precio unitario del producto en libras esterlinas.
- `CustomerID`: Identificador único del cliente (incluye análisis de impacto por valores nulos).
- `Country`: País de origen del cliente.

## ⚙️ Proceso del Proyecto (Pipeline)
1. **Data Engineering:** Limpieza de tipos de datos y auditoría de nulos en `CustomerID` para evaluar el peso de las ventas de usuarios no registrados.
2. **Business Analysis & EDA:** Visualizaciones con Seaborn para entender la distribución de precios, cantidades y desempeño geográfico.
3. **Feature Engineering:** Creación de métricas de ingresos totales (`TotalPrice`) y filtrado de anomalías (devoluciones).
4. **Modelado y Evaluación:** Entrenamiento de un modelo de Regresión Lineal para analizar la elasticidad/relación entre cantidad y precio, evaluando su desempeño.

## 📈 Resultados Principales
- [Espacio reservado para tus conclusiones clave, ej: El análisis geográfico demostró que X país concentra el Y% de las ventas...]
- [Conclusión sobre la regresión lineal...]

## 🛠️ Tecnologías Utilizadas
- **Python:** Lenguaje principal de análisis.
- **Pandas / NumPy:** Manipulación y transformación de datos.
- **Seaborn / Matplotlib:** Visualización de datos exploratorios.
- **Scikit-Learn:** Modelado de regresión lineal.
- **Docker:** Contenerización y reproducibilidad del entorno.

## 🚀 Cómo Ejecutar el Proyecto
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/online-retail-analysis.git](https://github.com/tu-usuario/online-retail-analysis.git)