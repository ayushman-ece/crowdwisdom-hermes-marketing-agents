import logging
import os

LOG_DIR = "outputs/logs"

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/system.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("CrowdWisdom")