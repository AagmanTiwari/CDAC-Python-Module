'''Assignment 3: Object State Persistence with Pickle
Scenario
A machine learning experiment tracker records trained model hyperparameters and validation metrics. Researchers need to serialize experiment sessions to disk and reload them seamlessly.

Problem Description
Create a class ExperimentSnapshot with:
Attributes: experiment_id (str), model_type (str), hyperparameters (dict), metrics (dict), timestamp (str).
Method get_best_metric(metric_name): Returns the numeric score for metric_name from metrics.
Create two helper functions:
save_experiment(snapshot, file_path): Serializes the ExperimentSnapshot object to file_path in binary mode using pickle.dump().
load_experiment(file_path): Deserializes and returns the ExperimentSnapshot instance from file_path. If the file does not exist, raises FileNotFoundError.
Example Walkthrough
exp = ExperimentSnapshot(
    experiment_id="EXP-2026-001",
    model_type="RandomForest",
    hyperparameters={"n_estimators": 100, "max_depth": 10},
    metrics={"accuracy": 0.942, "f1_score": 0.938},
    timestamp="2026-09-01 10:00:00"
)

save_experiment(exp, "experiment_01.pkl")

restored_exp = load_experiment("experiment_01.pkl")
print(restored_exp.model_type)                    # Output: RandomForest
print(restored_exp.get_best_metric("accuracy"))   # Output: 0.942

'''

import pickle


def save_snapshot(data, filename):

    with open(filename, "wb") as file:
        pickle.dump(data, file)

    print("Snapshot saved successfully.")


def load_snapshot(filename):

    with open(filename, "rb") as file:
        data = pickle.load(file)

    print("Snapshot loaded successfully.")

    return data


experiment = {
    "experiment_name": "Student Performance Analysis",
    "model": "Linear Regression",
    "accuracy": 92.5,
    "parameters": {
        "learning_rate": 0.01,
        "epochs": 100
    }
}


save_snapshot(experiment, "experiment.pkl")

loaded_experiment = load_snapshot("experiment.pkl")

print(loaded_experiment)
