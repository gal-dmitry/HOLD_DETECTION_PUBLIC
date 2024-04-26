import sys
import os.path as op
sys.path.append(
    op.abspath(op.join(__file__, op.pardir, op.pardir))
)

from utils._utils import *


def get_steps(trainer):
    
    steps = trainer.state.log_history[:-1]
    train_steps = steps[0::2]
    val_steps = steps[1::2]
    
    dct = {"train_steps": train_steps, "val_steps": val_steps}
    
    dct["train_epochs"] = [step["epoch"] for step in train_steps]
    dct["train_steps_"] = [int(step["step"]) for step in train_steps] 
    dct["train_loss"] = [step["loss"] for step in train_steps]           
    dct["train_lr"] = [step["learning_rate"] for step in train_steps] 
    
    dct["val_epochs"] = [step["epoch"] for step in val_steps]
    dct["val_steps_"] = [int(step["step"]) for step in val_steps] 
    dct["val_loss"] = [step["eval_loss"] for step in val_steps]
    
    return dct


# def plot_training(trainer, metric_names=[], suffix="", save_dir="."):
    
#     if suffix:
#         suffix = f"_{suffix}"
        
    
#     plt.plot(train_steps_, train_loss, label="train_loss")
#     plt.plot(val_steps_, val_loss, label="val_loss")
#     plt.plot(train_steps_, train_lr, label="lr")
#     plt.xlabel("epochs")
#     plt.legend()
#     plt.title(f"Training process{suffix}")
#     plt.savefig(f"{save_dir}/loss{suffix}.png")
#     plt.close()
    
#     for metric_name in metric_names:
#         metric_name = 'eval_' + metric_name
#         metric = [step[metric_name] for step in val_steps]
        
#         plt.plot(val_steps_, metric, label=metric_name)
#         plt.xlabel("steps")
        
#     plt.legend()
#     plt.title(f"Training process{suffix}")
#     plt.savefig(f"{save_dir}/metrics{suffix}.png")
#     plt.close()
    
    
def plot_kfold_training(kfold_dct, metric_names=[], suffix="", save_dir="."):
    
    # loss
    for fold, dct in kfold_dct.items():
        plt.plot(dct["train_steps_"], dct["train_loss"], label=f"train_loss_{fold}")
        plt.plot(dct["val_steps_"], dct["val_loss"], label=f"val_loss_{fold}")
#         plt.plot(dct["train_steps_"], dct["train_lr"], label=f"lr_{fold}")
        
    plt.xlabel("epochs")
    plt.legend()
    plt.title(f"Training process{suffix}")
    plt.savefig(f"{save_dir}/loss{suffix}.png")
    plt.close()
    
    
    # metrics
    for fold, dct in kfold_dct.items():
        
        for metric_name in metric_names:
            metric_name = 'eval_' + metric_name
            metric = [step[metric_name] for step in dct["val_steps"]]
            plt.plot(dct["val_steps_"], metric, label=f"{metric_name}_{fold}")
        
    plt.xlabel("steps")
    plt.legend()
    plt.title(f"Training process{suffix}")
    plt.savefig(f"{save_dir}/metrics{suffix}.png")
    plt.close()

        