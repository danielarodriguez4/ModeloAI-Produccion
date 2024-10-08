import argparse
import pandas as pd
import joblib

import sys
if 'google.colab' in sys.modules:
    sys.argv = ['predict.py', '--data_file', 'input_data.csv', '--model_file', 'modelo_entrenado.pkl']

# Argumentos de línea de comando
parser = argparse.ArgumentParser()
parser.add_argument('--data_file', required=True, type=str, help='a csv file with input data for predictions')
parser.add_argument('--model_file', required=True, type=str, help='the trained model file to load')

args = parser.parse_args()

model_file = args.model_file
data_file = args.data_file

# Se carga el modelo entregado en el script train.py
model = joblib.load('/content/modelo_entrenado.pkl')

# Se cargan los datos de entrada
data = pd.read_csv('/content/train.csv')

# Conversión a Unix timestamp en la columna de las fechas
if 'datetime' in data.columns:
    data['datetime'] = pd.to_datetime(data['datetime'])
    data['datetime'] = data['datetime'].apply(lambda x: x.timestamp())

# Uso de catacterísticas necesarias
feature_columns = [col for col in data.columns if col != 'count']
data = data[feature_columns]

# Se generan las predicciones
predictions = model.predict(data)

# Se guardan las predicciones en un archvio csv
output = pd.DataFrame(predictions, columns=["Prediction"])
output.to_csv("predicciones.csv", index=False)
print("Predicciones guardadas en predicciones.csv.")

