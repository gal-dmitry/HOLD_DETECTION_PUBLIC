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
- Link to the associated metadata folder
- Name of the associated section in the [IPython notebook](EXPERIMENTS_01.ipynb)
- Values of the main metrics

Each metadata folder contains the following information:
- Configuration files:
    - `config.yml` | contains all the hyperparameters used in a given experiment
- Figures:
    - `loss.png` | contains loss on train and validation sets logged across the training process
    - `metrics.png` | contains metrics on validation sets logged across the training process
- Tables:
    - `val_tr_search_f1.csv` | Metrics:
        - per each model and associated validation fold (columns)
        - per all unique predicted probability values (rows)
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

| Metadata folder | Notebook section name | Class weight | ROC AUC | Best threshold | Recall | Precision | Balanced Accuracy | F1
|:----------------|:----------------------|-------------:|--------:|---------------:|-------:|----------:|------------------:|---:|
| [2024_02_23__17_22_36](./mlruns/multiclass/2024_02_23__17_22_36) | `multiclass_02 / 2024_02_23__17_22_36` | `[0.005, 1.0, 1.0]` | 0.9946 | 0.5449 | 0.9135 | 0.8529 | 0.9135 | 0.8778 |
| [2024_02_24__08_57_59](./mlruns/multiclass/2024_02_24__08_57_59) | `multiclass_03 / 2024_02_24__08_57_59` | `[0.01, 1.0, 1.0]` | 0.9942 | 0.9791 | 0.8824 | 0.8899 | 0.8824 | 0.8836 |
| [2024_02_23__15_16_58](./mlruns/multiclass/2024_02_23__15_16_58) | `multiclass_01 / 2024_02_23__15_16_58` | `[0.02, 1.0, 1.0]` | 0.9935 | 0.5092 | 0.9095 | 0.8666 | 0.9095 | 0.8834 | 
| [2024_02_24__08_59_55](./mlruns/multiclass/2024_02_24__08_59_55) | `multiclass_04 / 2024_02_24__08_59_55` | `[0.05, 1.0, 1.0]` | 0.9939 | 0.9662 | 0.8802 | 0.9002 | 0.8802 | 0.8876 |
| [2024_02_25__08_20_52](./mlruns/multiclass/2024_02_25__08_20_52) | `multiclass_05 / 2024_02_25__08_20_52` | `[0.075, 1.0, 1.0]` | 0.9931 | 0.9627 | 0.8805 | 0.9063 | 0.8805 | 0.8908 |
| [2024_02_25__08_21_41](./mlruns/multiclass/2024_02_25__08_21_41) | `multiclass_06 / 2024_02_25__08_21_41` | `[0.1, 1.0, 1.0]` | 0.9931 | 0.9128 | 0.8883 | 0.8927 | 0.8883 | 0.889 | 
| [2024_02_27__13_28_54](./mlruns/multiclass/2024_02_27__13_28_54) | `multiclass_00 / 2024_02_27__13_28_54` | `[1.0, 1.0, 1.0]` | 0.9943 | 0.3347 | 0.9052 | 0.8706 | 0.9052 | 0.8843 |



#### Experiment 2. Learning rate adjustment.

| Metadata folder | Notebook section name | Learning rate | ROC AUC | Best threshold | Recall | Precision | Balanced Accuracy | F1 |
|:----------------|:----------------------|--------------:|--------:|---------------:|-------:|----------:|------------------:|---:|
| [2024_02_26__10_17_25](./mlruns/multiclass/2024_02_26__10_17_25) | `multiclass_08 / 2024_02_26__10_17_25` | 5.e-7 | 0.9858 | 0.5541 | 0.8126 | 0.8504 | 0.8126 | 0.8185 |
| [2024_02_26__10_16_38](./mlruns/multiclass/2024_02_26__10_16_38) | `multiclass_07 / 2024_02_26__10_16_38` | 1.e-6 | 0.9925 | 0.8656 | 0.8877 | 0.8985 | 0.8877 | 0.8921 |
| [2024_02_27__08_31_09](./mlruns/multiclass/2024_02_27__08_31_09) | `multiclass_09 / 2024_02_27__08_31_09` | 3.e-6 | 0.9947 | 0.8422 | 0.9113 | 0.8949 | 0.9113 | 0.9014 |
| [2024_02_25__08_20_52](./mlruns/multiclass/2024_02_25__08_20_52) | `multiclass_05 / 2024_02_25__08_20_52` | 5.e-6 | 0.9931 | 0.9627 | 0.8805 | 0.9063 | 0.8805 | 0.8908 |







