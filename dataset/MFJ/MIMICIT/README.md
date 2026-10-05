---
language:
- en
- zh
- es
- ja
- fr
- ko
- ar
license: mit
size_categories:
- 1M<n<10M
pretty_name: 'MIMIC-IT: Multi-Modal In-Context Instruction Tuning'
arxiv: 2306.05425
extra_gated_prompt: "<h1>MIMIC-IT Dataset Download\nAgreement</h1>\n<p>S-Lab, Nanyang\
  \ Technological University (S-Lab) provides access to\nthe MIMIC-IT Dataset (referred\
  \ to as the Dataset) under the following\nconditions.</p>\n<p>By signing, the researcher\
  \ agrees to the following terms of use:</p>\n<ol type=\"1\">\n<li>S-Lab makes no\
  \ warranties regarding the Dataset, including but not\nlimited to being up-to-date,\
  \ correct or complete. S-Lab cannot be held\nliable for providing access to the\
  \ Dataset or usage of the Dataset.</li>\n<li>The Dataset should only be used for\
  \ scientific or research purposes.\nAny other use is explicitly prohibited.</li>\n\
  <li>The researcher agrees to the following terms and conditions of data\nsources\
  \ of the Dataset:\n<ul>\n  <li>TVC: <a href=\"https://tvqa.cs.unc.edu/\">https://tvqa.cs.unc.edu/</a></li>\n\
  \  <li>LLaVA: <a href=\"https://huggingface.co/datasets/liuhaotian/LLaVA-Instruct-150K\"\
  >https://huggingface.co/datasets/liuhaotian/LLaVA-Instruct-150K</a>; <a href=\"\
  https://cocodataset.org/#termsofuse\">https://cocodataset.org/#termsofuse</a></li>\n\
  \  <li>DC: <a href=\"http://activity-net.org/index.html\">http://activity-net.org/index.html</a></li>\n\
  \  <li>VIST: <a href=\"https://visionandlanguage.net/VIST/index.html\">https://visionandlanguage.net/VIST/index.html</a></li>\n\
  \  <li>SD: <a href=\"https://goo.gl/forms/HJiFJSllupqeCbax1\">https://goo.gl/forms/HJiFJSllupqeCbax1</a></li>\n\
  \  <li>Ego4D: <a href=\"https://ego4ddataset.com/\">https://ego4ddataset.com/</a></li>\n\
  </ul></li>\n<li>The researcher takes full responsibility for usage of the Dataset\
  \ at\nany time.</li>\n<li>S-Lab reserves the right to terminate the researcher's\
  \ access to the\nDataset at any time.</li>\n<li>The place of jurisdiction is Singapore.</li>\n\
  <li>If any part of this agreement is legally invalid, this shall not\naffect the\
  \ remaining agreement.</li>\n</ol>\n"
extra_gated_fields:
  Verifiable Name: text
  Institution Email: text
  Institutional Affiliation: text
  I agree with the agreement: checkbox
dataset_info:
- config_name: CGD
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: image
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 26335666892.75
    num_examples: 141869
  download_size: 13284595128
  dataset_size: 26335666892.75
- config_name: CGD_Images
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 10977030309.125
    num_examples: 118287
  download_size: 10976812684
  dataset_size: 10977030309.125
- config_name: CGD_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 42088070
    num_examples: 141869
  download_size: 14266985
  dataset_size: 42088070
- config_name: DC_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 718166107
    num_examples: 226242
  download_size: 50424022
  dataset_size: 718166107
- config_name: E4D_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 3647794122
    num_examples: 2729222
  download_size: 396261870
  dataset_size: 3647794122
- config_name: LACONV
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: image
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 13374859898.25
    num_examples: 256870
  download_size: 3096198512
  dataset_size: 13374859898.25
- config_name: LACONV_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 119528906
    num_examples: 256870
  download_size: 54731579
  dataset_size: 119528906
- config_name: LACR_I2I
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: image
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 4027892178.625
    num_examples: 76643
  download_size: 3988169106
  dataset_size: 4027892178.625
- config_name: LACR_I2I_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 89534975
    num_examples: 76643
  download_size: 42911696
  dataset_size: 89534975
- config_name: LACR_T2T
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: image
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 4028004669.625
    num_examples: 76643
  download_size: 3988281406
  dataset_size: 4028004669.625
- config_name: LACR_T2T_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 89647466
    num_examples: 76643
  download_size: 43136360
  dataset_size: 89647466
- config_name: LADD
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: image
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 1293641342.0
    num_examples: 23240
  download_size: 1285923315
  dataset_size: 1293641342.0
- config_name: LADD_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 16659871
    num_examples: 23240
  download_size: 7472431
  dataset_size: 16659871
- config_name: LA_Images
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 4191197157.25
    num_examples: 81398
  download_size: 4190198358
  dataset_size: 4191197157.25
