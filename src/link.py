import csv
from tqdm import tqdm
from utils.cfg import CFG
from utils.download import Download
from utils.link import Link
from concurrent.futures import ThreadPoolExecutor

# save_path = "/Users/sunita/Documents/projects/sign_dataset/data"
save_path = CFG.save_path
download = Download(save_path)
links = Link()

video_urls = []
tags = CFG.tags
for tag in tqdm(tags,total=len(tags)):
    urls = links.gen_links_pl(tag)
    video_urls.extend(urls)

with open(download.link_path, "w") as f_out:
    urls = set(video_urls)
    for url in tqdm(urls,total=len(urls)):
        f_out.write(url + "\n")

with ThreadPoolExecutor(max_workers=8) as executor:
    return_pair = list(tqdm(executor.map(download._get_yt, urls), total=len(urls)))

with open(download.csv_path, "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    header = ("vid_id", "title")
    csv_writer.writerow(header)
    for pair in return_pair:
        yt, link_id, title = pair
        csv_writer.writerow((link_id, title))