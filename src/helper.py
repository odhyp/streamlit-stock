from src.bot_idx import IDXBot


def sample_func():
    with IDXBot() as bot:
        bot.download_daftar_saham(file_name="daftar_saham.xlsx")
