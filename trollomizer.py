import random
from ruamel import yaml
import os

def genLocations():
    LOCATIONS = [
                ["Ganons Tower - Big Key Chest","GanonDungeon"],
                ["Ganons Tower - Big Key Room - Left","GanonDungeon"],
                ["Ganons Tower - Big Key Room - Right","GanonDungeon"],
                ["Ganons Tower - Bob's Chest","GanonDungeon"],
                ["Ganons Tower - Bob's Torch","GanonDungeon"],
                ["Ganons Tower - Firesnake Room","GanonDungeon"],
                ["Ganons Tower - Hope Room - Left","GanonDungeon"],
                ["Ganons Tower - Hope Room - Right","GanonDungeon"],
                ["Ganons Tower - Map Chest","GanonDungeon"],
                ["Ganons Tower - Tile Room","GanonDungeon"],
                ["Ganons Tower - Big Chest","GanonDungeon"],
                ["Ganons Tower - Compass Room - Bottom Left","GanonDungeon"],
                ["Ganons Tower - Compass Room - Bottom Right","GanonDungeon"],
                ["Ganons Tower - Compass Room - Top Left","GanonDungeon"],
                ["Ganons Tower - Compass Room - Top Right","GanonDungeon"],
                ["Ganons Tower - DMs Room - Bottom Left","GanonDungeon"],
                ["Ganons Tower - DMs Room - Bottom Right","GanonDungeon"],
                ["Ganons Tower - DMs Room - Top Left","GanonDungeon"],
                ["Ganons Tower - DMs Room - Top Right","GanonDungeon"],
                ["Ganons Tower - Mini Helmasaur Room - Left","GanonDungeon"],
                ["Ganons Tower - Mini Helmasaur Room - Right","GanonDungeon"],
                ["Ganons Tower - Validation Chest","GanonDungeon"],
                ["Ganons Tower - Pre-Moldorm Chest","GanonDungeon"],
                ["Ganons Tower - Randomizer Room - Bottom Left","GanonDungeon"],
                ["Ganons Tower - Randomizer Room - Bottom Right","GanonDungeon"],
                ["Ganons Tower - Randomizer Room - Top Left","GanonDungeon"],
                ["Ganons Tower - Randomizer Room - Top Right","GanonDungeon"],

                ["Castle Tower - Dark Maze","Dungeon"],
                ["Castle Tower - Room 03","Dungeon"],
                ["Palace of Darkness - Big Chest","Dungeon"],
                ["Palace of Darkness - Big Key Chest","Dungeon"],
                ["Palace of Darkness - Boss","Dungeon"],
                ["Palace of Darkness - Compass Chest","Dungeon"],
                ["Palace of Darkness - Dark Basement - Left","Dungeon"],
                ["Palace of Darkness - Dark Basement - Right","Dungeon"],
                ["Palace of Darkness - Dark Maze - Bottom","Dungeon"],
                ["Palace of Darkness - Dark Maze - Top","Dungeon"],
                ["Palace of Darkness - Harmless Hellway","Dungeon"],
                ["Palace of Darkness - Map Chest","Dungeon"],
                ["Palace of Darkness - Shooter Room","Dungeon"],
                ["Palace of Darkness - Stalfos Basement","Dungeon"],
                ["Palace of Darkness - The Arena - Bridge","Dungeon"],
                ["Palace of Darkness - The Arena - Ledge","Dungeon"],
                ["Desert Palace - Big Chest","Dungeon"],
                ["Desert Palace - Big Key Chest","Dungeon"],
                ["Desert Palace - Boss","Dungeon"],
                ["Desert Palace - Compass Chest","Dungeon"],
                ["Desert Palace - Map Chest","Dungeon"],
                ["Desert Palace - Torch","Dungeon"],
                ["Hyrule Castle - Boomerang Chest","Dungeon"],
                ["Hyrule Castle - Map Chest","Dungeon"],
                ["Hyrule Castle - Zelda's Cell","Dungeon"],
                ["Sanctuary","Dungeon"],
                ["Sewers - Dark Cross","Dungeon"],
                ["Sewers - Secret Room - Left","Dungeon"],
                ["Sewers - Secret Room - Middle","Dungeon"],
                ["Sewers - Secret Room - Right","Dungeon"],
                ["Ice Palace - Big Chest","Dungeon"],
                ["Ice Palace - Big Key Chest","Dungeon"],
                ["Ice Palace - Boss","Dungeon"],
                ["Ice Palace - Compass Chest","Dungeon"],
                ["Ice Palace - Freezor Chest","Dungeon"],
                ["Ice Palace - Iced T Room","Dungeon"],
                ["Ice Palace - Map Chest","Dungeon"],
                ["Ice Palace - Spike Room","Dungeon"],
                ["Misery Mire - Big Chest","Dungeon"],
                ["Misery Mire - Big Key Chest","Dungeon"],
                ["Misery Mire - Boss","Dungeon"],
                ["Misery Mire - Bridge Chest","Dungeon"],
                ["Misery Mire - Compass Chest","Dungeon"],
                ["Misery Mire - Main Lobby","Dungeon"],
                ["Misery Mire - Map Chest","Dungeon"],
                ["Misery Mire - Spike Chest","Dungeon"],
                ["Skull Woods - Big Chest","Dungeon"],
                ["Skull Woods - Big Key Chest","Dungeon"],
                ["Skull Woods - Boss","Dungeon"],
                ["Skull Woods - Bridge Room","Dungeon"],
                ["Skull Woods - Compass Chest","Dungeon"],
                ["Skull Woods - Map Chest","Dungeon"],
                ["Skull Woods - Pinball Room","Dungeon"],
                ["Skull Woods - Pot Prison","Dungeon"],
                ["Swamp Palace - Big Chest","Dungeon"],
                ["Swamp Palace - Big Key Chest","Dungeon"],
                ["Swamp Palace - Boss","Dungeon"],
                ["Swamp Palace - Compass Chest","Dungeon"],
                ["Swamp Palace - Entrance","Dungeon"],
                ["Swamp Palace - Flooded Room - Left","Dungeon"],
                ["Swamp Palace - Flooded Room - Right","Dungeon"],
                ["Swamp Palace - Map Chest","Dungeon"],
                ["Swamp Palace - Waterfall Room","Dungeon"],
                ["Swamp Palace - West Chest","Dungeon"],
                ["Thieves' Town - Ambush Chest","Dungeon"],
                ["Thieves' Town - Attic","Dungeon"],
                ["Thieves' Town - Big Chest","Dungeon"],
                ["Thieves' Town - Big Key Chest","Dungeon"],
                ["Thieves' Town - Blind's Cell","Dungeon"],
                ["Thieves' Town - Boss","Dungeon"],
                ["Thieves' Town - Compass Chest","Dungeon"],
                ["Thieves' Town - Map Chest","Dungeon"],
                ["Tower of Hera - Basement Cage","Dungeon"],
                ["Tower of Hera - Big Chest","Dungeon"],
                ["Tower of Hera - Big Key Chest","Dungeon"],
                ["Tower of Hera - Boss","Dungeon"],
                ["Tower of Hera - Compass Chest","Dungeon"],
                ["Tower of Hera - Map Chest","Dungeon"],
                ["Turtle Rock - Big Chest","Dungeon"],
                ["Turtle Rock - Big Key Chest","Dungeon"],
                ["Turtle Rock - Boss","Dungeon"],
                ["Turtle Rock - Chain Chomps","Dungeon"],
                ["Turtle Rock - Compass Chest","Dungeon"],
                ["Turtle Rock - Crystaroller Room","Dungeon"],
                ["Turtle Rock - Eye Bridge - Bottom Left","Dungeon"],
                ["Turtle Rock - Eye Bridge - Bottom Right","Dungeon"],
                ["Turtle Rock - Eye Bridge - Top Left","Dungeon"],
                ["Turtle Rock - Eye Bridge - Top Right","Dungeon"],
                ["Turtle Rock - Roller Room - Left","Dungeon"],
                ["Turtle Rock - Roller Room - Right","Dungeon"],
                ["Eastern Palace - Big Chest","Dungeon"],
                ["Eastern Palace - Big Key Chest","Dungeon"],
                ["Eastern Palace - Boss","Dungeon"],
                ["Eastern Palace - Cannonball Chest","Dungeon"],
                ["Eastern Palace - Compass Chest","Dungeon"],
                ["Eastern Palace - Map Chest","Dungeon"],

                ["Pyramid Fairy - Left","MainQuest"],
                ["Pyramid Fairy - Right","MainQuest"],
                ["Master Sword Pedestal","MainQuest"],
                ["Ice Rod Cave","MainQuest"],
                ["Link's Uncle","MainQuest"],
                ["Secret Passage","MainQuest"],
                ["Link's House","MainQuest"],
                ["Sahasrahla","MainQuest"],
                ["Blacksmith","MainQuest"],
                ["Ether Tablet","MainQuest"],
                ["Flute Spot","MainQuest"],
                ["Catfish","MainQuest"],
                ["Stumpy","MainQuest"],
                ["Old Man","MainQuest"],
                ["King Zora","MainQuest"],
                ["Library","MainQuest"],

                ["Purple Chest","SideQuest"],
                ["Magic Bat","SideQuest"],
                ["Potion Shop","SideQuest"],
                ["Sick Kid","SideQuest"],
                ["Bottle Merchant","SideQuest"],
                ["Hobo","SideQuest"],

                ["Lumberjack Tree","LumberjackTree"],

                ["Chest Game","Minigame"],
                ["Maze Race","Minigame"],
                ["Digging Game","Minigame"],

                ["Bombos Tablet","Overworld"],
                ["Bumper Cave Ledge","Overworld"],
                ["Hookshot Cave - Bottom Left","Overworld"],
                ["Hookshot Cave - Top Left","Overworld"],
                ["Hookshot Cave - Top Right","Overworld"],
                ["Hookshot Cave - Bottom Right","Overworld"],
                ["Spike Cave","Overworld"],
                ["Mimic Cave","Overworld"],
                ["Hype Cave - Generous Guy","Overworld"],
                ["Mini Moldorm Cave - Generous Guy","Overworld"],
                ["Peg Cave","Overworld"],
                ["Brewery","Overworld"],
                ["C-Shaped House","Overworld"],
                ["Hype Cave - Bottom","Overworld"],
                ["Hype Cave - Middle Left","Overworld"],
                ["Hype Cave - Middle Right","Overworld"],
                ["Hype Cave - Top","Overworld"],
                ["Mire Shed - Left","Overworld"],
                ["Mire Shed - Right","Overworld"],
                ["Pyramid","Overworld"],
                ["Superbunny Cave - Bottom","Overworld"],
                ["Superbunny Cave - Top","Overworld"],
                ["Paradox Cave Lower - Far Left","Overworld"],
                ["Paradox Cave Lower - Far Right","Overworld"],
                ["Paradox Cave Lower - Left","Overworld"],
                ["Paradox Cave Lower - Middle","Overworld"],
                ["Paradox Cave Lower - Right","Overworld"],
                ["Paradox Cave Upper - Left","Overworld"],
                ["Paradox Cave Upper - Right","Overworld"],
                ["Spectacle Rock","Overworld"],
                ["Spectacle Rock Cave","Overworld"],
                ["Spiral Cave","Overworld"],
                ["Aginah's Cave","Overworld"],
                ["Blind's Hideout - Far Left","Overworld"],
                ["Blind's Hideout - Far Right","Overworld"],
                ["Blind's Hideout - Left","Overworld"],
                ["Blind's Hideout - Right","Overworld"],
                ["Blind's Hideout - Top","Overworld"],
                ["Cave 45","Overworld"],
                ["Checkerboard Cave","Overworld"],
                ["Chicken House","Overworld"],
                ["Floodgate Chest","Overworld"],
                ["Graveyard Cave","Overworld"],
                ["Kakariko Tavern","Overworld"],
                ["Kakariko Well - Bottom","Overworld"],
                ["Kakariko Well - Left","Overworld"],
                ["Kakariko Well - Middle","Overworld"],
                ["Kakariko Well - Right","Overworld"],
                ["Kakariko Well - Top","Overworld"],
                ["King's Tomb","Overworld"],
                ["Lake Hylia Island","Overworld"],
                ["Lost Woods Hideout","Overworld"],
                ["Mini Moldorm Cave - Far Left","Overworld"],
                ["Mini Moldorm Cave - Far Right","Overworld"],
                ["Mini Moldorm Cave - Left","Overworld"],
                ["Mini Moldorm Cave - Right","Overworld"],
                ["Mushroom","Overworld"],
                ["Bonk Rock Cave","Overworld"],
                ["Sahasrahla's Hut - Left","Overworld"],
                ["Sahasrahla's Hut - Middle","Overworld"],
                ["Sahasrahla's Hut - Right","Overworld"],
                ["Sunken Treasure","Overworld"],
                ["Waterfall Fairy - Left","Overworld"],
                ["Waterfall Fairy - Right","Overworld"],
                ["Zora's Ledge","Overworld"],

                ['Eastern Palace - Boss', 'Boss'],
                ['Desert Palace - Boss', 'Boss'],
                ['Tower of Hera - Boss', 'Boss'],
                ['Palace of Darkness - Boss', 'Boss'],
                ['Thieves\' Town - Boss', 'Boss'],
                ['Skull Woods - Boss', 'Boss'],
                ['Swamp Palace - Boss', 'Boss'],
                ['Ice Palace - Boss', 'Boss'],
                ['Misery Mire - Boss', 'Boss'],
                ['Turtle Rock - Boss', 'Boss'],

                ['Tower of Hera - Map Chest', 'Dungeon'],
                ['Tower of Hera - Compass Chest', 'Dungeon'],
                ['Tower of Hera - Big Chest', 'Dungeon'],
                ['Thieves\' Town - Blind\'s Cell', 'Dungeon'],
                ['Skull Woods - Map Chest', 'Dungeon'],
                ['Skull Woods - Big Chest', 'Dungeon'],
                ['Skull Woods - Pinball Room', 'Dungeon'],
                ['Skull Woods - Compass Chest', 'Dungeon'],
                ['Skull Woods - West Lobby Pot Key', 'Dungeon'],
                ['Skull Woods - Spike Corner Key Drop', 'Dungeon'],
                ["Floating Island","Overworld"],
                ["Desert Ledge","Overworld"]
                ]
    return LOCATIONS

