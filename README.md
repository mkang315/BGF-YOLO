# Official BGF-YOLO
This is the source code for the paper, "BGF-YOLO: Enhanced YOLOv8 with Multiscale Attentional Feature Fusion for Brain Tumor Detection", early accepted by the 27th International Conference on Medical Image Computing and Computer Assisted Intervention ([MICCAI 2024](https://conferences.miccai.org/2024/en)), of which I am the first author. The paper is available to download from [Springer](https://link.springer.com/content/pdf/10.1007/978-3-031-72111-3_4) or [arXiv](https://arxiv.org/pdf/2309.12585).

## Model
The Bilevel routing attention, Generalized feature pyramid networks, and Fourth detecting head You Only Look Once (BGF-YOLO) model configuration (i.e., network construction) file is bgf-yolo.yaml in the directory [./models/bgf](https://github.com/mkang315/BGF-YOLO/blob/main/models/bgf).

The hyperparameter setting file is default.yaml in the directory [./yolo/cfg/](https://github.com/mkang315/BGF-YOLO/blob/main/yolo/cfg).

#### Installation
Install requirements.txt in a Python >= 3.8 environment, including PyTorch >= 1.8.
```
pip install -r requirements.txt
```

#### Training CLI
```
python yolo/bgf/detect/train.py
```

#### Testing CLI

```
python yolo/bgf/detect/predict.py
```

## Evaluation
We trained and evaluated BGF-YOLO on the dataset [Br35H :: Brain Tumor Detection 2020](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection). The .txt format annotations in the file [dataset-Br35H.zip](https://github.com/mkang315/BGF-YOLO/blob/main/dataset-Br35H.zip) are coverted from original json format.

<!--
| Model | Precision | Recall | mAP<sub>50</sub> | mAP<sub>50:95</sub> |
| :-------: | :-------: | :-------: | :-------: | :-------: |
| [RT-DETR-X](https://github.com/ultralytics/ultralytics/tree/main/ultralytics/cfg/models/rt-detr) | 0.825 | 0.770 | 0.870 | 0.597 |
| [Co-DETR with Swin L (36 Epochs, DETR Augmentation)](https://github.com/Sense-X/Co-DETR) | – | – | 0.941 | 0.609 |
| [YOLOv9-E](https://github.com/WongKinYiu/yolov9) | **0.927** | 0.869 | 0.919 | 0.630 |
| [YOLOv10-X](https://github.com/THU-MIG/yolov10) | 0.916 | 0.808 | 0.880 | 0.603 |
| **BGF-YOLO (Ours)** | 0.919 | **0.926** | **0.974** | **0.653** |

## Generalizability in External Validation
We conducted additional experimental validation on a different domain using the [COVID-19 facemask detection dataset](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection). The table below consistently shows the superior detection performance of our method compared to YOLOv8x. This indicates the generalizability of our method to other domains of object detection.

| Model | Precision | Recall | mAP<sub>50</sub> | mAP<sub>50:95</sub> |
| :-------: | :-------: | :-------: | :-------: | :-------: |
| YOLOv8x | 0.866 | 0.773 | 0.802 | 0.494 |
| **BGF-YOLO (Ours)** | 0.847 | 0.764 | **0.820** | **0.504** |

## Suggested Citation
Our manuscript has been uploaded on [arXiv](https://arxiv.org/abs/2309.12585). Please cite our paper if you use code from this repository:
> Plain Text

- *IEEE* Style</br>
M. Kang, C.-M. Ting, F. F. Ting, and R. C.-W. Phan, "Bgf-yolo: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection," arXiv:2309.12585 [cs.CV], Jun. 2023.</br>

- *Nature* Style</br>
Kang, M., Ting, C.-M., Ting, F. F. & Phan, R. C.-W. BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. Preprint at https://arxiv.org/abs/2309.12585 (2023).</br>

- *Springer* Style</br>
Kang, M., Ting, C.-M., Ting, F. F., Phan, R.C.-W.: BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. arXiv preprint [arXiv:2309.12585](https://arxiv.org/abs/2309.12585) (2023)</br>
-->
## Referencing Guide
Please cite our paper if you use code from this repository. Here is a guide to referencing this work in various styles for formatting your references:
> Plain Text

- Springer Reference Style</br>
Kang, M., Ting, C.-M., Ting, F.F., Phan, R.C.-W.: BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In: Linguraru, M.G., et al. (eds.) MICCAI 2024. LNCS, vol. 15008, 35–45. Springer, Cham (2024). https://doi.org/10.1007/978-3-031-72111-3_4</br>
<sup>**NOTE:** MICCAI conference proceedings are part of the book series LNCS in which Springer's format for bibliographical references is strictly enforced. This is important, for instance, when citing previous MICCAI proceedings. LNCS stands for Lecture Notes in Computer Science.</sup>

- Nature Reference Style</br>
Kang, M., Ting, C.-M., Ting, F. F. & Phan, R. C.-W. BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6–10, 2024, Proceedings, Part VIII* (eds. Linguraru, M. G. et al.) 35–45 (Springer, 2024).</br>

- IEEE Reference Style</br>
M. Kang, C.-M. Ting, F. F. Ting, and R. C.-W. Phan, "Bgf-yolo: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection," in *Proc. Int. Conf. Med. Image Comput. Comput. Assist. Interv. (MICCAI)*, Marrakesh, Morocco, Oct. 6–10, 2024, pp. 35–45.</br>
<sup>**NOTE:** City of Conf., Abbrev. State, Country, Month & Day(s) are optional.</sup>

- Elsevier Numbered Style</br>
M. Kang, C.-M. Ting, F.F. Ting, R.C.-W. Phan, BGF-YOLO: Enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection, in: M.G. Linguraru, Q. Dou, A. Feragen, S. Giannarou, B. Glocker, K. Lekadir, et al. (Eds.), Proceedings of the 27th International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI), 6–10 October 2024, Marrakesh, Morocco, Springer, Cham, Germany, 2024, pp. 35–45.</br>
<sup>**NOTE:** Day(s) Month Year, City, Abbrev. State, Country of Conference, Publiser, and Place of Publication are optional.</sup>

- Harvard (Name–Date) Style</br>
Kang, M., Ting, C.-M., Ting, F.F., Phan, R.C.-W., 2024. BGF-YOLO: Enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In: M.G. Linguraru, Q. Dou, A. Feragen, S. Giannarou, B. Glocker, K. Lekadir, et al. (Eds.), Proceedings of the 27th International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI), 6–10 October 2024, Marrakesh, Morocco. Springer, Cham, Germany, pp. 35–45.</br>
<sup>**NOTE:** Day(s) Month Year, City, Abbrev. State, Country of Conference, Publiser, and Place of Publication are optional.</sup>

> BibTeX Format</br>
```
\begin{thebibliography}{1}
\bibitem{Kang24Bgfyolo} Kang, M., Ting, C.-M., Ting, F.F., Phan, R.C.-W.: BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In: Linguraru, M.G., et al. (eds.) MICCAI 2024. LNCS, vol. 15008, 35--45. Springer, Cham (2024). {\UrlFont https://doi.org/10.1007/978-3-031-72111-3\_4}
\end{thebibliography}
```
```
@inproceedings{Kang24Bgfyolo,
  author = "Kang, Ming and Ting, Chee-Ming and Ting, Fung Fung and Phan, Rapha{\"e}l C.-W.",
  title = "BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection",
  editor = "Linguraru, Marius George and et al.",
  booktitle = "Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6--10, 2024, Proceedings, Part VIII",
  series = "Lecture Notes in Computer Science (LNCS)",
  volume = "15008",
  pages = "35--45",
  publisher = "Springer",
  address = "Cham",
  year = "2024",
  doi= "10.1007/978-3-031-72111-3_4",
  url = "https://doi.org/10.1007/978-3-031-72111-3\_4"
}
```
```
@inproceedings{Kang24Bgfyolo,
  author = "Ming Kang and Chee-Ming Ting and Fung Fung Ting and Rapha{\"e}l C.-W. Phan",
  title = "Bgf-yolo: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection",
  booktitle = "Proc. Int. Conf. Med. Image Comput. Comput. Assist. Interv. (MICCAI)",
  address = "Marrakesh, Morocco, Oct. 6--10",
  pages = "35--45",
  year = "2024",
}
```
<sup>**NOTE:** Please remove some optional *BibTeX* fields, for example, `series`, `volume`, `address`, `url` and so on, while the *LaTeX* compiler produces an error. Author names may be manually modified if not automatically abbreviated by the compiler under the control of the .bst file if applicable which defines bibliography/reference style. `Kang24Bgfyolo` could be `b1`, `bib1`, or `ref1` when references appear in numbered style in which they are cited. The quotation mark pair `""` in the field could be replaced by the brace `{}`. </sup>

## License
BGF-YOLO is released under the GNU Affero General Public License v3.0 (AGPL-3.0). Please see the [LICENSE](https://github.com/mkang315/BGF-YOLO/blob/main/LICENSE) file for more information.

## Copyright Notice
Many utility codes of our project base on the codes of [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics), [GiraffeDet](https://github.com/damo-cv/GiraffeDet), [DAMO-YOLO](https://github.com/tinyvision/DAMO-YOLO), and [BiFormer](https://github.com/rayleizhu/BiFormer) repositories.
