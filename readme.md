# sam model
This repo contains the code to implement,
1. SAM
2. fastSAM
3. fastSAM-s
models for box detection tasks.

## Getting Started
Currently fastSAM.ipynb is partially ready for public consumption
1. Google Colab
    - Open the notebook in Colab
        <a target="blank" href="https://colab.research.google.com/github/mora-bprs/sam-model/blob/main/fast-sam.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="open stuff in google colab"/>
        </a>
    - Modify the `COLAB` and `INITIALIZED` variables accordingly
    - Menu -> Runtime -> Run All -> Sitback and Relax
2. Local Environment
    - Make sure you have python version >=3.10
        ```shell
        python3 --version
        ```
    - Create a python virtual environment (prefereably in the working directory)
        ```shell
        python3 -m venv .venv
        ```
    - Activate the python environment according to your shell
    - Install pip dependencies
        ```shell
        pip install -r requirements.txt
        ```
    - Run The Notebook in VSCode with Python and Jupyter Extensions or In the Jupyter Environment
    - Set the `INITIALIZED` variable accordingly


WIP - Detailed Documentation at [SAM Documentation](https://mora-bprs.github.io/docs/models/sam/)

## Possible Errors and Gotchas
- When you are running on Google Colab modify the COLAB and INITIALIZED variables accordingly then you can execute run all 🥂
- [x] ~There seems to be an error in tkinter import resolving in venv of a python3.11 version, use python3.8 -> 3.10 to resolve this issue.~
- Use python version 3.10 or 3.11 for maximum compatibility
- `pip install -r requirements.txt` will take a long time at first in local testing depending on the python version you choose. Sit back and have a coffee.

## Model Checkpoints

source : [https://pypi.org/project/segment-anything-fast/](https://pypi.org/project/segment-anything-fast/)

Two model versions of the model are available with different sizes. Click the links below to download the checkpoint for the corresponding model type.

- `default` or `FastSAM`: [YOLOv8x based Segment Anything Model](https://drive.google.com/file/d/1m1sjY4ihXBU1fZXdQ-Xdj-mDltW-2Rqv/view?usp=sharing) | [Baidu Cloud (pwd: 0000)](https://pan.baidu.com/s/18KzBmOTENjByoWWR17zdiQ?pwd=0000).
- FastSAM-s: [YOLOv8s based Segment Anything Model](https://drive.google.com/file/d/10XmSj6mmpmRb8NhXbtiuO9cTTBwR_9SV/view).
