import csv
from tqdm import tqdm
from utils.cfg import CFG
from utils.utils import Utils
from pytube import YouTube
import os
from concurrent.futures import ThreadPoolExecutor

# save_path = "/Users/sunita/Documents/projects/sign_dataset/data"
save_path = CFG.save_path

utils = Utils(save_path)

with open(os.path.join(save_path,"done.txt"), "r") as f_read:
    done_links = [link for link in f_read]

links = utils.get_links()
links = [link for link in links if link not in done_links]
print(len(links))


with ThreadPoolExecutor(max_workers=8) as executor:
    return_pair = list(
        tqdm(executor.map(utils.generate_video_and_captions, links), total=len(links))
    )