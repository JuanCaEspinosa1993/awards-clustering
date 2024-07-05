import joblib
import torch
import plotly.express as px


def plot_clusters(features, labels):
    fig = px.scatter_3d(
        x=features[:, 0], y=features[:, 1], z=features[:, 2],
        color=labels,
        title="3D Scatter Plot of Clusters"
    )
    fig.show()


if __name__ == "__main__":
    features = torch.load('../data/processed/features.pt')
    model = joblib.load('../models/kmeans_model.pkl')
    labels = model.predict(features)
    plot_clusters(features, labels)
