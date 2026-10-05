import logging
import os

def setup_logger(logger_file="output/bioforge.log"):
    folder = os.path.dirname(logger_file)
    if folder != "":
        os.makedirs(folder, exist_ok=True)

    logger = logging.getLogger("bioforge")
    logger.setLevel(logging.WARNING)

    full_path = os.path.abspath(logger_file)
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            if handler.baseFilename == full_path:
                return logger

    file_handler = logging.FileHandler(logger_file, mode="a", encoding="utf-8")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
