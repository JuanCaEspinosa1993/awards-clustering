# Lectura y carga de datos XML
import os
import xml.etree.ElementTree as ET


def read_xml_files(input_dir):
    data = []
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.xml'):
            file_path = os.path.join(input_dir, file_name)
            tree = ET.parse(file_path)
            root = tree.getroot()
            data.append(root)
    return data


if __name__ == "__main__":
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
    # Aquí puedes guardar o procesar los datos leídos