- config_name: SD
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: image
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 3098784669.75
    num_examples: 15989
  download_size: 1669131271
  dataset_size: 3098784669.75
- config_name: SD_Images
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 2523484759.75
    num_examples: 26154
  download_size: 2438558263
  dataset_size: 2523484759.75
- config_name: SD_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 4112174
    num_examples: 15989
  download_size: 1237759
  dataset_size: 4112174
- config_name: SN
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: image
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 7979712053.04
    num_examples: 6640
  download_size: 3401191449
  dataset_size: 7979712053.04
- config_name: SN_Images
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 859886037.875
    num_examples: 11513
  download_size: 859698909
  dataset_size: 859886037.875
- config_name: SN_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 7230721
    num_examples: 6640
  download_size: 1324832
  dataset_size: 7230721
- config_name: TVC
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: image
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 130408953299.393
    num_examples: 137607
  download_size: 79524699480
  dataset_size: 130408953299.393
- config_name: TVC_Images
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 13056626872.375
    num_examples: 227701
  download_size: 13052443854
  dataset_size: 13056626872.375
- config_name: TVC_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 161582906
    num_examples: 137607
  download_size: 30882217
  dataset_size: 161582906
- config_name: VST
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: image
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 7093814625.328
    num_examples: 32893
  download_size: 4263530868
  dataset_size: 7093814625.328
- config_name: VST_Images
  features:
  - name: id
    dtype: string
  - name: image
    dtype: image
  splits:
  - name: train
    num_bytes: 14529719834.625
    num_examples: 144755
  download_size: 14282540973
  dataset_size: 14529719834.625
- config_name: VST_Instructions
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: answer
    dtype: string
  - name: images
    sequence: string
  - name: related instructions
    sequence: string
  splits:
  - name: train
    num_bytes: 30877616
    num_examples: 32893
  download_size: 9311504
  dataset_size: 30877616
configs:
- config_name: CGD
  data_files:
  - split: train
    path: CGD/train-*
- config_name: CGD_Images
  data_files:
  - split: train
    path: CGD_Images/train-*
- config_name: CGD_Instructions
  data_files:
  - split: train
    path: CGD_Instructions/train-*
- config_name: DC_Instructions
  data_files:
  - split: train
    path: DC_Instructions/train-*
- config_name: E4D_Instructions
  data_files:
  - split: train
    path: E4D_Instructions/train-*
- config_name: LACONV
  data_files:
  - split: train
    path: LACONV/train-*
- config_name: LACONV_Instructions
  data_files:
  - split: train
    path: LACONV_Instructions/train-*
- config_name: LACR_I2I
  data_files:
  - split: train
    path: LACR_I2I/train-*
- config_name: LACR_I2I_Instructions
  data_files:
  - split: train
    path: LACR_I2I_Instructions/train-*
- config_name: LACR_T2T
  data_files:
  - split: train
    path: LACR_T2T/train-*
- config_name: LACR_T2T_Instructions
  data_files:
  - split: train
    path: LACR_T2T_Instructions/train-*
- config_name: LADD
  data_files:
  - split: train
    path: LADD/train-*
- config_name: LADD_Instructions
  data_files:
  - split: train
    path: LADD_Instructions/train-*
- config_name: LA_Images
  data_files:
  - split: train
    path: LA_Images/train-*
- config_name: SD
  data_files:
  - split: train
    path: SD/train-*
- config_name: SD_Images
  data_files:
  - split: train
    path: SD_Images/train-*
- config_name: SD_Instructions
  data_files:
  - split: train
    path: SD_Instructions/train-*
- config_name: SN
  data_files:
  - split: train
    path: SN/train-*
- config_name: SN_Images
  data_files:
  - split: train
    path: SN_Images/train-*
- config_name: SN_Instructions
  data_files:
  - split: train
    path: SN_Instructions/train-*
- config_name: TVC
  data_files:
  - split: train
    path: TVC/train-*
- config_name: TVC_Images
  data_files:
  - split: train
    path: TVC_Images/train-*
- config_name: TVC_Instructions
  data_files:
  - split: train
    path: TVC_Instructions/train-*
- config_name: VST
  data_files:
  - split: train
    path: VST/train-*
- config_name: VST_Images
  data_files:
  - split: train
    path: VST_Images/train-*
- config_name: VST_Instructions
  data_files:
  - split: train
    path: VST_Instructions/train-*
---

<p align="center" width="100%">
<img src="https://i.postimg.cc/sxy8v9PS/mimicit-logo.png"  width="80%" height="80%">
</p>


