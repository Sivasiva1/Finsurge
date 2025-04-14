import logging 

logger = logging.basicConfig(filename="exception.log" ,level=logging.DEBUG,
                             format="%(asctime)s - %(levelname)s - %(message)s")
try:
     a = 10 / 0 
except Exception as e :
     logging.error("Zero Division Error ",exc_info=True) 
    