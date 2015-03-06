import logging
from little.bits import configs

__author__ = 'charlie'
logging.basicConfig(filename=configs.log_file,level=configs.logging_level)


def log(message, level=logging.INFO):
    print(message)
    if level is logging.INFO or level is logging.NOTSET:
        logging.info(message)
    elif level is logging.DEBUG:
        logging.debug(message)
    elif level is logging.WARN or level is logging.WARNING:
        logging.warn(message)
    if level is logging.ERROR:
        logging.error(message)
    elif level is logging.CRITICAL:
        logging.critical(message)
    elif level is logging.FATAL:
        logging.fatal(message)