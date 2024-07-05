# Evaluación de modelo
from sklearn.metrics import silhouette_score, davies_bouldin_score


def evaluate_clustering(features, labels):
    silhouette_avg = silhouette_score(features, labels)
    davies_bouldin_avg = davies_bouldin_score(features, labels)
    print(f"Silhouette Score: {silhouette_avg}")
    print(f"Davies-Bouldin Index: {davies_bouldin_avg}")
    return silhouette_avg, davies_bouldin_avg


if __name__ == "__main__":
    import torch
    import joblib

    features = torch.load('../data/processed/features.pt')
    model = joblib.load('../models/kmeans_model.pkl')
    labels = model.predict(features)
    evaluate_clustering(features, labels)
