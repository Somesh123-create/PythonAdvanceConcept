import logging

#basic logging config
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%m-%Y %H:%M:%S %p')
#
# logging.debug("this is debug")
# logging.info("this is info")
# logging.error("this is error")
# logging.warning("this is warning")
# logging.critical("this is critical")

#config log handler to send log to handler

logger = logging.getLogger(__name__)
#create handler
strem_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#level and formate
strem_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formater = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
strem_h.setFormatter(formater)
file_h.setFormatter(formater)

logger.addHandler(strem_h)
logger.addHandler(file_h)

logger.warning("this is warning")
logger.error("this is error")
