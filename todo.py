# 🚀 Importando librerías necesarias
import json              # 📄 Para leer y escribir archivos JSON
import argparse          # 💻 Para crear la interfaz CLI
from pathlib import Path  # 📁 Manejo de rutas de archivos
from colorama import init, Fore, Style  # 🎨 Para colores en terminal
init(autoreset=True)

# 📂 Ruta del archivo JSON que almacena las tareas
todo = Path("tasks.json")
