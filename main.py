import logging

from src.data_reader import read_json
from src.helper import update_daftar_saham, ringkasan_saham


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
    )

    update_daftar_saham()
    ringkasan_saham()


if __name__ == "__main__":
    main()
