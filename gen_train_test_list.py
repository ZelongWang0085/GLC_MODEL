import os
from tqdm import tqdm
import random
import shutil

color_img_path = "./GLC/"
label_img_path = "./GLC_label/"

limgs = os.listdir(label_img_path)


random.shuffle(limgs)

pd = tqdm(total=len(limgs))
i = 0
for limg in limgs:
    pd.update(1)
    if i >= int(len(limgs) * 0.8):
        src_name = "./GLC/" + limg.replace("label_", "")
        dst_name = "./data/train/images/imgs/" + limg.replace("label_", "")
        shutil.copyfile(src_name, dst_name)
        src_name = "./GLC_label/" + limg
        dst_name = "./data/train/masks/imgs/" + limg
        shutil.copyfile(src_name, dst_name)
    else:
        src_name = "./GLC/" + limg.replace("label_", "")
        dst_name = "./data/test/images/imgs/" + limg.replace("label_", "")
        shutil.copyfile(src_name, dst_name)
        src_name = "./GLC_label/" + limg
        dst_name = "./data/test/masks/imgs/" + limg
        shutil.copyfile(src_name, dst_name)
    i += 1
pd.close()
