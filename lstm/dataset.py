from torch.utils.data import Dataset
import torch
import numpy as np

class StationDataset(Dataset):

  def __init__(self, sequences): 
    self.sequences = sequences
  
  def __len__(self): 
    return len(self.sequences)

  def __getitem__(self, idx): 
    sequence, label, label_station_name = self.sequences[idx] 

    return dict( 
        sequence = torch.Tensor(sequence.to_numpy(np.uint8)),
        label = torch.tensor(label).long(),
        label_name = label_station_name
        )
  