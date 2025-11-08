# Actividad Repaso

## Crear el entorno con venv

```
# Crear entorno virtual
python -m venv .env

# Activar entorno
# En Windows
.env\Scripts\activate
# En macOS / Linux
source .env/bin/activate

# En Windows, Si aparece el error .env\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. Ejecutar:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned


# Instalar paquetes
pip install flask

# Guardar dependencias
pip freeze > requirements.txt

# Restaurar dependencias
pip install -r requirements.txt

# Desactivar entorno
deactivate
```