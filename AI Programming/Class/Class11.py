import logging

logging.basicConfig(filename = 'mylog.txt', level=logging.DEBUG)

def add(a,b):
    ret = a+b
    logging.debug(f"debug: {ret}")    
    logging.info(f"info: {ret}")
    logging.warning(f"warning: {ret}")
    logging.error(f"error: {ret}")
    logging.critical(f"critical: {ret}")
    return ret

add(10,20)