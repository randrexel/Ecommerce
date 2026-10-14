
from pathlib import Path
import matplotlib.pyplot as plt

# ==============================================================================
# CONFIGURACIÓN DE RUTAS DE SALIDA
# ==============================================================================

# Definimos la carpeta de destino para guardar las imágenes.
# Path() maneja automáticamente las barras de ruta tanto en Windows (\) como en Linux/Docker (/).
output_dir = Path("pry_ecommerce/imagenes")

# Creamos el directorio si no existe previamente en el sistema.
# - parents=True: Crea cualquier carpeta padre requerida en la ruta si no existe.
# - exist_ok=True: Evita un error de Python si la carpeta ya estaba creada.
output_dir.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# GUARDAR EL GRÁFICO
# ==============================================================================

# Unimos la ruta del directorio con el nombre del archivo usando el operador '/' de pathlib
ruta_imagen = output_dir / 'ingresos_por_pais.png'

# Guardamos el gráfico activo de matplotlib en la ruta especificada.
# - dpi=300: Configura una alta resolución (calidad para impresión/reportes).
# - bbox_inches='tight': Elimina espacios en blanco innecesarios alrededor del gráfico.
plt.savefig(ruta_imagen, dpi=300, bbox_inches='tight')