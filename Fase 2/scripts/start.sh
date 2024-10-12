#!/bin/bash
if [[ "$1" == "train" ]]; then
    python train.py
elif [[ "$1" == "predict" ]]; then
    python predict.py
else
    echo "Opción inválida. Utiliza 'train' o 'predict'"
