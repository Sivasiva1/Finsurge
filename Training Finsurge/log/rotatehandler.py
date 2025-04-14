import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=3)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger = logging.getLogger("RotatingLogger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

for i in range(100):
    logger.info(f"Logging message {i}")
