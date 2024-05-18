# HOLD_DETECTOR_PUBLIC



### Description

This is a public repository containing code for paper ["Text-based detection of on-hold scripts in contact center calls"](./). The paper presents a framework for detecting on-hold phrases in client-manager dialogues transcribed using ASR. 



### Structure

- [Configuration files](./configs/train/multiclass)

- [Experiment artefacts](./mlruns/multiclass)

- [Experiment reports](EXPERIMENTS_01.ipynb)



### Code

This code can be applied for training a transformers' model on an arbitrary dataset for binary/multiclass text classification. You may want to change any hyperparameters in the configuration file. To launch the training process, you should run the following command:

```bash
python train.py --config_path <config_path>.yml
```

Example:

```bash
python train.py --config_path configs/train/multiclass/multiclass_09.yml
```



### Experiments

This section reports information about provided experiments. Each table row contains:
- Values of the main metrics
- Link to the associated metadata folder
- Name of the associated section in the [IPython notebook](EXPERIMENTS_01.ipynb)

Each metadata folder contains the following information:
- Configuration files:
    - `config.yml` | contains all the hyperparameters used in a given experiment
- Figures:
    - `loss.png` | contains loss on train and validation sets logged across the training process
    - `metrics.png` | contains metrics on validation sets logged across the training process
- Tables:
    - `val_tr_search_f1.csv` | Metrics:
        - Per each model and associated validation fold (columns)
        - Per all unique predicted probability values (rows)
    - `val_metrics_f1.csv` | Metrics:
        - per each model and associated validation fold (columns)
        - per different averaging types (rows):
            - None: per each of 3 classes
            - Macro
            - Weighted
    - `test_metrics_f1.csv` | Metrics:
        - per each model (columns)
        - per different averaging types (rows):
            - None: per each of 3 classes
            - Macro
            - Weighted


#### Experiment 1. Class weight adjustment.
///


#### Experiment 2. Learning rate adjustment.

| Metadata folder | Notebook section name | Learning rate | ROC AUC | Best threshold | Recall | Precision | Balanced Accuracy | F1 |
|:----------------|:----------------------|--------------:|--------:|---------------:|-------:|----------:|------------------:|---:|
| [2024_02_26__10_17_25](./mlruns/multiclass/2024_02_26__10_17_25) | `multiclass_08 / 2024_02_26__10_17_25` | 5.e-7 | 0.9858 | 0.5541 | 0.8126 | 0.8504 | 0.8126 | 0.8185 |
| [2024_02_26__10_16_38](./mlruns/multiclass/2024_02_26__10_16_38) | `multiclass_07 / 2024_02_26__10_16_38` | 1.e-6 | 0.9925 | 0.8656 | 0.8877 | 0.8985 | 0.8877 | 0.8921 |
| [2024_02_27__08_31_09](./mlruns/multiclass/2024_02_27__08_31_09) | `multiclass_09 / 2024_02_27__08_31_09` | 3.e-6 | 0.9947 | 0.8422 | 0.9113 | 0.8949 | 0.9113 | 0.9014 |
| [2024_02_25__08_20_52](./mlruns/multiclass/2024_02_25__08_20_52) | `multiclass_05 / 2024_02_25__08_20_52` | 5.e-6 | 0.9931 | 0.9627 | 0.8805 | 0.9063 | 0.8805 | 0.8908 |







