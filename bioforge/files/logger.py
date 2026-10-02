import logging
import os

def setup_logger(logger_file="output/bioforge.log"):
    """configure the shared 'bioforge' logger and return it. """
    #make sure the folder for the log file exists
    folder = os.path.dirname(logger_file)
    if folder != "":
        os.makedirs(folder , exist_ok=True)


    #get the shared logger and choose wich levels it records
    logger = logging.getLogger("bioforge")
    logger.setLevel(logging.WARNING)
        # if this file already has a handler, do not add another one
    full_path = os.path.abspath(logger_file)
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            if handler.baseFilename == full_path:
                return logger
    #write messages to the file (append mode, UTF-8)
    file_handler = logging.FileHandler(logger_file, mode="a", encoding="utf-8")

    #decide how each line looks
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger    