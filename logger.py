import logging


class Logger:

    """Logger to be used in multiple modules"""

    def __init__(self, name, level):
        # Logger for this module
        self.log = logging.getLogger(name)
        self.log.setLevel(level)

        # Handler for logger
        file_handler = logging.FileHandler(filename=name+'-debug.log', encoding='utf-8', mode='w')
        file_handler.setLevel(level=logging.DEBUG)

        # Formatters for handlers
        file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)

        # Add handlers to logger
        self.log.addHandler(file_handler)
