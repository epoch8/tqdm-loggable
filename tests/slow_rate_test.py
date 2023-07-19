import time
import logging
from tqdm_loggable.auto import tqdm

logging.basicConfig(level=logging.INFO)


sleeps = [8, 2, 7, 3, 4, 6, 8, 2, 7, 3]


for i in tqdm(sleeps):
    time.sleep(i)
