import pandas as pd


def convert_daftar_saham(input_file: str, output_file: str):
    df = pd.read_excel(input_file)
    df.drop(columns=df.columns[0], inplace=True)
    df.set_index(df.columns[0], inplace=True)
    df.to_json(output_file, orient="index", indent=4)
