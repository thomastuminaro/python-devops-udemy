import logging
import sys

def setup_script_logger(logger_name: str) -> logging.Logger:
    """Creates and return a logger

    Args:
        logger_name (str): name of the new logger to create, must not be empty

    Raises:
        TypeError: if logger_name isn't a string
        ValueError: if logger_name is empty
        e: generic error which will match any logger configuration issue

    Returns:
        logging.Logger: configuration of the new logger
    """
    if not isinstance(logger_name, str):
        raise TypeError("logger_name must be a string.")
    if logger_name == "":
        raise ValueError("logger_name must not be empty.")
    try:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        sh_handler = logging.StreamHandler(sys.stdout)
        fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        sh_handler.setFormatter(fmt)
        logger.addHandler(sh_handler)
    except Exception as e:
        print(f"Faced error when configuring logger : {e}")
        raise e
    else:
        return logger

if __name__ == "__main__":
    mylogger = setup_script_logger("mylogger")
    mylogger.debug("Test warning message")

    fail_logger = setup_script_logger("")