import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.metrics import confusion_matrix
from utils.utils import show_confusion_matrix, classification_results

class Metrics():

    def __init__(self): 
        self.writeResults = ""
        self.predictions=[]
        self.labels=[]

    def results(self, gt, pred):
        self.labels.append(gt)
        self.predictions.append(pred)

    def write_finals_metrics(self):
            cm = pd.DataFrame(confusion_matrix(self.labels,self.predictions))
            show_confusion_matrix(cm,"./metrics_outputs/")
            classification_results(self.labels,self.predictions,"./metrics_outputs/")

