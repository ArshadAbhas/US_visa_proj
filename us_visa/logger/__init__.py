import logging
import os
from from_root import from_root
from datetime import datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'
logs_path = os.path.join(from_root(),log_dir)
os.makedirs(logs_path, exist_ok=True)

logs_path = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(
    filename=logs_path,
    level=logging.INFO,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)