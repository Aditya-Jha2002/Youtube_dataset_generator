from cfg import CFG
import os

# save_path = "/Users/sunita/Documents/projects/sign_dataset/data"
save_path = CFG.save_path
vid_path = os.path.join(save_path, "videos")
cap_path = os.path.join(save_path, "captions")

vid_names = os.listdir(vid_path)
cap_names = os.listdir(cap_path)
print("No of videos:", len(vid_names))
print("No of captions:", len(cap_names))
vid_names = set([vid_name.split(".")[0] for vid_name in vid_names])
cap_names = set([vid_name.split(".")[0] for vid_name in vid_names])

done_items = vid_names.intersection(cap_names)
print("No of tasks done:", len(done_items))

with open(os.path.join(save_path,'done.txt'),'w') as f_in:
    for vid_name in vid_names:
        f_in.write('https://www.youtube.com/watch?v='+vid_name)