# ALTTPRYamlRandomizer
Build Fun MultiWorld Yamls for you and your friends

This is meant to be used to modify your existing YAML settings for the [Archipelago MultiWorld](https://github.com/Berserker66/MultiWorld-Utilities/releases) repo.

## INSTRUCTIONS

Simply run **ALTTPRYamlRandomizer.py**

Every yaml in the /Player directory will be read, modified, and written to the /Output directory.
Modifications are done as per the settings defined in the provided **YamlRandomizer.yaml** file.

This tool relies a lot on the plando feature of Archipelago.
To enable this, you need to modify your Archipelago **host.yaml** before you generate seeds:

    plando_options: "items,texts"

## DETAILS

I've made a YAML tool that I'd like to share with you. It started out as a way for me to add some social fun stuff to my group's multiworld sessions - and it has been really well received so I figured I'd put together something that could actually be utilised by others.

It features 3 main things.

1) The Textomizer
    Using the newly added text-plandomizer, I have created an algorithm that generates unique zelda-based dialogue to be plandod onto any defined categories (signs, people, choices, item-receives).

2) The Trollomizer
    Specify the exact amount of players to get random progression item on Lumberjack or Pedestal, slow menu speed, or fast heart rate sound effects.
    You can also give out a random amount of starting items that are only semi-useful (i.e bugnet, boomerang, 1 bossheart etc).

3) The Locationizer
    Here you can specify regions to pre-fill with trash items.
    Are you playing door-rando and dont wanna waste time in the overworld?
    Specify "Overworld and FetchQuest" and you'll be guaranteed fast low% door-rando fun.
    Do you hate dungeons? Then enable full keysanity and specify "dungeons".