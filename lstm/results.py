
class Results_inferences():

    def __init__(self): 
        self.writeResults = ""

    def results(self, stationname, prediction):
        self.writeResults += "{}, {}\n".format(stationname,prediction)

    def write_finals_results(self):
        with open("./inference_outputs/results" + ".txt", "w+") as f:
            f.write(self.writeResults)
            


