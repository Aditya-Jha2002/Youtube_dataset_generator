import csv
from tqdm import tqdm
from utils.cfg import CFG
from utils.utils import Utils
import os
from concurrent.futures import ThreadPoolExecutor
from pytube import YouTube

# save_path = "/Users/sunita/Documents/projects/sign_dataset/data"
save_path = CFG.save_path
vid_save_path = os.path.join(save_path, "videos")
cap_save_path = os.path.join(save_path, "captions")
link_path = os.path.join(save_path, "links.txt")
csv_path = os.path.join(save_path, "watch_id_title.csv")

utils = Utils(vid_save_path, cap_save_path, link_path)

links = utils.get_links()

with ThreadPoolExecutor(max_workers=8) as executor:
    return_pair = list(tqdm(executor.map(utils._get_yt, links), total=len(links)))

with open(csv_path, "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    header = ("vid_id", "title")
    csv_writer.writerow(header)
    for pair in return_pair:
        yt, link_id, title = pair
        csv_writer.writerow((link_id, title))
