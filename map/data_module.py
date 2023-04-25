import pytorch_lightning as pl
from dataset import StationDataset
from parameters import parameters as p
import pandas as pd
from torch.utils.data import DataLoader

class StationDataModule(pl.LightningDataModule):

    def __init__(self, input_data_train:pd.DataFrame,input_data_valid:pd.DataFrame):
        super().__init__()
        self.train_sequences = create_sequences(input_data_train, p["Surverse"], p["sequence_lenght"])
        self.valid_sequences = create_sequences(input_data_valid, p["Surverse"], p["sequence_lenght"])
        self.batch_size = p["batch_size"]

    def setup(self,stage=None):
        self.train_dataset = StationDataset(self.train_sequences)
        self.valid_dataset = StationDataset(self.valid_sequences)
    
    def train_dataloader(self): 
        return DataLoader( 
            self.train_dataset,
            batch_size=self.batch_size,
            shuffle=True 
        )
    def val_dataloader(self): 
        return DataLoader( 
            self.valid_dataset,
            batch_size=self.batch_size,
            shuffle=False
        )

def create_sequences(input_data:pd.DataFrame,target_column,sequence_length):
    sequences= []
    data_size=len(input_data)

    for i in range(data_size - sequence_length): 

        sequence= input_data[i:i+sequence_length] 

        label_position= i + sequence_length 
        label=input_data.iloc[label_position][target_column] 

        sequences.append((sequence,label)) 
    return sequences