def genDungeons():
    DUNGEONS = [
        'Eastern Palace',
        'Desert Palace',
        'Tower of Hera',
        'Palace of Darkness',
        'Swamp Palace',
        'Skull Woods',
        'Thieves\' Town',
        'Ice Palace',
        'Misery Mire',
        'Turtle Rock'
    ]
    xtalDungeons = random.sample(DUNGEONS,7)
    pendantDungeons = []
    for d in DUNGEONS:
        if d not in xtalDungeons:
            pendantDungeons.append(d)
    return xtalDungeons,pendantDungeons

def genGame(crystals):
    xtalDungeons,pendantDungeons = genDungeons()
    medallions = {'Misery Mire': random.choice(['Bombos','Ether','Quake']), 'Turtle Rock': random.choice(['Bombos','Ether','Quake'])}

    # Moon Pearl, Hammer, ProgressiveGlove, Swords, and Bows are considered always accessible and not considered for ped
    required = set()
    if 'Skull Woods' in xtalDungeons:
        required.add('Fire Rod')
    if 'Swamp Palace' in xtalDungeons:
        required.add('Magic Mirror')
        required.add('Hookshot')
    if 'Misery Mire' in xtalDungeons:
        required.add('Progressive Glove')
        required.add('Flute')
        required.add(medallions['Misery Mire'])
    if 'Turtle Rock' in xtalDungeons:
        required.add('Progressive Glove')
        required.add('Fire Rod')
        required.add('Ice Rod')
        required.add(medallions['Turtle Rock'])
    if 'Ice Palace' in xtalDungeons:
        required.add('Progressive Glove')
        required.add('Flippers')
        if 'Fire Rod' not in required and 'Bombos' not in required:
            required.add(random.sample(['Fire Rod', 'Bombos'],1)[0])
    if 'Desert Palace' in xtalDungeons and ('Flute' not in required and 'Magic Mirror' not in required):
        add = random.choice([['Book of Mudora'],['Flute','Magic Mirror']])
        for a in add:
            required.add(a)
    if 'Tower of Hera' in xtalDungeons:
        if 'Magic Mirror' not in required and 'Hookshot' not in required:
            required.add(random.choice(['Magic Mirror', 'Hookshot']))

    pendantRequired = set()
    if 'Skull Woods' in pendantDungeons:
        pendantRequired.add('Fire Rod')
    if 'Swamp Palace' in pendantDungeons:
        pendantRequired.add('Magic Mirror')
        pendantRequired.add('Hookshot')
    if 'Misery Mire' in pendantDungeons:
        pendantRequired.add('Progressive Glove')
        pendantRequired.add('Flute')
        pendantRequired.add(medallions['Misery Mire'])
    if 'Turtle Rock' in pendantDungeons:
        pendantRequired.add('Progressive Glove')
        pendantRequired.add('Fire Rod')
        pendantRequired.add('Ice Rod')
        pendantRequired.add(medallions['Turtle Rock'])
    if 'Ice Palace' in pendantDungeons:
        pendantRequired.add('Progressive Glove')
        pendantRequired.add('Flippers')
        if 'Fire Rod' not in pendantRequired and 'Bombos' not in pendantRequired:
            if 'Bombos' not in required:
                pendantRequired.add('Bombos')
            elif 'Fire Rod' not in required:
                pendantRequired.add('Fire Rod')
            else:
                pendantRequired.add(random.sample(['Fire Rod', 'Bombos'],1)[0])
    if 'Desert Palace' in pendantDungeons and ('Flute' not in pendantRequired and 'Magic Mirror' not in pendantRequired):
        if 'Book of Mudora' not in required:
            pendantRequired.add('Book of Mudora')
        elif 'Flute' not in required and 'Magic Mirror' not in required:
            pendantRequired.add('Flute')
            pendantRequired.add('Magic Mirror')
        else:
            add = random.choice([['Book of Mudora'],['Flute','Magic Mirror']])
            for a in add:
                pendantRequired.add(a)
    if 'Tower of Hera' in pendantDungeons:
        if 'Magic Mirror' not in required:
            pendantRequired.add('Magic Mirror')
        if 'Hookshot' not in required:
            pendantRequired.add('Hookshot')
        else:
            pendantRequired.add(random.choice(['Magic Mirror', 'Hookshot']))


    return xtalDungeons, pendantDungeons, required, pendantRequired, medallions

