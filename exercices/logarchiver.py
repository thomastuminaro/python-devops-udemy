from pathlib import Path
from typing import Union
import re

def archive_log_files(log_directory: Union[str, Path], archive_date: str) -> list[Path]:
    if not isinstance(log_directory, Path) and not isinstance(log_directory, str):
        raise TypeError("log_directory must be a Path or a string.")
    
    folder = log_directory
    if isinstance(log_directory, str):
        folder = Path(log_directory)
    
    if not folder.is_dir() or not folder.exists(): #type: ignore
        raise ValueError("log_directory must exist and be a directory.")
    
    if not isinstance(archive_date, str):
        raise TypeError("archive_date must be a string.")
    
    if not re.compile("(1|2)[0-9]{3}-[0-1][0-9]-[0-3][0-9]").match(archive_date):
        raise ValueError("archive_date must be in YYYY-MM-DD format.")
    
    renamed_files = []
    for file in folder.glob("*.log"): #type: ignore
        file.rename(f"{folder}/{file.stem}-{archive_date}.log")
        renamed_files.append(file)
    
    return renamed_files

if __name__ == "__main__":
    log_dir = Path(__file__).parent / "empty"
    log_dir_str = "/Users/thomastuminaro/Documents/Work/Python/python-devops-udemy/exercices/files/"
    print(archive_log_files(log_dir, "2026-05-18"))