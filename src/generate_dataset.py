import os
from tqdm import tqdm
from utils.cfg import CFG
from utils.download import Download
from utils.link import Link
from concurrent.futures import ThreadPoolExecutor

# save_path = "/Users/sunita/Documents/projects/sign_dataset/data"
save_path = CFG.save_path

download = Download(save_path)
links = Link()

links = links.get_links(download.link_path)


if CFG.cont == True:
    download.generate_done()

    with open(os.path.join(save_path,"done.txt"), "r") as f_read:
        done_links = [link for link in f_read]

    links = [link for link in links if link not in done_links]

with ThreadPoolExecutor(max_workers=8) as executor:
    return_pair = list(
        tqdm(executor.map(download.generate_video_and_captions, links), total=len(links))
    )