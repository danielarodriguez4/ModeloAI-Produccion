
# Descripción  

 - **Fase 2**:
    - Se añade el script `01 - generate data and model.py` para generar datos sintéticos.
    - Se añade el script `02 - run scripts.py` para cargar los archivos generados en los scripts `train.py` y `predict.py`.

# ¿Cómo ejecutar?
  
- **Fase 2**
    - Corre el script `train.py` para entrenar un modelo de regresión lineal basado en el "train.csv" del modelo inicial.
    - Abre el script `predict.py`.
    - Carga el archivo `modelo_entrenado.pkl` para generar predicciones usando el modelo pre-entrenado generado en el punto anterior.
    - Una vez generadas las predicciones, cárgalas en `01 - generate data and model.py` y corre el código.
    - Carga el archivo `predicciones.csv`, `test_new_data.csv` y train_new_data.csv` en el `02 - run scripts.py` y corre el código para obtener el nuevo modelo e
