import os
import subprocess
import sys

# Obtenemos el puerto que nos da Render
port = os.environ.get("PORT", "8000")

# Comando para forzar el arranque de Mercury
# Usamos el ejecutable directo de python para evitar errores de PATH
cmd = [
    sys.executable, "-m", "mercury", "run", 
    "0.0.0.0:" + port, 
    "--port", port,
    "02_articulo_interactivo.ipynb"
]

print(f"🚀 Arrancando Mercury en el puerto {port}...")
subprocess.run(cmd)