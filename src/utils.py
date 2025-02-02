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


