import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')


for j in range(1000):
    logging.info(f"loop val: {j}")
