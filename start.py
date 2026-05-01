import os
import subprocess
import sys

# Obtenemos el puerto que nos da Render (por defecto 8000 si no lo encuentra)
port = os.environ.get("PORT", "8000")

# Comando corregido para Mercury
cmd = [
    sys.executable, "-m", "mercury", "run", 
    "02_articulo_interactivo.ipynb", # El archivo que vas a servir
    "--host", "0.0.0.0",             # CRÍTICO: Render necesita 0.0.0.0 para exponer la app a internet
    "--port", port                   # El puerto dinámico de Render
]

print(f"🚀 Arrancando Mercury en el puerto {port}...")
subprocess.run(cmd)