# Official BGFG-YOLO
This is the source code for the paper, "BGF-YOLO: Enhanced YOLOv8 with Multiscale Attentional Feature Fusion for Brain Tumor Detection", of which I am the first author.

## Model
The model configuration (i.e., network construction) file is bgf-yolo.yaml in the directory [./cfg/models/bgf](https://github.com/mkang315/BGF-YOLO/blob/main/cfg/models/bgf/bgf-yolo.yaml).

#### Training

The hyperparameter setting file is default.yaml in the directory [./cfg/](https://github.com/mkang315/BGF-YOLO/blob/main/cfg/default.yaml).

###### Training CLI
```
python yolo/bgf/detect/train.py
```

#### Testing CLI

```
python yolo/bgf/detect/predict.py
```

## Evaluation
We trained and evaluated BGF-YOLO on the dataset [Br35H :: Brain Tumor Detection 2020](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection)..

## Suggested Citation
Our manuscript has been uploaded on [arXiv](https://arxiv.org/abs/2309.). Please cite our paper if you use code from this repository:
> Plain Text

- *IEEE* Style</br>
M. Kang, C.-M. Ting, F. F. Ting, and R. C.-W. Phan, "BGF-YOLO: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection," arXiv:2309. [cs.CV], Jun. 2023.</br>

- *Nature* Style</br>
Kang, M., Ting, C.-M., Ting, F. F. & Phan, R. C.-W. BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. Preprint at https://arxiv.org/abs/2309. (2023).</br>

- *Springer* Style</br>
Kang, M., Ting, C.-M., Ting, F. F., Phan, R.C.-W.: BGF-YOLO: BGFG-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. arXiv preprint [arXiv:2309.](https://arxiv.org/abs/2309.) (2023)</br>

## License
BGF-YOLO is released under the GNU Affero General Public License v3.0 (AGPL-3.0). Please see the [LICENSE](https://github.com/mkang315/BGF-YOLO/blob/main/LICENSE) file for more information.

## Copyright Notice
Many utility codes of our project base on the codes of [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics), [GiraffeDet](https://github.com/damo-cv/GiraffeDet) and [BiFormer](https://github.com/rayleizhu/BiFormer) repositories.