def trollYamls(players,amount):
    trolls = min([len(players),amount])
    if trolls > 0:
        return random.sample(players,trolls)
    else:
        return ['None']

def trollomizer(input_yamls,parameters):

    players = []
    for player in input_yamls:
        players.append(player)

    cutslow = trollYamls(players,parameters['cutsceneslow'])
    menuslow = trollYamls(players,parameters['menuslow'])
    fastheart = trollYamls(players,parameters['fastheart'])
    pedestal = trollYamls(players,parameters['pedestal'])
    agahnim = trollYamls(players,parameters['agahnim'])

    for player,settings in input_yamls.items():
        if 'local_items' not in settings:
            settings['local_items'] = []
        if 'Moon Pearl' not in settings['local_items']:
            settings['local_items'].append('Moon Pearl')

        if player in cutslow:
            settings['rom']['cutscenespeed'] = {'normal': 0, 'slow': 1, 'fast': 0, 'blazing': 0}

        if player in menuslow:
            settings['rom']['menuspeed'] = {'normal': 0, 'instant': 0, 'double': 0, 'triple': 0, 'quadruple': 0, 'half': 1}

        if player in fastheart:
            settings['rom']['heartbeep'] = {'double': 1, 'normal': 0, 'half': 0, 'quarter': 0, 'off': 0}

        xtalDungeons, pendantDungeons, required, pendantRequired, medallions = genGame(crystals=7)

        if 'plando_items' not in settings:
            settings['plando_items'] = []

        pedSelection = {}
        for item in required:
            if item not in pendantRequired:
                pedSelection[item] = 1
        if player in pedestal:
            settings['plando_items'].append(
                {
                    'items': pedSelection,
                    'world': False,
                    'from_pool': True,
                    'location': 'Master Sword Pedestal'
                }
            )
        jackSelection = {}
        for item in required:
            jackSelection[item] = 1
        if player in pedestal:
            for item in pendantRequired:
                jackSelection[item] = 1

        if player in agahnim:
            settings['plando_items'].append(
                {
                    'items': jackSelection,
                    'world': False,
                    'from_pool': True,
                    'location': 'Lumberjack Tree'
                }
            )            
        if player in pedestal or player in agahnim:
            xtalLocations = []
            for dungeon in xtalDungeons:
                xtalLocations.append('{} - Prize'.format(dungeon))
            xtalLayout = {
                'items': {
                    'Crystal 1': 1,
                    'Crystal 2': 1,
                    'Crystal 3': 1,
                    'Crystal 4': 1,
                    'Crystal 5': 1,
                    'Crystal 6': 1,
                    'Crystal 7': 1,
                },
                'world': False,
                'from_pool': True,
                'locations': xtalLocations
            }
            settings['plando_items'].append(xtalLayout)

            pendantLocations = []
            for dungeon in pendantDungeons:
                pendantLocations.append('{} - Prize'.format(dungeon))
            pendantLayout = {
                'items': {
                    'Green Pendant': 1,
                    'Red Pendant': 1,
                    'Blue Pendant': 1
                },
                'world': False,
                'from_pool': True,
                'locations': pendantLocations
            }
            settings['plando_items'].append(pendantLayout)
            
            settings['misery_mire_medallion'] = {'random': 0, 'Ether': 0, 'Bombos': 0, 'Quake': 0}
            settings['misery_mire_medallion'][medallions['Misery Mire']] = 1
            settings['turtle_rock_medallion'] = {'random': 0, 'Ether': 0, 'Bombos': 0, 'Quake': 0}
            settings['turtle_rock_medallion'][medallions['Turtle Rock']] = 1

        usefulItems = ['Pegasus Boots', 'Bug Catching Net', 'Blue Boomerang', 'Red Boomerang', 'Mushroom', 'Magic Powder', 'Lamp', 'Shovel', 'Cane of Byrna', 'Cape', 'Progressive Glove', 'Magic Upgrade (1/2)', 'Progressive Shield', 'Rupees (300)']
        usefulItems += ['Boss Heart Container'] * 4
        if player in agahnim or player in pedestal:
            if 'Quake' not in medallions:
                usefulItems += ['Quake']
            if 'Ether' not in medallions:
                usefulItems += ['Ether']
            if 'Bombos' not in medallions:
                usefulItems += ['Bombos']
        usefulItems += ['Bottle ({})'.format(random.choice(['Green Potion', 'Red Potion', 'Blue Potion', 'Good Bee', 'Fairy']))]
        usefulItems += ['Bottle ({})'.format(random.choice(['Green Potion', 'Red Potion', 'Blue Potion', 'Good Bee', 'Fairy']))]
        start_cnt = parameters['startinventory']['min']
        start_max = parameters['startinventory']['min']
        while True:
            if start_cnt <= start_max:
                if random.random() < 0.5:
                    start_cnt += 1
                else:
                    break
            else:
                break
        if start_cnt > 0:
            startItems = random.sample(usefulItems, start_cnt)
            for item in startItems:
                if item not in settings['startinventory']:
                    settings['startinventory'][item] = 1
                else:
                    settings['startinventory'][item] += 1
        
        input_yamls[player] = settings
