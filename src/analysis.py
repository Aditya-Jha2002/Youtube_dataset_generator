from concurrent.futures import ThreadPoolExecutor
from utils.cfg import CFG
from utils.analysis import Analysis
import os
from tqdm import tqdm

save_path = CFG.save_path
analysis = Analysis(save_path)

caption_paths = os.listdir(analysis.sub_save_path)

with ThreadPoolExecutor(max_workers=8) as executor:
    return_pair = list(
        tqdm(
            executor.map(analysis.get_caption_stats, caption_paths),
            total=len(caption_paths),
        )
    )

subtitles = []
timestamps = []
for pair in return_pair:
    subtitle, timestamp = pair
    subtitles.append(subtitle)
    timestamps.append(timestamp)

# subtitles = [subtitle for subtitle in subtitles]
subtitle_corpus = " ".join(subtitles)

with open(analysis.data_stats_path + "subtitle_corpus.txt", "w") as f:
    f.write(subtitle_corpus)

with open(analysis.data_stats_path + "time_stamp.txt", "w") as f:
    for timestamp in timestamps:
        f.write(timestamp + "\n")