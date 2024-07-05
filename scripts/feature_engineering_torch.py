import torch
from transformers import BertModel, BertTokenizer


def extract_features(processed_data):
    abstracts = [item['abstract'] for item in processed_data]
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')

    features = []
    for abstract in abstracts:
        inputs = tokenizer(abstract, return_tensors='pt',
                           padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        # Use [CLS] token representation
        embeddings = outputs.last_hidden_state[:, 0, :].numpy()
        features.append(embeddings)

    features = torch.cat(features, dim=0)
    return features


if __name__ == "__main__":
    from data_processing import process_data
    from data_ingestion import read_xml_files

    input_dir = '../data/raw/'
    data = read_xml_files(input_dir)
    processed_data = process_data(data)
    features = extract_features(processed_data)
    torch.save(features, '../data/processed/features.pt')
