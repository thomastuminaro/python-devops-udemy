import os
from pathlib import Path

def read_log_lines(filepath):
    """
    Creates a generator that reads a log file, yielding valid, non-comment lines.

    Args:
        filepath (str): The path to the log file.

    Yields:
        str: A stripped, non-empty, non-comment line from the file.
    """
    # TODO: Implement the generator logic.
    # 1. Open the file safely.
    # 2. Iterate through each line, removing whitespace and checking whether it's valid.
    # 3. If the line is valid, yield it.
    with open(Path(filepath), 'r') as f:
        for line in f.readlines():
            if line.startswith("["):
                yield(line.strip())
            else:
                continue

if __name__ == "__main__":
    logfile = f"{Path(__file__).parent}/files/log.txt"
    print(logfile)
    lines_gen = read_log_lines(logfile)

    for line in lines_gen:
        print(line)