import argparse
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
import sys
if 'google.colab' in sys.modules:
    sys.argv = ['train.py', '--data_file', 'train.csv', '--model_file', 'modelo_entrenado.pkl', '--overwrite_model']

parser = argparse.ArgumentParser()
parser.add_argument('--data_file', required=True, type=str, help='a csv file with train data')
parser.add_argument('--model_file', required=True, type=str, help='where the trained model will be stored')
parser.add_argument('--overwrite_model', default=False, action='store_true', help='if sets overwrites the model file if it exists')

args = parser.parse_args()

model_file = args.model_file
data_file = args.data_file
overwrite = args.overwrite_model

# Cargar datos de entrenamiento
data = pd.read_csv('train.csv')

# Convertir las fechas a Unix timestamp
data['datetime'] = pd.to_datetime(data['datetime'])
data['datetime'] = data['datetime'].apply(lambda x: x.timestamp())

X = data.drop("count", axis=1)  # Características
y = data["count"]  # Etiquetas

# Entrenar el modelo
model = LinearRegression()
model.fit(X, y)

# Guardar el modelo en un archivo
joblib.dump(model, model_file)
print(f"Modelo guardado exitosamente en {model_file}.")
