from src.bot_idx import IDXBot
from src.converter import convert_daftar_saham
from src.utils import PathManager as pm, generate_date_range


def update_daftar_saham():
    # TODO: add a logger file to know when the "daftar_saham" is last updated
    # TODO: delete unused "daftar_saham.xlsx" file after converting
    excel_path = pm.get_file_path("daftar_saham.xlsx")
    json_path = pm.get_file_path("daftar_saham.json")

    with IDXBot() as bot:
        bot.download_daftar_saham(output_name=excel_path)

    convert_daftar_saham(input_file=excel_path, output_file=json_path)


def ringkasan_saham():
    start_date = "2025-01-02"
    end_date = "2025-01-02"

    output_dir = pm.get_output_path("ringkasan_saham")
    date_range = generate_date_range(start_date, end_date)

    with IDXBot() as bot:
        bot.download_ringkasan_saham(output_dir, date_range)
