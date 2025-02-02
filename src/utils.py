import datetime
from pathlib import Path


class PathManager:
    """Static utility class for managing project paths."""

    @staticmethod
    def get_root_path() -> Path:
        return Path(__file__).resolve().parent.parent

    @staticmethod
    def get_data_path() -> Path:
        return PathManager.get_root_path() / "data"

    @staticmethod
    def file_exists(filename: str) -> bool:
        return (PathManager.get_data_path() / filename).exists()

    @staticmethod
    def get_file_path(filename: str) -> Path:
        return PathManager.get_data_path() / filename

    @staticmethod
    def get_output_path(dir_name: str) -> Path:
        return PathManager.get_data_path() / dir_name


def generate_date_range(start_date: str, end_date: str) -> list:
    formatted_start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    formatted_end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    date_range_length = (formatted_end_date - formatted_start_date).days + 1
    date_list = [
        (formatted_start_date + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        for i in range(date_range_length)
    ]
    return date_list
