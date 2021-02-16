import random

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

def genTrollName():
    names = [
        'Gnent','Nad','Ayle','Iste','Lam','Rstynn','Tann','Oelee','Ker','Amsey','Ssag',
        'Llang','Mmark','Lind','Nes','Elly','Egui','Wall','Uince','Ike','Ldoch','Atha',
        'Uba','Kigm','Nell','Wiss','Nanc','Lis','Nin','Arla','Hoth','Bel','Ddiet','Rton'
    ]
    return ' '.join(random.sample(names,2))

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
        
        if settings['name'] == 'random':
            settings['name'] = genTrollName()

        input_yamls[player] = settings
