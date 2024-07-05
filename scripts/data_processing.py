# Procesamiento y limpieza de datos
import xml.etree.ElementTree as ET
import os


def process_data(data):
    processed_data = []
    for item in data:
        # Procesar cada elemento del XML
        award = item.find('Award')
        processed_item = {
            'title': award.find('AwardTitle').text.strip(),
            'agency': award.find('AGENCY').text,
            'effective_date': award.find('AwardEffectiveDate').text,
            'expiration_date': award.find('AwardExpirationDate').text,
            'total_amount': float(award.find('AwardTotalIntnAmount').text),
            'amount': float(award.find('AwardAmount').text),
            'abstract': award.find('AbstractNarration').text.strip(),
            'investigator': award.find('Investigator/PI_FULL_NAME').text,
            'institution': award.find('Institution/Name').text.strip(),
        }
        processed_data.append(processed_item)
    return processed_data


if __name__ == "__main__":
    from data_ingestion import read_xml_files

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    relative_path = 'data/raw'
    absolute_path = os.path.abspath(
        os.path.join(parent_dir + "/" + relative_path))
    print(f" buscando data en: {absolute_path}")

    input_dir = absolute_path

    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"El directorio {input_dir} no existe")

    data = read_xml_files(input_dir)
    processed_data = process_data(data)
    print(processed_data[:2])
