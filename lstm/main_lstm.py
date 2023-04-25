from inference import InferenceModule
from parameters import parameters as p
from data_module import StationDataModule
from LSTM import StationPredictor
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint,EarlyStopping
from pytorch_lightning.loggers import TensorBoardLogger
import pandas as pd
import shutil
import os

def main():

    pl.seed_everything(p["seed"])

    if p["runTrain"]:

        if os.path.exists("./model_outputs/" + p["model_name"] + ".ckpt"):
            os.remove("./model_outputs/" + p["model_name"] + ".ckpt")

        data_train = pd.read_csv('./data_inputs/data_train.csv')

        data_valid = pd.read_csv('./data_inputs/data_valid.csv')

        data_module = StationDataModule(data_train,data_valid)

        model = StationPredictor()

        checkpoint_callback = ModelCheckpoint(
        dirpath="./model_outputs/",
        filename=p["model_name"], 
        save_top_k=1,
        verbose=True, 
        monitor="train_f1", 
        mode="max" 
        )

        early_stop_callback = EarlyStopping(monitor="train_f1",min_delta=0.00, patience=3, verbose=False, mode="max")

        trainer = pl.Trainer(logger=True,callbacks=[early_stop_callback, checkpoint_callback],max_epochs=10000)

        trainer.fit(model,data_module)
        
        shutil.copy("./parameters.py", "./model_outputs/")

        del data_train
        del data_valid
        del data_module
        del trainer

    if p["runInference"]:

        data_test = pd.read_csv('./data_inputs/data_test.csv')

        trained_model = StationPredictor.load_from_checkpoint("./model_outputs/" + p["model_name"] + ".ckpt")

        trained_model.freeze()

        inference = InferenceModule(trained_model,data_test)

        inference.start_module_prediction()

        inference.results_inf.write_finals_results()

        inference.start_module_metrics()

        inference.results_metrics.write_finals_metrics()

        del data_test

if __name__ == '__main__':
    main()