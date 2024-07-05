from sklearn.cluster import KMeans
import joblib


def train_model(features):
    model = KMeans(n_clusters=3)  # Por ejemplo, 3 clusters
    model.fit(features)
    return model


if __name__ == "__main__":
    from feature_engineering import extract_features
    from data_processing import process_data
    from data_ingestion import read_xml_files

    input_dir = '../data/raw/'
    data = read_xml_files(input_dir)
    processed_data = process_data(data)
    features, vectorizer = extract_features(processed_data)
    model = train_model(features)

    joblib.dump(model, '../models/model.pkl')
    joblib.dump(vectorizer, '../models/vectorizer.pkl')
