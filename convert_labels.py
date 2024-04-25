# coding=utf-8
import os
import cv2
from tqdm import tqdm
import numpy as np


def data_split():
    img_size = 256
    a = ["1985", "1990", "1995", "2000", "2005", "2010", "2015", "2020"]
    for ai in a:
        path = "./GLC_old/GLC_FCS30_{}_E100N50.tif".format(ai)
        print(path)
        img = cv2.imread(path, cv2.COLOR_GRAY2RGB)
        for len in range(img.shape[0] // img_size):
            lin = img[
                len * img_size : (len + 1) * img_size,
                len * img_size : (len + 1) * img_size,
            ]
            cv2.imwrite(
                "./GLC/"
                + ai
                + "_"
                + str(len * img_size)
                + "_"
                + str((len + 1) * img_size)
                + ".jpg",
                lin,
            )


def data_make_label():
    save_path = "./GLC_label/"
    data_path = "./GLC/"
    limgs = os.listdir(data_path)
    # pixel_list=[10,11,20,120,121,122,130,140,150,152,153,180,190,200,201,2022,210,220,250]
    pixel_list = [180, 210]
    pd = tqdm(total=len(limgs))

    for item in limgs:
        pd.update(1)
        if item[:4] == "2020":
            continue
        lin_item = str(int(item[:4]) + 5) + item[4:]
        # lin_item=item
        img = cv2.imread(data_path + lin_item, cv2.COLOR_GRAY2RGB)
        # label=np.ones(img.shape)*255
        label = np.zeros(img.shape) * 255
        for pixel in pixel_list:
            for i, j in np.argwhere(img == pixel):
                label[i, j] = 255
        if len(np.where(label == 255)[0]) != 0:
            # print(len(np.where(label==255)[0]))
            cv2.imwrite(save_path + "label_" + item, label)
        else:
            continue
    pd.close()


if __name__ == "__main__":
    # 第一步
    data_split()
    # 第二步
    data_make_label()
