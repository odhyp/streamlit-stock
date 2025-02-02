import logging
import pandas as pd


def convert_daftar_saham(input_file: str, output_file: str):
    logging.debug("Running %s on %s", __name__, input_file)
    df = pd.read_excel(input_file)
    df.drop(columns=df.columns[0], inplace=True)
    df.set_index(df.columns[0], inplace=True)
    df.to_json(output_file, orient="index", indent=4)
    logging.info("Successfully converted %s to %s", input_file, output_file)
