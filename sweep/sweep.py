import pytorch_lightning as pl
from pytorch_lightning.callbacks import EarlyStopping
import pandas as pd
import optuna
from data_module import StationDataModule
from LSTM import StationPredictor

def objective(trial: optuna.trial.Trial)-> float:

    # We optimize the number of layers, hidden units in each layer and dropouts.
    n_layers = trial.suggest_int("n_layers", 1, 3)
    dropout = trial.suggest_float("dropout", 0.5, 0.85)
    BATCH_SIZE = trial.suggest_int("BATCH_SIZE", 4,64)
    n_hidden = trial.suggest_int("n_hidden", 4, 256, log=True)
    SEQUENCE_LENGHT = trial.suggest_int("SEQUENCE_LENGH", 1, 100, log=True)

    early_stop_callback = EarlyStopping(monitor="valid_f1",min_delta=0.00, patience=3, verbose=False, mode="max")

    data_train = pd.read_csv('./sweep_data_inputs/data_train.csv')

    data_valid = pd.read_csv('./sweep_data_inputs/data_valid.csv')

    data_module = StationDataModule(data_train,data_valid)

    model = StationPredictor()

    trainer = pl.Trainer(
        logger=True,
        max_epochs=1000,
        callbacks=[early_stop_callback],
    )

    
    hyperparameters = dict(n_layers=n_layers, dropout=dropout, n_hidden=n_hidden,BATCH_SIZE=BATCH_SIZE,SEQUENCE_LENGHT=SEQUENCE_LENGHT)
    trainer.logger.log_hyperparams(hyperparameters)
    trainer.fit(model,data_module)

    return trainer.callback_metrics["valid_f1"].item()
