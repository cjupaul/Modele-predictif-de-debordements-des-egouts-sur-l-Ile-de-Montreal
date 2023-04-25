from results import Results_inferences
from metrics import Metrics
from parameters import parameters as p
import torch
from tqdm.auto import tqdm
from dataset import StationDataset
from data_module import create_sequences

class InferenceModule():

    def __init__(self, model, data):
        super().__init__()
        self.model = model
        self.data_test = StationDataset(create_sequences(data, p["Surverse"],p["Site No"], p["sequence_lenght"]))

        self.model.eval()

        self.results_inf = Results_inferences()
        self.results_metrics = Metrics()
        
    def start_module_prediction(self):

        with torch.no_grad():
            for item in tqdm(self.data_test):
                sequence = item["sequence"]
                label_name = item["label_name"]
                _, output =self.model(torch.unsqueeze(sequence,dim=0))
                prediction = torch.argmax(output, dim=1)
                self.results_inf.results(int(label_name.item()), prediction.item())

    def start_module_metrics(self):

        with torch.no_grad():
            for item in tqdm(self.data_test):
                sequence = item["sequence"]
                label = item["label"]
                _, output =self.model(torch.unsqueeze(sequence,dim=0))
                prediction = torch.argmax(output, dim=1)
                self.results_metrics.results(label.item(), prediction.item())
