import random
import base64
import math

def generateItemPool(amount):
    tc = 112
    items = {
        'Arrows (10)': math.ceil(23/tc*amount),
        'Bombs (3)': math.ceil(17/tc*amount),
        'Bee': math.ceil(1/tc*amount),
        'Bee Trap': math.ceil(1/tc*amount),
        'Rupee (1)': math.ceil(1/tc*amount),
        'Rupees (5)': math.ceil(4/tc*amount),
        'Rupees (20)': math.ceil(28/tc*amount),
        'Rupees (50)': math.ceil(7/tc*amount),
        'Rupees (100)': math.ceil(3/tc*amount),
        'Rupees (300)': math.ceil(3/tc*amount),
        'Piece of Heart': math.ceil(24/tc*amount),
    }
    return items

def rollSetting(options):
    settings = []
    weights = []
    for option,weight in options.items():
        settings.append(option)
        weights.append(weight)
    return random.choices(settings,weights,k=1)[0]

def locationizer(input_yamls,parameters):
    LOCATIONS = [
                ["Ganons Tower - Big Key Chest","Dungeon"],
                ["Ganons Tower - Big Key Room - Left","Dungeon"],
                ["Ganons Tower - Big Key Room - Right","Dungeon"],
                ["Ganons Tower - Bob's Chest","Dungeon"],
                ["Ganons Tower - Bob's Torch","Dungeon"],
                ["Ganons Tower - Firesnake Room","Dungeon"],
                ["Ganons Tower - Hope Room - Left","Dungeon"],
                ["Ganons Tower - Hope Room - Right","Dungeon"],
                ["Ganons Tower - Map Chest","Dungeon"],
                ["Ganons Tower - Tile Room","Dungeon"],
                ["Ganons Tower - Big Chest","Dungeon"],
                ["Ganons Tower - Compass Room - Bottom Left","Dungeon"],
                ["Ganons Tower - Compass Room - Bottom Right","Dungeon"],
                ["Ganons Tower - Compass Room - Top Left","Dungeon"],
                ["Ganons Tower - Compass Room - Top Right","Dungeon"],
                ["Ganons Tower - DMs Room - Bottom Left","Dungeon"],
                ["Ganons Tower - DMs Room - Bottom Right","Dungeon"],
                ["Ganons Tower - DMs Room - Top Left","Dungeon"],
                ["Ganons Tower - DMs Room - Top Right","Dungeon"],
                ["Ganons Tower - Mini Helmasaur Room - Left","Dungeon"],
                ["Ganons Tower - Mini Helmasaur Room - Right","Dungeon"],
                ["Ganons Tower - Validation Chest","Dungeon"],
                ["Ganons Tower - Pre-Moldorm Chest","Dungeon"],
                ["Ganons Tower - Randomizer Room - Bottom Left","Dungeon"],
                ["Ganons Tower - Randomizer Room - Bottom Right","Dungeon"],
                ["Ganons Tower - Randomizer Room - Top Left","Dungeon"],
                ["Ganons Tower - Randomizer Room - Top Right","Dungeon"],

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
                ["Sewers - Dark Cross","Dungeon"],
                ["Sewers - Secret Room - Left","Dungeon"],
                ["Sewers - Secret Room - Middle","Dungeon"],
                ["Sewers - Secret Room - Right","Dungeon"],
                ["Sanctuary","Dungeon"],

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

                ['Skull Woods - Map Chest', 'Dungeon'],
                ['Skull Woods - Big Chest', 'Dungeon'],
                ['Skull Woods - Pinball Room', 'Dungeon'],
                ['Skull Woods - Compass Chest', 'Dungeon'],
                ["Skull Woods - Big Key Chest","Dungeon"],
                ["Skull Woods - Boss","Dungeon"],
                ["Skull Woods - Bridge Room","Dungeon"],
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

                ["Pyramid Fairy - Left","FetchQuest"],
                ["Pyramid Fairy - Right","FetchQuest"],
                ["Sahasrahla","FetchQuest"],
                ["Ether Tablet","FetchQuest"],
                ["Flute Spot","FetchQuest"],
                ["Old Man","FetchQuest"],
                ["Blacksmith","FetchQuest"],
                ["Purple Chest","FetchQuest"],
                ["Magic Bat","FetchQuest"],
                ["Potion Shop","FetchQuest"],
                ["Sick Kid","FetchQuest"],

                ["Lumberjack Tree","LumberjackTree"],
                ["Master Sword Pedestal","MasterSwordPedestal"],

                ["Chest Game","Overworld"],
                ["Maze Race","Overworld"],
                ["Digging Game","Overworld"],
                ["Link's House","Overworld"],
                ["Link's Uncle","Overworld"],
                ["Secret Passage","Overworld"],
                ["Ice Rod Cave","Overworld"],
                ["Catfish","Overworld"],
                ["Stumpy","Overworld"],
                ["King Zora","Overworld"],
                ["Library","Overworld"],
                ["Bottle Merchant","Overworld"],
                ["Hobo","Overworld"],
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
                ["Floating Island","Overworld"],
                ["Desert Ledge","Overworld"]
                ]

    for player,settings in input_yamls.items():

        barren_regions = parameters['barren_regions']
        # Check if keysanity, otherwise remove dungeon locations
        if 'Dungeon' in barren_regions:
            sanities = ['map_shuffle','compass_shuffle','smallkey_shuffle', 'bigkey_shuffle']
            fullsanity = True
            for sanity in sanities:
                if sanity in settings:
                    settings[sanity] = rollSetting(settings[sanity])
                    if settings[sanity] == 'off':
                        fullsanity = False
                else:
                    fullsanity = False
            
            if not fullsanity:
                barren_regions.remove('Dungeon')
                    
        TRASH_LOCATIONS = []
        for location,group in LOCATIONS:
            if group in parameters['barren_regions']:
                TRASH_LOCATIONS.append(location)

        # Remove already plando'd locations
        if 'plando_items' in settings:
            for item in settings['plando_items']:
                if 'world' in item and item['world'] == False:
                    if 'location' in item:
                        try:
                            TRASH_LOCATIONS.remove(item['location'])
                        except:
                            pass
                    elif 'locations' in item:
                        for location in item['locations']:
                            try:
                                TRASH_LOCATIONS.remove(location)
                            except:
                                pass
        else:
            settings['plando_items'] = []

        items = generateItemPool(len(TRASH_LOCATIONS))
        barren_plando = {
            'items': items,
            'from_pool': False,
            'world': False,
            'locations': TRASH_LOCATIONS
        }
        settings['plando_items'].append(barren_plando)

        input_yamls[player] = settings
