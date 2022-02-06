import os
from ruamel.yaml import YAML
from pathlib import Path
os.chdir(Path(__file__).parent)


with open("appconfig.yaml",mode ="r",encoding="UTF-8") as file:
    yaml_string = file.read()

yaml = YAML()

config_dict = yaml.load(yaml_string)
print(config_dict['appname'])
print(config_dict['version'])
print(config_dict['authors'])