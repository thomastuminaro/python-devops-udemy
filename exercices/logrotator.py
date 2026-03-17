import logging, logging.handlers
from pathlib import Path

def configure_rotating_logger(logger_name: str, log_filepath: str, max_size_bytes: int, backup_count: int) -> logging.Logger:
    """Generates a rotating file logger 

    Args:
        logger_name (str): name of the logger, must be string and not empty
        log_filepath (str): path where to write logs, must be non empty string
        max_size_bytes (int): must be above 0, size at which logs rotate
        backup_count (int): can be 0 or above, count of backups to keep 

    Returns:
        logging.Logger: configured logger 
    """
    if not isinstance(logger_name, str) or not isinstance(log_filepath, str):
        raise TypeError("logger_name and log_filepath must be string.")
    if log_filepath == "" or logger_name == "":
        raise ValueError("logger_name and log_filepath must not be empty.")
    if not max_size_bytes > 0:
        raise ValueError("max_size_bytes must be a positive number.")
    if not backup_count >= 0 or not isinstance(backup_count, int):
        raise ValueError("backup_count must be a non-negative integer.")
    
    try:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        rotate_fh = logging.handlers.RotatingFileHandler(filename=log_filepath, 
                                                         mode="a",
                                                         maxBytes=max_size_bytes,
                                                         backupCount=backup_count,
                                                         encoding="utf-8")
        rotate_fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)8s - %(message)s"))
        logger.addHandler(rotate_fh)
        return logger
    except Exception as err:
        print(f"Faced unexpected : {err}")
        raise err

if __name__ == "__main__":
    log_path = Path(__file__).parent / "files/rotated-logs.log"
    svc_logger = configure_rotating_logger(logger_name="kubernetes_logs", 
                                           log_filepath=str(log_path), 
                                            max_size_bytes=1024,
                                             backup_count=2)
    for i in range(200):
        svc_logger.info(f"Checking status of component {i}.")