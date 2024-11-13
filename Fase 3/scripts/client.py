import requests

# Llamada al endpoint /train
response = requests.post('http://localhost:5000/train', json={'data_file': 'data/train.csv'})
print(response.json())

# Llamada al endpoint /predict
response = requests.post('http://localhost:5000/predict', json={'data_file': 'data/input_data.csv'})
print(response.json())
