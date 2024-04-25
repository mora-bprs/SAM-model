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
        <a target="blank" href="https://colab.research.google.com/github/mora-bprs/SAM-model/blob/thuva/fastSAM.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
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


WIP - Detailed Documentation at [SAM Documentation](https://mora-bprs.github.io/docs/models/sam/)

## Possible Errors and Gotchas
- When you are running on Google Colab modify the COLAB and INITIALIZED variables accordingly then you can execute run all 🥂
- [x] ~There seems to be an error in tkinter import resolving in venv of a python3.11 version, use python3.8 -> 3.10 to resolve this issue.~
- Use python version 3.10 or 3.11 for maximum compatibility
- `pip install -r requirements.txt` will take a long time at first in local testing depending on the python version you choose. Sit back and have a coffee.

## Pending Tasks
- [x] Simplify dependency graph
- [x] Simplify code logic to recreate the results on all platforms
- [ ] Add references and license information of models and repos
- [ ] Move all dataset and weights hosting to github and huggingface
- [ ] Integrate SAM into fastSAM notebook for comparision
- [ ] Implement Python scripts for implementation
- [ ] Integration with webcam
- [ ] Move Nix configuration to separate branch