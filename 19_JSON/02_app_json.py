import os
import json
from pathlib import Path
os.chdir(Path(__file__).parent)

with open("appconfig.json",mode ="r",encoding="UTF-8") as file:
    json_string = file.read()

config_dict = json.loads(json_string)
print(config_dict['appname'])
print(config_dict['dataset_path'])
print(config_dict['dataset'][1])
