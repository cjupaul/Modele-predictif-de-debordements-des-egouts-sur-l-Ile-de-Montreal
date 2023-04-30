import os
import subprocess
import shutil
from parameters import parameters as p

def main():


    if p['runData']:
        print("dossier data est en cours...")

        os.chdir('data')
        subprocess.run(["python", "main_data.py"])
        os.chdir('..')

        print("dossier data est terminé...")
        print(" ")
        

    if p['runLstm']:
        print("dossier lstm est en cours...")

        file_to_add_lstm = ["data_test.csv","data_train.csv","data_valid.csv"]

        for file in file_to_add_lstm:
            if not os.path.exists("./lstm/data_inputs/" + file) or p['runData'] == True:
                shutil.copy("./data/data_preprocessing_outputs/" + file, "./lstm/data_inputs/")

        os.chdir('lstm')
        subprocess.run(["python", "main_lstm.py"])
        os.chdir('..')

        print("dossier lstm est terminé...")
        print(" ")


    if p['runMap']:
        print("dossier map est en cours...")

        file_to_add_map = ["data_test_2020.csv","data_test.csv","df.csv"]

        for file in file_to_add_map:
            if not os.path.exists("./map/data_inputs/" + file) or p['runData'] == True:
                shutil.copy("./data/data_preprocessing_outputs/" + file, "./map/data_inputs/")

        if not os.path.exists("./lstm/model_inputs/LSTM.ckpt"):
            shutil.copy("./lstm/model_outputs/LSTM.ckpt", "./map/model_inputs/")

        os.chdir('map')
        subprocess.run(["python", "main_map.py"])
        os.chdir('..')

        print("dossier map est terminé...")
        print(" ")


    if p['runSweep']:
        print("dossier sweep est en cours...")

        file_to_add_sweep = ["data_train.csv","data_valid.csv"]

        for file in file_to_add_sweep:
            if not os.path.exists("./sweep/sweep_data_inputs/" + file) or p['runData'] == True:
                shutil.copy("./data/data_preprocessing_outputs/" + file, "./sweep/sweep_data_inputs/")

        os.chdir('sweep')
        subprocess.run(["python", "main_sweep.py"])
        os.chdir('..')

        print("dossier sweep est terminé...")
        print(" ")


if __name__ == '__main__':
    main()
