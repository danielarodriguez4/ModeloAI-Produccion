#!/bin/bash

if [[ "$1" == "train" ]]; then
    python train.py
elif [[ "$1" == "predict" ]]; then
    python predict.py
elif [[ "$1" == "api" ]]; then
    export FLASK_APP=apirest.py
    flask run --host=0.0.0.0 --port=5000
else
    echo "Opción inválida. Usa 'train', 'predict' o 'api'."
fi
