import os
import csv
from pytube import Playlist
from utils.cfg import CFG


class Link:
    def gen_links_pl(self,tag):
        tag = "https://www.youtube.com/playlist?list=" + tag
        p = Playlist(tag)
        urls = [url for url in p.video_urls]
        return urls

    def get_links(self,link_path):
        with open(link_path, "r") as f_read:
            links = [link for link in f_read]
            return links

    def _read_get_watch_id_title(self,csv_path):
        watch_id_title = {}
        with open(csv_path, "r") as f_in:
            reader = csv.DictReader(f_in)
            for row in reader:
                watch_id_title[row["title"]] = row["vid_id"]
        return watch_id_title