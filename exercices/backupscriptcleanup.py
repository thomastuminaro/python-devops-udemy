import shutil
from pathlib import Path

def create_backup(source_dir: str | Path, dest_dir: str | Path) -> None:
    if not isinstance(source_dir, (Path, str)) or not isinstance(dest_dir, (Path, str)):
        raise TypeError("source_dir and dest_dir must be string or Path.")
    
    src_path = source_dir
    dst_path = dest_dir

    if isinstance(source_dir, str):
        src_path = Path(source_dir)
    if isinstance(dest_dir, str):
        dst_path = Path(dest_dir)

    if not src_path.exists() or not src_path.is_dir(): #type: ignore
        raise ValueError("source_dir directory must exist.")
    
    if dst_path.exists(): #type: ignore
        shutil.rmtree(dest_dir)

    shutil.copytree(src=src_path, dst=dst_path)

if __name__ == "__main__":
    src = Path(__file__).parent / "files/source"
    dst = Path(__file__).parent / "files/dest"
    dst_wrong = ["list"]
    src_wrong = Path(__file__).parent / "files/conf.txt"
    create_backup(src, dst)