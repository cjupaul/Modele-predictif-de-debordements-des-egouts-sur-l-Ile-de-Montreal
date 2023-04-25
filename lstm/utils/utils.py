import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.metrics import classification_report

def show_confusion_matrix(confusion_matrix, path):
    hmap=sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="Blues")
    hmap.yaxis.set_ticklabels(hmap.yaxis.get_ticklabels(), rotation=0, ha="right")
    hmap.xaxis.set_ticklabels(hmap.xaxis.get_ticklabels(), rotation=30, ha="right")
    plt.ylabel("True déversement")
    plt.xlabel("Predicted déversement")
    plt.savefig(path + "Confusion_matrix.pdf")  

def classification_results(targcol,predcol,path):
    labels = list(set(targcol))
    report_dict = classification_report(targcol, predcol, output_dict=True)
    repdf = pd.DataFrame(report_dict).round(2).transpose()
    repdf.insert(loc=0, column='class', value=labels + ["accuracy", "macro avg", "weighted avg"])
    repdf.to_csv(path + "classification_report.csv", index=False)