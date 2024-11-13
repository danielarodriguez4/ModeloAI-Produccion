#!/bin/bash

if [[ "$1" == "train" ]]; then
    # Ejecuta el script de entrenamiento
    python train.py
elif [[ "$1" == "predict" ]]; then
    # Ejecuta el script de predicción
    python predict.py
elif [[ "$1" == "api" ]]; then
    # Inicia el servidor Flask para la API REST
    echo "Iniciando la API REST Flask..."
    export FLASK_APP=apirest.py
    export FLASK_ENV=development  # Solo en desarrollo, quítalo para producción
    flask run --host=0.0.0.0 --port=5000
else
    echo "Opción inválida. Utiliza 'train', 'predict' o 'api'."
fi
