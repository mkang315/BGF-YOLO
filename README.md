# Official BGF-YOLO
<div style="display:flex;justify-content: center">
<a href="https://github.com/mkang315/BGF-YOLO"><img src="https://img.shields.io/static/v1?label=GitHub&message=Code&color=black&logo=github"></a>
<a href="https://github.com/mkang315/BGF-YOLO"><img alt="Build" src="https://img.shields.io/github/stars/mkang315/BGF-YOLO"></a> 
<a href="https://huggingface.co/mkang315/BGF-YOLO"><img src="https://img.shields.io/static/v1?label=%F0%9F%A4%97%20Hugging%20Face&message=Model&color=yellow"></a>
<a href="https://arxiv.org/abs/2309.12585"><img alt="Build" src="https://img.shields.io/badge/arXiv%20paper-2309.12585-b31b1b.svg"></a>
</div>

## Description
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

## Referencing Guide
Please cite the paper if using this repository. Here is a guide to referencing this work in various styles for formatting your references:</br>

> Plain Text</br>
- **Springer Reference Style**</br>
Kang, M., Ting, C.-M., Ting, F.F., Phan, R.C.-W.: BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In: Linguraru, M.G., et al. (eds.) MICCAI 2024. LNCS, vol. 15008, pp. 35–45. Springer, Cham (2024). https://doi.org/10.1007/978-3-031-72111-3_4</br>
<sup>**NOTE:** *MICCAI* and *ECCV* conference proceedings are part of the book series LNCS in which Springer's format for bibliographical references is strictly enforced. This is important, for instance, when citing previous *MICCAI* and *ECCV* proceedings. LNCS stands for Lecture Notes in Computer Science.</sup>

- **Nature Reference Style**</br>
Kang, M., Ting, C.-M., Ting, F. F. & Phan, R. C.-W. BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6–10, 2024, Proceedings, Part VIII* (eds. Linguraru, M. G. et al.) 35–45 (Springer, 2024).</br>

- **Elsevier Numbered Style**</br>
M. Kang, C.-M. Ting, F.F. Ting, R.C.-W. Phan, BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection, in: M.G. Linguraru, Q. Dou, A. Feragen, S. Giannarou, B. Glocker, K. Lekadir, et al. (Eds.), Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6–10, 2024, Proceedings, Part VIII, Lecture Notes in Computer Science (LNCS), vol. 15008, 2024, pp. 35–45.</br>
<sup>**NOTE:** Day(s) Month Year, City, Abbrev. State, Country of Conference, Publiser, and Place of Publication are optional and omitted. Alterative version of the booktitle, series and volume is 'Proceedings of the 27th International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI), Vol. 15008 of Lecture Notes in Computer Science (LNCS),'.</sup>

- **Elsevier Name–Date (Harvard) Style**</br>
Kang, M., Ting, C.-M., Ting, F.F., Phan, R.C.-W., 2024. BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In: M.G. Linguraru, Q. Dou, A. Feragen, S. Giannarou, B. Glocker, K. Lekadir, et al. (Eds.), Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6–10, 2024, Proceedings, Part VIII. Vol. 15008 of Lecture Notes in Computer Science (LNCS), Springer, Cham, Germany, pp. 35–45.</br>
<sup>**NOTE:** Day(s) Month Year, City, Abbrev. State, Country of Conference, Publiser, and Place of Publication are optional. Alterative version of the booktitle, Day(s) Month Year, City, and Country of Conference is 'Proceedings of the 27th International Conference on Medical Image Computing and Computer Assisted Intervention (MICCAI), 6–10 October 2024, Marrakesh, Morocco.'.</sup>

- **Elsevier Vancouver Style**</br>
Kang M, Ting C-M, Ting FF, Phan RC-W. BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In: Linguraru MG, Dou Q, Feragen A, Giannarou S, Glocker B, Lekadir K, et al., editors. Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6–10, 2024, Proceedings, Part VIII. Lecture Notes in Computer Science (LNCS), Vol. 15008. Cham: Springer; 2024. p. 35–45.</br>

- **Elsevier Embellished Vancouver Style**</br>
Kang M, Ting C-M, Ting FF, Phan RC-W. BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In: Linguraru MG, Dou Q, Feragen A, Giannarou S, Glocker B, Lekadir K, et al., editors. *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6–10, 2024, Proceedings, Part VIII*. *Lecture Notes in Computer Science (LNCS)*, Vol. 15008. Cham: Springer; 2024. p. 35–45.</br>

- **IEEE Reference Style**</br>
M. Kang, C.-M. Ting, F. F. Ting, and R. C.-W. Phan, "Bgf-yolo: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection," in *Proc. Int. Conf. Med. Image Comput. Comput. Assist. Interv. (MICCAI)*, Marrakesh, Morocco, Oct. 6–10, 2024, vol. 15008, pp. 35–45.</br>
<sup>**NOTE:** City of Conf., Abbrev. State, Country, Month & Day(s) are optional.</sup>

