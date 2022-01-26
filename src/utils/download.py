import csv
from tqdm import tqdm
from utils.cfg import CFG
from pytube import YouTube
import os


class Download:
    def __init__(self, save_path):
        self.save_path = save_path
        self.vid_save_path = os.path.join(save_path, "videos")
        self.sub_save_path = os.path.join(save_path, "captions")
        self.link_path = os.path.join(save_path, "links.txt")
        self.csv_path = os.path.join(save_path, "watch_id_title.csv")

    def generate_video_and_captions(self, link):
            yt, link_id, title = self._get_yt(link)
            self._get_caption(yt, link_id)
            self._get_video(yt, link_id)
            return link_id, title

    def _get_yt(self, link):
        yt = YouTube(link)
        link_id = link.split("=")[-1]
        title = yt.title
        return yt, link_id, title

    def _get_caption(self, yt, link_id):
        captions = yt.captions

        if "en-IN" in captions:
            caption = yt.captions["en-IN"].generate_srt_captions()
        elif "en" in captions:
            caption = yt.captions["en"].generate_srt_captions()
        else:
            caption = "No caption"

        with open(os.path.join(self.sub_save_path, link_id + ".txt"), "w") as f_out:
            f_out.write(caption)

    def _get_video(self, yt, link_id):
        stream = yt.streams.filter(file_extension="mp4", res="720p", progressive=True).first()
        if stream != None:
            stream.download(self.vid_save_path, filename=link_id + ".mp4")

    def _read_get_watch_id_title(self):
        watch_id_title = {}
        with open(self.csv_path, "r") as f_in:
            reader = csv.DictReader(f_in)
            for row in reader:
                watch_id_title[row["title"]] = row["vid_id"]
        return watch_id_title

    def generate_done(self):
        vid_files = os.listdir(self.vid_save_path)
        vid_names = set([vid_file.split(".")[0] for vid_file in vid_files])
        with open(os.path.join(self.save_path,'done.txt'),'w') as f_in:
            for vid_name in vid_names:
                f_in.write('https://www.youtube.com/watch?v='+vid_name)


