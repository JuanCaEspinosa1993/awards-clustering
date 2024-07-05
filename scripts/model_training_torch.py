from sklearn.cluster import KMeans
import torch
import joblib


def train_model(features):
    kmeans = KMeans(n_clusters=3)  # Por ejemplo, 3 clusters
    kmeans.fit(features)
    return kmeans


if __name__ == "__main__":
    features = torch.load('../data/processed/features.pt')
    model = train_model(features)
    joblib.dump(model, '../models/kmeans_model.pkl')
