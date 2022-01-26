from concurrent.futures import ThreadPoolExecutor
from utils.cfg import CFG
from utils.download import Download
import os

class Analysis():
    def __init__(self,save_path):
        self.sub_save_path = os.path.join(save_path,"captions")
        self.data_stats_path = os.path.join(save_path, "data_stats")

    def get_caption_stats(self, cap_path):
        with open(os.path.join(self.sub_save_path, cap_path), "r") as f:
            lines = [line.strip() for line in f]
            timestamp = " ".join(lines[1::4])
            subtitle = " ".join(lines[2::4])
            return subtitle, timestamp