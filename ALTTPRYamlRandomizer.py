from ruamel import yaml
import os
from textomizer import textomizer
from trollomizer import trollomizer
from locationizer import locationizer

input_yamls = {}
for file in os.listdir("./Players/"):
    if file.endswith(".yaml"):
        input_yaml = os.path.join('Players', file)
        with open(input_yaml, "r", encoding='utf-8') as f:
            input_yamls[input_yaml] = yaml.load(f, Loader=yaml.RoundTripLoader)

yamlRandomizerSettings = 'YamlRandomizer.yaml'
with open(yamlRandomizerSettings, "r", encoding='utf-8') as f:
    yamlSettings = yaml.load(f, Loader=yaml.RoundTripLoader)

if yamlSettings['textomizer']['enabled']:
    textomizer(input_yamls,yamlSettings['textomizer'])

if yamlSettings['trollomizer']['enabled']:
    trollomizer(input_yamls,yamlSettings['trollomizer'])

if yamlSettings['locationizer']['enabled']:
    locationizer(input_yamls,yamlSettings['locationizer'])

for input_yaml,settings in input_yamls.items():
    output_file = os.path.join('Output', 'multi_' + os.path.basename(input_yaml))
    with open(output_file, "w+", encoding='utf-8') as f:
        yaml.dump(settings,f, Dumper=yaml.RoundTripDumper, encoding='utf-8', allow_unicode=True, default_flow_style=False)

