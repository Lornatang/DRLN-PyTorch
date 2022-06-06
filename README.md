# DRLN-PyTorch

## Overview

This repository contains an op-for-op PyTorch reimplementation of [Densely Residual Laplacian Super-Resolution](https://arxiv.org/abs/1906.12021v2).

## Table of contents

- [DRLN-PyTorch](#drln-pytorch)
    - [Overview](#overview)
    - [Table of contents](#table-of-contents)
    - [Download weights](#download-weights)
    - [Download datasets](#download-datasets)
    - [How Test and Train](#how-test-and-train)
        - [Test](#test)
        - [Train model](#train-model)
        - [Resume train model](#resume-train-model)
    - [Result](#result)
    - [Contributing](#contributing)
    - [Credit](#credit)
        - [Densely Residual Laplacian Super-Resolution](#densely-residual-laplacian-super-resolution)

## Download weights

- [Google Driver](https://drive.google.com/drive/folders/17ju2HN7Y6pyPK2CC_AqnAfTOe9_3hCQ8?usp=sharing)
- [Baidu Driver](https://pan.baidu.com/s/1yNs4rqIb004-NKEdKBJtYg?pwd=llot)

## Download datasets

Contains DIV2K, DIV8K, Flickr2K, OST, T91, Set5, Set14, BSDS100 and BSDS200, etc.

- [Google Driver](https://drive.google.com/drive/folders/1A6lzGeQrFMxPqJehK9s37ce-tPDj20mD?usp=sharing)
- [Baidu Driver](https://pan.baidu.com/s/1o-8Ty_7q6DiS3ykLU09IVg?pwd=llot)

Please refer to `README.md` in the `data` directory for the method of making a dataset.

## How Test and Train

Both training and testing only need to modify the `config.py` file. 

### Test

- line 31: `upscale_factor` change to `2`.
- line 33: `mode` change to `test`.
- line 70: `model_path` change to `results/pretrained_models/DRLN_BIX2-DIV2K-5346a619.pth.tar`.

### Train model

- line 31: `upscale_factor` change to `2`.
- line 33: `mode` change to `train`.
- line 35: `exp_name` change to `DRLN_BIX2`.

### Resume train model

- line 31: `upscale_factor` change to `2`.
- line 33: `mode` change to `train`.
- line 35: `exp_name` change to `DRLN_BIX2`.
- line 48: `resume` change to `samples/DRLN_BIX2/epoch_xxx.pth.tar`.

## Result

Source of original paper results: [https://arxiv.org/pdf/1906.12021v2.pdf](https://arxiv.org/pdf/1906.12021v2.pdf)

In the following table, the psnr value in `()` indicates the result of the project, and `-` indicates no test.

| Method | Scale |          Set5 (PSNR/SSIM)           |          Set14(PSNR/SSIM)           |          BSD100(PSNR/SSIM)          |         Urban100(PSNR/SSIM)         |         Manga109(PSNR/SSIM)         |
|:------:|:-----:|:-----------------------------------:|:-----------------------------------:|:-----------------------------------:|:-----------------------------------:|:-----------------------------------:|
|  DRLN  |   2   | 38.27(**38.17**)/0.9616(**0.9618**) | 34.28(**33.83**)/0.9231(**0.9204**) | 32.47(**32.27**)/0.9032(**0.9017**) | 33.54(**32.64**)/0.9332(**0.9332**) | 39.75(**38.87**)/0.9792(**0.9779**) |
|  DRLN  |   3   | 34.78(**34.50**)/0.9303(**0.9287**) | 30.73(**30.29**)/0.8488(**0.8415**) | 29.36(**29.09**)/0.8117(**0.8066**) | 29.21(**28.29**)/0.8722(**0.8557**) | 34.71(**33.35**)/0.9509(**0.9446**) |
|  DRLN  |   4   | 32.63(**32.36**)/0.9002(**0.8979**) | 28.94(**28.65**)/0.7900(**0.7836**) | 27.83(**27.61**)/0.7444(**0.7388**) | 26.98(**26.31**)/0.8119(**0.7929**) | 31.54(**30.43**)/0.9196(**0.9088**) |
|  DRLN  |   8   | 27.36(**27.21**)/0.7882(**0.7827**) | 25.34(**25.01**)/0.6531(**0.6433**) | 25.01(**24.86**)/0.6057(**0.6001**) |     23.06(**-**)/0.64712(**-**)     | 25.29(**24.70**)/0.8041(**0.7861**) |

Low resolution / Recovered High Resolution / Ground Truth
<span align="center"><img src="figure/result.png"/></span>

## Contributing

If you find a bug, create a GitHub issue, or even better, submit a pull request. Similarly, if you have questions,
simply post them as GitHub issues.

I look forward to seeing what the community does with these models!

## Credit

### Densely Residual Laplacian Super-Resolution

_Saeed Anwar, Nick Barnes_ <br>

**Abstract** <br>
Super-Resolution convolutional neural networks have recently demonstrated high-quality restoration for single images.
However, existing algorithms often require very deep architectures and long training times. Furthermore, current
convolutional neural networks for super-resolution are unable to exploit features at multiple scales and weigh them
equally, limiting their learning capability. In this exposition, we present a compact and accurate super-resolution
algorithm namely, Densely Residual Laplacian Network (DRLN). The proposed network employs cascading residual on the
residual structure to allow the flow of low-frequency information to focus on learning high and mid-level features. In
addition, deep supervision is achieved via the densely concatenated residual blocks settings, which also helps in
learning from high-level complex features. Moreover, we propose Laplacian attention to model the crucial features to
learn the inter and intra-level dependencies between the feature maps. Furthermore, comprehensive quantitative and
qualitative evaluations on low-resolution, noisy low-resolution, and real historical image benchmark datasets illustrate
that our DRLN algorithm performs favorably against the state-of-the-art methods visually and accurately.

[[Paper]](https://arxiv.org/pdf/1906.12021v2) [[Code(PyTorch)]](https://github.com/saeed-anwar/DRLN)

```bibtex
@article{anwar2019drln,
    title={Densely Residual Laplacian Super-Resolution},
    author={Anwar, Saeed and Barnes, Nick},
    journal={IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)},
    year={2020}
}
```
