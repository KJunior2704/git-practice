import pandas as pd
import yaml
import json

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

max_days = config["max_days_since_calibration"]
output_file = config["output_file"]

sensors = pd.read_excel("sensors.xlsx")
calibrations = pd.read_csv("calibrations.csv")

combined = pd.merge(
    sensors,
    calibrations,
    on="sensor_id"
)

overdue = combined[
    combined["days_since_calibration"] > max_days
]

overdue = overdue[
    ["sensor_id", "lab", "owner", "days_since_calibration"]
]

overdue_list = overdue.to_dict(orient="records")


with open(output_file, "w") as file:
    json.dump(overdue_list, file, indent=2)

