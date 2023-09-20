import os
import sys
import glob
import xml.etree.ElementTree as ET
import numpy as np
import sys
sys.path.append("/root/huanggua/ultralytics-main")
from ...datasets.data_config import get_train_data
from PIL import  Image

# TRAIN, VAL or TEST folder
origin_img_folder = "TRAIN"
origin_label_folder = "TRAIN"
classes = ["Brain tumor"]

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = round(x * dw ,2)
    w = round(w * dw,2)
    y = round(y * dh,2)
    h = round(h * dh,2)
    return (x, y, w, h)

def progress(percent,width=100):
    if percent > 1:
        percent=1
    show_str=('[%%-%ds]' %width) %(int(percent*width)*'#')
    print('\r%s %s%%' %(show_str,int(percent*100)),end='',file=sys.stdout,flush=True)

def convert_annotation(ffile,image_id):
    out_file = open(get_train_data() + origin_label_folder + '/%s.txt' % (image_id), 'w')
    image = Image.open(os.path.join(get_train_data(),origin_img_folder,'%s.jpg' % (image_id)))
    w = image.width
    h = image.height

    try:
        cls_id = '0'
        for obj in ffile['regions']:
            if obj['shape_attributes']['name'] == 'ellipse':
                center = obj['shape_attributes']['cx'], obj['shape_attributes']['cy']
                axes =  obj['shape_attributes']['rx'], obj['shape_attributes']['ry']
                angle = obj['shape_attributes']['theta']

                width = int(axes[0] * 2)
                height = int(axes[1] * 2)
                b = (int(center[0] - width/2), int(center[0] + width/2), int(center[1] - height/2), int(center[1] + height/2))

            else:
                px = np.array(obj['shape_attributes']['all_points_x'])
                py = np.array(obj['shape_attributes']['all_points_y'])

                b = (min(px), max(px), min(py), max(py))
            bb = convert((w, h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    except:
        print(image_id)
        pass
import shutil
import json

if __name__ == "__main__":
    current = 0
    with open(os.path.join(get_train_data(),origin_img_folder,"annotations_val.json")) as file:
        data = json.load(file)

    for file in data.items():
        current +=1
        image_id = file[1]['filename'].split(".")[0]
        convert_annotation(file[1],image_id)


