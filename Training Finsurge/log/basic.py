import logging 

#priority -- > debug , info , warning , error , critical 
logging.basicConfig(level=logging.DEBUG)

logging.info("This is INFO logging")
logging.debug("This is DEBUG logging")
logging.error("This is ERROR logging")
logging.warning("This is WARNING logging")
logging.critical("This is CRITICAL logging") 
