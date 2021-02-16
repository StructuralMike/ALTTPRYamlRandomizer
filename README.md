# ALTTPRYamlRandomizer
Build Fun MultiWorld Yamls for you and your friends

This is meant to be used to modify your existing YAML settings for the [Archipelago MultiWorld](https://github.com/Berserker66/MultiWorld-Utilities/releases) repo.

## INSTRUCTIONS

Simply run **ALTTPRYamlRandomizer.py**

Every yaml in the /Player directory will be read, modified, and written to the /Output directory.
Modifications are done as per the settings defined in the provided **YamlRandomizer.yaml** file.

This tool relies a lot on the plando feature of Archipelago.
To enable this, you need to modify your Archipelago **host.yaml** file accordingly:

    plando_options: "items,texts"