<div>
<div align="center">
    <a href='https://brianboli.com/' target='_blank'>Bo Li<sup>*,♠,1</sup></a>&emsp;
    <a href='https://zhangyuanhan-ai.github.io/' target='_blank'>Yuanhan Zhang<sup>*,♠,1</sup></a>&emsp;
    <a href='https://cliangyu.com/' target='_blank'>Liangyu Chen<sup>*,1</sup></a>&emsp;
    <a href='https://king159.github.io/' target='_blank'>Jinghao Wang<sup>*,1</sup></a>&emsp;
    <a href='https://pufanyi.github.io/' target='_blank'>Fanyi Pu<sup>*,1</sup></a>&emsp;
    </br>
    <a href='https://jingkang50.github.io/' target='_blank'>Jingkang Yang<sup>1</sup></a>&emsp;
    <a href='https://chunyuan.li/' target='_blank'>Chunyuan Li<sup>2</sup></a>&emsp;
    <a href='https://liuziwei7.github.io/' target='_blank'>Ziwei Liu<sup>&#x2709,1</sup></a>
</div>
<div>
<div align="center">
    <sup>1</sup>S-Lab, Nanyang Technological University&emsp;
    <sup>2</sup>Microsoft Research, Redmond
    </br>
    <sup>♠</sup> Co-Project Lead&emsp;
    <sup>*</sup> Equal Contribution&emsp;
    <sup>&#x2709</sup> Corresponding Author
    
</div>

## Dataset Description

- **Homepage: https://otter-ntu.github.io**
- **Repository: https://github.com/Luodian/Otter**
- **Paper: https://arxiv.org/abs/2306.05425**

