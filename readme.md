# sam model
This repo contains the code to implement,
1. SAM
2. fastSAM
3. fastSAM-s
models for box detection tasks.

Detailed Documentation at [SAM Documentation](https://mora-bprs.github.io/docs/models/sam/)

## Possible Errors and Gotchas
- There seems to be an error in tkinter import resolving in venv of a python3.11 version, use python3.8 -> 3.10 to resolve this issue.
- `pip install -r requirements.txt` will take a very long time at first in local testing depending on the python version you choose. Sit back and have a coffee.

## Pending Tasks
-[] Simplify dependency graph
-[] Simplify code logic to recreate the results on all platforms
-[] Move all dataset and weights hosting to github and huggingface