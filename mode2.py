#how to add traceback in logging
import logging
import traceback
import logging.config
logging.config.fileConfig('logging.conf')

# Create a logger
logger = logging.getLogger('simpleExample')


def test1fun(a, b):
    try:
        res = a + b
        if res > 10:
            raise ValueError("result greater than 10")
    except Exception as e:
        logger.error(e, exc_info=True)
    else:
        logger.info(res)
    finally:
        logger.debug("Cleaning up..")


def using_traceback(a:list):
    try:
        val = a[10]
    except:
        logger.warning(f"Error: {traceback.format_exc()}")

using_traceback([1, 3, 4])
