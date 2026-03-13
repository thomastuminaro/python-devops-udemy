from pathlib import Path

def read_config_file(filepath):
    """
    Validates the filepath and yields each line from the file.

    Args:
        filepath (str): The path to the configuration file.

    Yields:
        str: A single line from the file.
    """
    
    with open(filepath, 'r') as f:
        for line in f:
            yield line


def filter_config_lines(lines):
    """
    Filters an iterable of lines, yielding stripped, non-empty, non-comment lines.

    Args:
        lines (iterable): An iterable producing string lines.

    Yields:
        str: A line that is not a comment or empty.
    """
    for line in lines:
        if line.strip() == "" or line.startswith("#"):
            continue
        yield line.strip() 


def parse_config_lines(lines):
    """
    Parses an iterable of clean config lines into (section, key, value) tuples.

    Args:
        lines (iterable): An iterable producing clean config lines.

    Yields:
        tuple: A tuple in the format (section, key, value).
    """
    
    section = None
    for line in lines:
        if line.startswith("["):
            section = line.strip("[]")
            continue
        yield (section, line.strip(" ").split("=")[0].strip(), "=".join(line.strip(" ").split("=")[1:]).strip()) 

if __name__ == "__main__":
    conf = Path(__file__).parent / "files/conf.txt"
    print(conf)

    conf_gen = read_config_file(conf)
    conf_filtered = filter_config_lines(conf_gen)
    conf_parsed = parse_config_lines(conf_filtered)

    for l in conf_parsed:
        print(l)