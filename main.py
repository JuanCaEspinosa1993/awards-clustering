from scripts.data_ingestion import read_xml_files
from scripts.data_processing import process_data
from scripts.feature_engineering_torch import extract_features
from scripts.model_training import train_model
from scripts.visualization import plot_clusters
from scripts.model_evaluation import evaluate_clustering
import torch
import joblib
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = 'data/raw'

absolute_path = os.path.join(script_dir + "/" + relative_path)

input_dir = absolute_path
print(f"Ruta source data: {input_dir}")

if not os.path.exists(input_dir):
    raise FileNotFoundError(f"El directorio {input_dir} no existe")

# relative_path = '../data/raw'
# absolute_path = os.path.abspath(relative_path)
# print(relative_path)
# print(absolute_path)

# # Leer y procesar datos
data = read_xml_files(input_dir)
print(data)
processed_data = process_data(data)

# Extraer características y entrenar modelo
features = extract_features(processed_data)
# torch.save(features, '../data/processed/features.pt')
# model = train_model(features)

# # Guardar modelo y vectorizador
# joblib.dump(model, '../models/k_means_model.pkl')

# # Evaluar modelo
# labels = model.predict(features)
# evaluate_clustering(features, labels)

# # Visualizar clusters
# plot_clusters(features, labels)
