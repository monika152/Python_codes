# pip install ruamel.yaml

from ruamel.yaml import YAML

yaml_string = """
first_name : Sara
last_name : Meier
"""

yaml = YAML()
yaml_data = yaml.load(yaml_string)
print(yaml_data) # ordereddict([('first_name','Sara'),'last_name';'Meier)])

print(yaml_data['first_name'])
print(yaml_data['last_name'])
