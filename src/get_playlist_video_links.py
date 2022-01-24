from pytube import Playlist
from utils.cfg import CFG
import os

save_path = CFG.save_path
link_path = os.path.join(save_path, "links.txt")
videolinks = []
playlists = CFG.playlists
for playlist in playlists:
    playlist_link = "https://www.youtube.com/playlist?list=" + playlist
    p = Playlist(playlist_link)
    for url in p.video_urls:
        videolinks.append(url)

with open(link_path, "w") as f_out:
    urls = set(videolinks)
    for url in urls:
        f_out.write(url + "\n")