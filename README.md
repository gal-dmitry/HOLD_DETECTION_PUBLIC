# HOLD_DETECTOR_PUBLIC


This is a public repository containing the code for the paper "Text-based detection of on-hold scripts in contact center calls". The paper presents a framework for detecting on-hold phrases in client-manager dialogues transcribed using ASR. 

- [Experiments](EXPERIMENTS_01.ipynb)

- [Configuration files](./configs/train/multiclass)

- [Artefacts](./mlruns/multiclass)

- How to launch a training process:

    ```bash
    python train.py --config_path configs/train/multiclass/multiclass_09.yml
    ```