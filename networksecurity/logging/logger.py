import logging
import os
from datetime import datetime

LOG_FILE = f"networksecurity_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logs_dir = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_dir), exist_ok=True)

logging.basicConfig(filename=logs_dir, level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
