#!/bin/bash

VENV_NAME="env"

if [ -d "$VENV_NAME" ]; then
    echo "Activando el entorno virtual '$VENV_NAME'..."
    source "$VENV_NAME/bin/activate"
    echo "Entorno virtual activado."
    echo "Levantando el servidor..."
    python Web-Socket/server.py
else
    echo "El entorno virtual '$VENV_NAME' no existe. Creando uno nuevo..."
    python3 -m venv "$VENV_NAME"
    source "$VENV_NAME/bin/activate"
    echo "Entorno virtual '$VENV_NAME' creado y activado."
    echo "Descargando Dependencias"
    pip install -r requirements.txt
    echo "Levantando el servidor..."
    python Web-Socket/server.py
fi


source "$VENV_NAME/bin/activate"

