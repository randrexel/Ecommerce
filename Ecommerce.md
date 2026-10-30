# Online Retail E-Commerce Analytics & Modeling

## Objetivo del Proyecto
Analizar el comportamiento de las ventas de una tienda de comercio electrónico  a partir de sus registros de transacciones.
El proyecto busca conocer la distribución de ventas por países, identificar patrones de compra y estudiar la relación entre cantidades vendidas y los precios unitarios, utilizando herramientas de datos y modelado.

## Dataset Utilizado
- **Fuente:** Dataset transaccional de e-commerce (541,909 registros).
- **Cobertura:** Transacciones globales (principalmente UK e internacional, país con una elevada concentración de transacciones).

## Variables Principales
- `InvoiceNo`: Número de factura (identificador para cada transacción; Las devoluciones estan marcadas con 'C').
- `StockCode`: Código de cada producto.
- `Description`: Nombre del producto.
- `Quantity`: Cantidad de unidades adquiridas por transacción.
- `InvoiceDate`: Fecha y hora de factura.
- `UnitPrice`: Precio unitario del producto en libras esterlinas.
- `CustomerID`: Identificador único del cliente, usado para evaluar el comportamiento del cliente y también conocer registros sin identificar.
- `Country`: País de origen o asociado al cliente.

## Desarrollo del Proyecto (Pipeline)
1. **Data Engineering:** Se realizo la revisión de tipos de datos y limpieza de datos, así como auditoría de nulos en `CustomerID` para evaluar el impacto de las ventas de clientes sin identificar.
2. **Business Analysis & EDA:** Visualizaciones con Seaborn para observar y comprender el comportamiento de la distribución de precios, cantidades y como se reparten geograficamente.
3. **Feature Engineering:** Creación de métricas de ingresos totales (`TotalPrice`) y con su filtro correspondiente para las cancelaciones o devoluciones.
4. **Modelado y Evaluación:** Se aplico un modelo de Regresión Lineal para analizar la relación entre cantidad vendidas y precio, evaluando su los resultados obtenidos.

## Resultados Principales
**Análisis Geográfico y Power BI:** El análisis de las ventas por país permitió identificar que el **Reino Unido** concentra la gran mayoría de las transacciones e ingresos globales de la tienda. En power BI se implementaron mapas coropléticos con degradados de color y medidas DAX personalizadas en libras (£), esto para representar los ingresos.
El segundo lugar en ventas es Irlanda con un amplio margen de diferencia en relación a Reino Unido.
* **Segmentación de Clientes (RFM):** Se utilizaron para el procesamiento en Pandas y NumPy (`np.select`), se clasificó a la base de datos en clústeres estratégicos (`Champions / VIP`, `Leales`, `En Riesgo`, `Inactivos`). Esta clasificación permite identificar qué clientes requieren campañas que priorizen su retención.
* **Modelado:** El análisis de regresión se pudo comprender el comportamiento de las ventas en función del precio unitario de los productos.

## Tecnologías Utilizadas
- **Python:** Principalmente usado para el desarrollo del proyecto.
- **Pandas / NumPy:** Manipulación y transformación de datos.
- **Seaborn / Matplotlib:** Visualización de datos exploratorios.
- **Scikit-Learn:** Modelado de regresión lineal.
- **GitHub:** Respaldos del proyecto.
- **Docker:** Contenerización y reproducibilidad del entorno.

## Cómo Ejecutar el Proyecto
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/randrexel/Ecommerce.git](https://github.com/randrexel/Ecommerce.git)