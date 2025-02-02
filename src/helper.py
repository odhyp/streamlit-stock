from src.bot_idx import IDXBot
from src.converter import convert_daftar_saham
from src.utils import PathManager as pm


def update_daftar_saham():
    excel_path = pm.get_file_path("daftar_saham.xlsx")
    json_path = pm.get_file_path("daftar_saham.json")

    with IDXBot() as bot:
        bot.download_daftar_saham(output_name=excel_path)

    convert_daftar_saham(input_file=excel_path, output_file=json_path)
