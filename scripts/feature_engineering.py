from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def extract_features(processed_data):
    abstracts = [item['abstract'] for item in processed_data]
    vectorizer = TfidfVectorizer(stop_words='english')
    features = vectorizer.fit_transform(abstracts)
    return features, vectorizer


if __name__ == "__main__":
    from data_processing import process_data
    from data_ingestion import read_xml_files

    input_dir = '../data/raw/'
    data = read_xml_files(input_dir)
    processed_data = process_data(data)
    features, vectorizer = extract_features(processed_data)
    # Aquí puedes guardar las características y el vectorizador
