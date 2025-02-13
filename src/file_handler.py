import csv
from typing import List, Dict

class FileHandler:
    """Handles reading and writing CSV files."""
    @staticmethod
    def read_csv(file_path: str) -> List[Dict[str, str]]:
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
            return []

    @staticmethod
    def write_csv(file_path: str, data: List[Dict[str, str]], fieldnames: List[str]) -> None:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)