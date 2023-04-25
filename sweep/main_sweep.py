import pytorch_lightning as pl
import optuna
from sweep import objective
from parameters import parameters as p

def main():
    
    pl.seed_everything(p["seed"])

    study = optuna.create_study(direction="maximize")

    study.optimize(objective, n_trials=1)

    print("Number of finished trials: {}".format(len(study.trials)))

    print("Best trial:")
    trial = study.best_trial

    print("  Value: {}".format(trial.value))

    print("  Params: ")
    for key, value in trial.params.items():
        print("    {}: {}".format(key, value))

if __name__ == '__main__':
    main()