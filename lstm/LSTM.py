from parameters import parameters as p
import torch
import torch.nn as nn
from torchmetrics import F1Score
import pytorch_lightning as pl
import torch.optim as optim

class LSTM(nn.Module):

    def __init__(self):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size = p["n_features"],
            hidden_size = p["n_hidden"],
            num_layers = p["n_layers"],
            batch_first = True,
            dropout = p["dropout"]
        )
        self.classifier = nn.Linear(p["n_hidden"], p["n_classes"])

    def forward(self, x):
        self.lstm.flatten_parameters()
        _, (hidden, _) = self.lstm(x)

        out = hidden[-1]
        return self.classifier(out)

class StationPredictor(pl.LightningModule):

    def __init__(self):
        super().__init__()
        self.model = LSTM()
        self.criterion = nn.CrossEntropyLoss()
            
    def forward(self, x ,labels= None):
        output = self.model(x)
        loss = 0
        if labels is not None:
            loss=self.criterion(output,labels)
        return loss, output
  
    def training_step(self, batch,batch_idx):
        sequences = batch['sequence']
        labels = batch['label']

        self.forward(sequences)

        self.criterion = nn.CrossEntropyLoss()

        loss, outputs = self(sequences, labels)
        predictions = torch.argmax(outputs, dim=1) 
        f1 = F1Score(task="binary",snum_classes=2)
        step_f1 = f1(predictions, labels)

        self.log('train_loss', loss, prog_bar=True, logger=True) 
        self.log('train_f1', step_f1, prog_bar=True, logger=True)
        return {'loss': loss, 'f1': step_f1} 

    def validation_step(self, batch,batch_idx):
        sequences = batch['sequence']
        labels = batch['label']

        self.forward(sequences)

        self.criterion = nn.CrossEntropyLoss()

        loss, outputs = self(sequences, labels)
        predictions = torch.argmax(outputs, dim=1) 
        f1 = F1Score(task="binary",snum_classes=2)
        step_f1 = f1(predictions, labels)

        self.log('valid_loss', loss, prog_bar=True, logger=True) 
        self.log('valid_f1', step_f1, prog_bar=True, logger=True)
        return {'loss': loss, 'f1': step_f1}

    def configure_optimizers(self):
        return optim.Adam(self.parameters())