**Note 1: To reduce memory consumption during image loading and improve loading speed, we are converting the JSON format of images to the Parquet format. For detailed information, please refer to [this link](https://github.com/Luodian/Otter/blob/main/docs/mimicit_format.md).**

**Note 2: We are uploading the full version of `DC` and `E4D`, the new files are indicated by the suffix `1207`.**


### Dataset Summary

MIMIC-IT offers a diverse and extensive dataset of 2.8M multimodal instruction-response pairs, designed to enhance the performance of Vision-Language Models (VLMs) in real-life scenarios, enabling VLMs to excel in perception, reasoning, and planning while also catering to a multilingual audience. 

MIMIC-IT enables the application of egocentric visual assistant model that can serve that can answer your questions like **Hey, Do you think I left my keys on the table?**. Harness the power of MIMIC-IT to unlock the full potential of your AI-driven visual assistant and elevate your interactive vision-language tasks to new heights.

MIMIC-IT provides multilingual instructions, supporting English, Chinese, Korean, Japanese, German, French, Spanish, and Arabic, thereby allowing a larger global audience to altogether enjoy from the convenience brought about by advancements in artificial intelligence.

<p align="center" width="100%">
<img src="https://i.postimg.cc/4x66gHhw/mimic-it.jpg"  width="100%" height="100%">
</p>

## Using MIMIC-IT

We have already upload the `images.parquet` file. You can check [`tools/load.py`](tools/load.py) to learn how to load the dataset (`instruction.json` + `images.parquet`) and check the integrity of the whole dataset.

You can also use [this code](https://huggingface.co/datasets/pufanyi/MIMICIT/blob/main/tools/convert_to_parquet.py) to convert `image.json` to `parquet` version by yourself.

You can following the steps to obtain the MIMIC-IT dataset. Each task (e.g. `DC`, `LA`) in MIMIC-IT is composed of three parts, including:
1. `xx.json` file: the images in base64 format.
2. `xx_instructions.json` file: the instruction-response pairs (also includes image ids and related instructions ids for each instruction-response pair) for each task.
3. `xx_train.json` file: the customized related instruction-response pairs for each instruction.

You can directly download the contents in the `data` folder. The distribution of the `data` folder is as follows:

```plain
data/
	CGD/
		CGD.json
		CGD_images_preview.csv
		CGD_instructions.json
	...
```

For each `dataset_name`, there are three main files **except for `DC` and `E4D`**:

1. `{dataset_name}.json`: Stores the image numbers and their corresponding base64 codes in lossless compressed PNG format.
   ```json
   {
     "image_id_1": "base64_code_1",
     "image_id_2": "base64_code_2",
     ...
   }
   ```
2. `{dataset_name}_images_preview.csv`: Stores the image numbers and their corresponding base64 codes in lossy compressed JPG format, mainly used for display in the Dataset Card.
   ```csv
   id, image
   "image_id_1", "base64_code_1"
   "image_id_2", "base64_code_2"
   ...
   ```
3. `{dataset_name}_instructions.json`: Stores each instruction and its associated answer.
   ```json
   {
     "meta": {
       "version": current_version,
       "time": update_time,
       "author": "ntu"
     },
     "data": {
       "instruction_id_1": {
         "instruction": "instruction_1",
         "answer": "answer_of_instruction_1",
         "image_ids": [
           "image_id_1",
           "image_id_2",
           ...
         ],
         "rel_ins_ids": [
           "related_instruction_id_1",
           "related_instruction_id_2",
           ...
         ]
       },
       ...
     }
   }
   ```

Of course, you can also use `wget` or `curl` for direct downloads. Below is an example.

Before proceeding with the downloads, you need to set your Hugging Face token. For that, please refer to [this page](https://huggingface.co/docs/hub/security-tokens).


```shell
$ # Set Hugging Face Token
$ HF_TOKEN="YOUR_HUGGING_FACE_TOKEN"

$ # Set the dataset you want to download
$ DATASET_NAME="DATASET_YOU_WANT_TO_DOWNLOAD" # e.g. CGD

$ # Download {DATASET_NAME}.json
$ wget --header="Authorization: Bearer $HF_TOKEN" "https://huggingface.co/datasets/pufanyi/MIMICIT/resolve/main/data/${DATASET_NAME}/${DATASET_NAME}.json"

$ # Download {DATASET_NAME}_instructions.json
$ wget --header="Authorization: Bearer $HF_TOKEN" "https://huggingface.co/datasets/pufanyi/MIMICIT/resolve/main/data/${DATASET_NAME}/${DATASET_NAME}_instructions.json"

$ # Download {DATASET_NAME}_images_preview.csv (usually not necessary)
$ wget --header="Authorization: Bearer $HF_TOKEN" "https://huggingface.co/datasets/pufanyi/MIMICIT/resolve/main/data/${DATASET_NAME}/${DATASET_NAME}_images_preview.csv"
```

Or

```shell
$ # Set Hugging Face Token
$ HF_TOKEN="YOUR_HUGGING_FACE_TOKEN"

$ # Set the dataset you want to download
$ DATASET_NAME="DATASET_YOU_WANT_TO_DOWNLOAD" # e.g. CGD

$ # Download {DATASET_NAME}.json
$ curl -LJO -H "Authorization: Bearer $HF_TOKEN" "https://huggingface.co/datasets/pufanyi/MIMICIT/resolve/main/data/${DATASET_NAME}/${DATASET_NAME}.json"

$ # Download {DATASET_NAME}_instructions.json
$ curl -LJO -H "Authorization: Bearer $HF_TOKEN" "https://huggingface.co/datasets/pufanyi/MIMICIT/resolve/main/data/${DATASET_NAME}/${DATASET_NAME}_instructions.json"

$ # Download {DATASET_NAME}_images_preview.csv (usually not necessary)
$ curl -LJO -H "Authorization: Bearer $HF_TOKEN" "https://huggingface.co/datasets/pufanyi/MIMICIT/resolve/main/data/${DATASET_NAME}/${DATASET_NAME}_images_preview.csv"
```

Alternatively, you can use `dataset.load_dataset` for downloading. However, due to Hugging Face's size limitations, all images can only be loaded in JPG format. Below is an example using `CGD` dataset:


### CGD_Images

Download the JPG format images and their corresponding identifiers:

```python
from datasets import load_dataset
data = load_dataset("pufanyi/MIMICIT", "CGD_Images")
```

The format will be like:

```json
{
	"id": "CGD_IMG_000000426149",
	"image": <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=224x224 at 0x7F84601D62F0>
}
```

It should be noted that, due to size limitations, for `DC` (Dense Captions), this command will only extract a portion of the images from the `DC` collection for downloading.

### CGD_Instructions

Download all instructions:

```python
from datasets import load_dataset
data = load_dataset("pufanyi/MIMICIT", "CGD_Instructions")
```

The format will be like:

```json
{
    "id": "CGD_INS_000000",
    "instruction": "What is the difference between the two pizzas in these images?",
    "answer": "The pizza in the first image is on a red plate and being held by an old lady, while the pizza in the second image is on a metal counter being prepared by a woman in a blue shirt.",
    "images": [
        "CGD_IMG_000000069568",
        "CGD_IMG_000000328270"
    ],
    "related instructions": [
        "CGD_INS_000001"
    ]
}
```

### CGD_Preview

Download all instructions along with their corresponding JPG images:

```python
from datasets import load_dataset
data = load_dataset("pufanyi/MIMICIT", "CGD_Preview")
```

The format will be like:

```json
{
    "id": "CGD_INS_000000",
    "instruction": "What is the difference between the two pizzas in these images?",
    "answer": "The pizza in the first image is on a red plate and being held by an old lady, while the pizza in the second image is on a metal counter being prepared by a woman in a blue shirt.",
    "images": [
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=224x224 at 0x7F8460267DF0>,
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=224x224 at 0x7F8460267700>
    ],
    "related instructions": [
        "CGD_INS_000001"
    ]
}
```

It should be noted that, due to size limitations, for `DC` (Dense Captions), this command will only extract a portion of the images from the `DC` collection for downloading.