- **IEEE Full Name Reference Style**</br>
Ming Kang, Chee-Ming Ting, Fung Fung Ting, and Raphaël C.-W. Phan. Bgf-yolo: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection. In *MICCAI*, vol. 15008, pages 35–45, 2024.</br>
<sup>**NOTE:** This is a modification to the standard IEEE Reference Style and used by most IEEE/CVF conferences, including *CVPR*, *ICCV*, and *WACV*, to render first names in the bibliography as "Firstname Lastname" rather than "F. Lastname" or "Lastname, F.".</sup></br>
&nbsp;- **IJCAI Full Name-Year Variation**</br>
\[Kang *et al.*, 2024\] Ming Kang, Chee-Ming Ting, Fung Fung Ting, and Raphaël C.-W. Phan. Bgf-yolo: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection. In *Proceedings of the 27th International Conference on Medical Image Computing and Computer-Assisted Intervention*, vol. 15008, pages 35–45, Cham, Germany, October 2024. Springer.</br>
&nbsp;- **ACL Full Name-Year Variation**</br>
Ming Kang, Chee-Ming Ting, Fung Fung Ting, and Raphaël C.-W. Phan. 2024. Bgf-yolo: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection. In *Proceedings of the 27th International Conference on Medical Image Computing and Computer-Assisted Intervention*, vol. 15008, pages 35–45, Cham, Germany. Springer.</br>

- **APA7 (Author–Date) Style**</br>
Kang, M., Ting, C.-M., Ting, F. F., & Phan, R. C.-W. (2024). BGF-YOLO: Enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In M.G. Linguraru, Q. Dou, A. Feragen, S. Giannarou, B. Glocker, K. Lekadir, J. A. Schnabel (Eds.), *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6–10, 2024, Proceedings, Part VIII* (pp. 35–45). Springer. https://doi.org/10.1007/978-3-031-72111-3_4</br>
&nbsp;- **ICML (Author–Year) Variation**</br>
Kang, M., Ting, C.-M., Ting, F. F., and Phan, R. C.-W. BGF-YOLO: Enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In M.G. Linguraru, Q. Dou, A. Feragen, S. Giannarou, B. Glocker, K. Lekadir, J. A. Schnabel (Eds.), *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6–10, 2024, Proceedings, Part VIII*, pp. 35–45, Cham, Germany, 2024. Springer.</br>
<sup>**NOTE:** For *NeurIPS* and *ICLR*, any reference/citation style is acceptable as long as it is used consistently. The sample of references in Formatting Instructions For NeurIPS almost follows APA7 (author–date) style and that in Formatting Instructions For ICLR Conference Submissions is similar to IJCAI full name-year variation.</sup>

> BibTeX Format</br>
```
\begin{thebibliography}{1}
\bibitem{Kang24Bgfyolo} Kang, M., Ting, C.-M., Ting, F.F., Phan, R.C.-W.: BGF-YOLO: enhanced YOLOv8 with multiscale attentional feature fusion for brain tumor detection. In: Linguraru, M.G., et al. (eds.) MICCAI 2024. LNCS, vol. 15008, pp. 35--45. Springer, Cham (2024). {\UrlFont https://doi.org/10.1007/978-3-031-72111-3\_4}
\end{thebibliography}
```
```
@inproceedings{Kang24Bgfyolo,
  author = "Kang, Ming and Ting, Chee-Ming and Ting, Fung Fung and Phan, Rapha{\"e}l C.-W.",
  title = "{BGF-YOLO}: enhanced {YOLO}v8 with multiscale attentional feature fusion for brain tumor detection",
  editor = "Linguraru, Marius George and others",
  % editor = "Linguraru, Marius George and Dou, Qi and Feragen, Aasa and Giannarou, Stamatia and Glocker, Ben and Lekadir, Karim and et al." %% Elsevier Style
  booktitle = "Medical Image Computing and Computer-Assisted Intervention – MICCAI 2024: 27th International Conference, Marrakesh, Morocco, October 6--10, 2024, Proceedings, Part VIII",
  series = "Lecture Notes in Computer Science (LNCS)",
  volume = "15008",
  pages = "35--45",
  publisher = "Springer",
  address = "Cham",
  year = "2024",
  doi= "10.1007/978-3-031-72111-3_4",
  url = "https://doi.org/10.1007/978-3-031-72111-3_4"
}
```
```
@inproceedings{Kang24Bgfyolo,
  author = "Ming Kang and Chee-Ming Ting and Fung Fung Ting and Rapha{\"e}l C.-W. Phan",
  title = "Bgf-yolo: Enhanced yolov8 with multiscale attentional feature fusion for brain tumor detection",
  booktitle = "Proc. Int. Conf. Med. Image Comput. Comput. Assist. Interv. (MICCAI)",
  % booktitle = MICCAI, %% IEEE Full Name Reference Style
  address = "Marrakesh, Morocco, Oct. 6--10",
  volume = "15008",
  pages = "35--45",
  year = "2024"
}
```
<sup>**NOTE:** Please remove some optional *BibTeX* fields/tags such as `series`, `volume`, `address`, `url`, and so on if the *LaTeX* compiler produces an error. Author names may be manually modified if not automatically abbreviated by the compiler under the control of the bibliography/reference style (i.e., .bst) file. The *BibTex* citation key may be `bib1`, `b1`, or `ref1` when references appear in numbered style in which they are cited. `others` in the `author` and `editor` may be `et al.` under some bibliography style files, such as IEEEtran.bst. The quotation mark pair `""` in the field could be replaced by the brace `{}`, whereas the brace `{}` in the *BibTeX* field/tag `title` plays a role of keeping letters/characters/text original lower/uppercases or sentence/capitalized cases unchanged while using Springer Nature bibliography style files, for example, sn-nature.bst.</sup>

## License
BGF-YOLO is released under the GNU Affero General Public License v3.0 (AGPL-3.0). Please see the [LICENSE](https://github.com/mkang315/BGF-YOLO/blob/main/LICENSE) file for more information.

## Copyright Notice
Many utility codes of our project base on the codes of [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics), [GiraffeDet](https://github.com/damo-cv/GiraffeDet), [DAMO-YOLO](https://github.com/tinyvision/DAMO-YOLO), and [BiFormer](https://github.com/rayleizhu/BiFormer) repositories.
