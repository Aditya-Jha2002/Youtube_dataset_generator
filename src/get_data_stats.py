from concurrent.futures import ThreadPoolExecutor
from utils.cfg import CFG
from utils.utils import Utils
import os
from tqdm import tqdm

save_path = CFG.save_path
# save_path = "/Users/sunita/Documents/projects/sign_dataset/data"
utils = Utils(save_path)

caption_path = os.path.join(save_path, "captions")
caption_paths = os.listdir(caption_path)

def get_subtitle(cap_path):
    with open(os.path.join(caption_path, cap_path), "r") as f:
        lines = [line.strip() for line in f]
        subtitle = " ".join(lines[2::4])
        return subtitle


with ThreadPoolExecutor(max_workers=8) as executor:
    subtitles = list(
        tqdm(executor.map(get_subtitle, caption_paths), total=len(caption_paths))
    )

all_subtitle = [subtitle for subtitle in subtitles]
caption_corpus = " ".join(all_subtitle)

with open(save_path + "corpus.txt", "w") as f:
    f.write(caption_corpus)
