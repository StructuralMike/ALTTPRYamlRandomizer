import random
import json

def importText(origins):
    text_data_file = './text_data.json'
    with open(text_data_file, "r", encoding='utf-8') as f:
        text_data = json.load(f)

    textPool = {
        'questions': set(),
        'choice_1s': set(),
        'choice_2s': set(),
        'ats': set(),
        'other': set()
        }

    for origin in origins:
        for category in textPool:
            textPool[category].update(text_data[origin][category])

    return textPool

def setDefaultText():
    text = {}
    text['game_over_menu'] = "{SPEED0}\nSave-Continue\nSave-Quit\nContinue"
    text['follower_no_enter'] = "Can't you take me some place nice."
    text['uncle_leaving_text'] = "I'm just going out for a pack of smokes."
    text['uncle_dying_sewer'] = "I've fallen and I can't get up, take this."
    text['tutorial_guard_1'] = "Only adults should travel at night."
    # 10
    text['tutorial_guard_2'] = "You can press X to see the Map."
    text['tutorial_guard_3'] = "Press the A button to lift things by you."
    text['tutorial_guard_4'] = "When you has a sword, press B to slash it."
    text['tutorial_guard_5'] = "このメッセージはニホンゴでそのまま" # on purpose
    text['tutorial_guard_6'] = "Are we really still reading these?"
    text['tutorial_guard_7'] = "Jeez! There really are a lot of things."
    text['priest_sanctuary_before_leave'] = "Go be a hero!"
    text['sanctuary_enter'] = "YAY!\nYou saved Zelda!"
    text['zelda_sanctuary_story'] = "Do you want to hear me say this again?\n{HARP}\n  ≥ no\n    yes\n{CHOICE}"
    text['priest_sanctuary_before_pendants'] = "Go'on and get them pendants so you can beat up Agahnim."
    text['priest_sanctuary_after_pendants_before_master_sword'] = "Kudos! But seriously, you should be getting the master sword, not having a kegger in here."
    text['priest_sanctuary_dying'] = "They took her to the castle! Take your sword and save her!"
    text['zelda_save_sewers'] = "You saved me!"
    text['priest_info'] = "So, I'm the dude that will protect Zelda. Don't worry, I got this covered."
    text['zelda_sanctuary_before_leave'] = "Be careful!"
    text['telepathic_intro'] = "{NOBORDER}\n{SPEED6}\nHey, come find me and help me!"
    # 20
    text['telepathic_reminder'] = "{NOBORDER}\n{SPEED6}\nI'm in the castle basement."
    text['zelda_go_to_throne'] = "Go north to the throne."
    text['zelda_push_throne'] = "Let's push it from the left!"
    text['zelda_switch_room_pull'] = "Pull this lever using A."
    text['zelda_save_lets_go'] = "Let's get out of here!"
    text['zelda_save_repeat'] = "I like talking, do you?\n  ≥ no\n    yes\n{CHOICE}"
    text['zelda_before_pendants'] = "You need to find all the pendants…\n\n\nNumpty."
    text['zelda_after_pendants_before_master_sword'] = "Very pretty pendants, but really you should be getting that sword in the forest!"
    text['telepathic_zelda_right_after_master_sword'] = "{NOBORDER}\n{SPEED6}\nHi @,\nHave you been thinking about me?\narrrrrgghh…\n… … …"
    text['zelda_sewers'] = "Just a little further to the Sanctuary."
    text['zelda_switch_room'] = "The Sanctuary!\n\nPull my finger"
    text['kakariko_saharalasa_wife'] = "Heya, @!\nLong time no see.\nYou want a master sword?\n\nWell good luck with that."
    text['kakariko_saharalasa_wife_sword_story'] = "It occurs to me that I like toast and jam, but cheese and crackers is better.\nYou like?\n  ≥ cheese\n    jam\n{CHOICE}"
    text['kakariko_saharalasa_wife_closing'] = "Anywho, I have things to do. You see those 2 ovens?\n\nYeah 2!\nWho has 2 ovens nowadays?"
    text['kakariko_saharalasa_after_master_sword'] = "Cool sword!\n\n\n…\n\n\n…\n\n\nPlease save us"
    text['kakariko_alert_guards'] = "GUARDS! HELP!\nThe creeper\n@ is here!"
    # 30
    text['sahasrahla_quest_have_pendants'] = "{BOTTOM}\nCool beans, but I think you should mosey on over to the lost woods."
    text['sahasrahla_quest_have_master_sword'] = "{BOTTOM}\nThat's a pretty sword, but I'm old, forgetful, and old. Why don't you go do all the hard work while I hang out in this hut."
    text['sahasrahla_quest_information'] = "{BOTTOM}\nSahasrahla, I am. You would do well to find the 3 pendants from the 3 dungeons in the Light World.\nUnderstand?\n  ≥ yes\n    no\n{CHOICE}"
    text['sahasrahla_bring_courage'] = "{BOTTOM}\nWhile you're here, could you do me a solid and get the green pendant from that dungeon?\n{HARP}\nI'll give you a present if you do."
    text['sahasrahla_have_ice_rod'] = "{BOTTOM}\nLike, I sit here, and tell you what to do?\n\n\nAlright, go and find all the maidens, there are, like, maybe 7 of them. I dunno anymore. I'm old."
    text['telepathic_sahasrahla_beat_agahnim'] = "{NOBORDER}\n{SPEED6}\nNice, so you beat Agahnim. Now you must beat Ganon. Good Luck!"
    text['telepathic_sahasrahla_beat_agahnim_no_pearl'] = "{NOBORDER}\n{SPEED6}\nOh, also you forgot the Moon Pearl, dingus. Go back and find it!"
    text['sahasrahla_have_boots_no_icerod'] = "{BOTTOM}\nCave in South East has a cool item."
    text['sahasrahla_have_courage'] = "{BOTTOM}\nLook, you have the green pendant! I'll give you something. Go kill the other two bosses for more pendant fun!"
    text['sahasrahla_found'] = "{BOTTOM}\nYup!\n\nI'm the old man you are looking for. I'll keep it short and sweet: Go into that dungeon, then bring me the green pendant and talk to me again."
    text['sign_rain_north_of_links_house'] = "↑ Dying Uncle\n  This way…"
    text['sign_north_of_links_house'] = "> Randomizer" #"> Randomizer The telepathic tiles can have hints!"
    text['sign_path_to_death_mountain'] = "Cave to lost, old man.\nGood luck."
    text['sign_lost_woods'] = "\n↑ Lost Woods"
    text['sign_zoras'] = "Danger!\nDeep water!\nZoras!"
    text['sign_outside_magic_shop'] = "Welcome to the Magic Shoppe"
    # 40
    text['sign_death_mountain_cave_back'] = "Cave away from sky cabbages"
    text['sign_east_of_links_house'] = "↓ Lake Hylia\n\n Also, a shop"
    text['sign_south_of_lumberjacks'] = "← Kakariko\n  Village"
    text['sign_east_of_desert'] = "← Desert\n\n     It's hot."
    text['sign_east_of_sanctuary'] = "↑→ Potions!\n\nWish waterfall"
    text['sign_east_of_castle'] = "→ East Palace\n\n← Castle"
    text['sign_north_of_lake'] = "\n Lake  Hiriah"
    text['sign_desert_thief'] = "Don't talk to me or touch my sign!"
    text['sign_lumberjacks_house'] = "Lumberjacks, Inc.\nYou see 'em, we saw 'em."
    text['sign_north_kakariko'] = "↓ Kakariko\n  Village"
    text['witch_bring_mushroom'] = "Double, double toil and trouble!\nBring me a mushroom!"
    text['witch_brewing_the_item'] = "This mushroom is busy brewing. Come back later."
    text['witch_assistant_no_bottle'] = "A bottle for your thoughts? or to put potions in."
    text['witch_assistant_no_empty_bottle'] = "Gotta use your stuff before you can get more."
    text['witch_assistant_informational'] = "Red is life\nGreen is magic\nBlue is both\nI'll heal you for free though."
    text['witch_assistant_no_bottle_buying'] = "If only you had something to put that in, like a bottle…"
    # 50
    text['potion_shop_no_empty_bottles'] = "Whoa, bucko!\nNo empty bottles."
    text['item_get_lamp'] = "Lamp! You can see in the dark, and light torches."
    text['item_get_boomerang'] = "Boomerang! Press START to select it."
    text['item_get_bow'] = "You're in bow mode now!"
    text['item_get_shovel'] = "This is my new mop. My friend George, he gave me this mop. It's a pretty good mop. It's not as good as my old mop. I miss my old mop. But it's still a good mop."
    text['item_get_magic_cape'] = "Finally! we get to play Invisble Man!"
    text['item_get_powder'] = "It's the powder. Let's cause some mischief!"
    text['item_get_flippers'] = "Splish! Splash! Let's go take a bath!"
    text['item_get_power_gloves'] = "Feel the power! You can now lift light rocks! Rock on!"
    text['item_get_pendant_courage'] = "We have the Pendant of Courage! How brave!"
    text['item_get_pendant_power'] = "We have the Pendant of Power! How robust!"
    text['item_get_pendant_wisdom'] = "We have the Pendant of Wisdom! How astute!"
    text['item_get_mushroom'] = "A Mushroom! Don't eat it. Find a witch."
    text['item_get_book'] = "It book! U R now litterit!"
    text['item_get_moonpearl'] = "I found a shiny marble! No more hops!"
    text['item_get_compass'] = "A compass! I can now find the boss."
    # 60
    text['item_get_map'] = "Yo! You found a MAP! Press X to see it."
    text['item_get_ice_rod'] = "It's the Ice Rod! Freeze Ray time."
    text['item_get_fire_rod'] = "A Rod that shoots fire? Let's burn all the things!"
    text['item_get_ether'] = "We can chill out with this!"
    text['item_get_bombos'] = "Let's set everything on fire, and melt things!"
    text['item_get_quake'] = "Time to make the earth shake, rattle, and roll!"
    text['item_get_hammer'] = "STOP!\n\nHammer Time!" # 66
    text['item_get_flute'] = "Finally! We can play the Song of Time!"
    text['item_get_cane_of_somaria'] = "Make blocks!\nThrow blocks!\nsplode Blocks!"
    text['item_get_hookshot'] = "BOING!!!\nBOING!!!\nSay no more…"
    text['item_get_bombs'] = "BOMBS! Use A to pick 'em up, throw 'em, get hurt!"
    text['item_get_bottle'] = "It's a terrarium. I hope we find a lizard!"
    text['item_get_big_key'] = "Yo! You got a Big Key!"
    text['item_get_titans_mitts'] = "So, like, you can now lift anything.\nANYTHING!"
    text['item_get_magic_mirror'] = "We could stare at this all day or, you know, beat Ganon…"
    text['item_get_fake_mastersword'] = "It's the Master Sword! …or not…\n\n         FOOL!"
    # 70
    text['post_item_get_mastersword'] = "{NOBORDER}\n{SPEED6}\n@, you got the sword!\n{CHANGEMUSIC}\nNow let's go beat up Agahnim!"
    text['item_get_red_potion'] = "Red goo to go! Nice!"
    text['item_get_green_potion'] = "Green goo to go! Nice!"
    text['item_get_blue_potion'] = "Blue goo to go! Nice!"
    text['item_get_bug_net'] = "Surprise Net! Let's catch stuff!"
    text['item_get_blue_mail'] = "Blue threads? Less damage activated!"
    text['item_get_red_mail'] = "You feel the power of the eggplant on your head."
    text['item_get_temperedsword'] = "Nice… I now have a craving for Cheetos."
    text['item_get_mirror_shield'] = "Pit would be proud!"
    text['item_get_cane_of_byrna'] = "It's the Blue Cane. You can now protect yourself with lag!"
    text['missing_big_key'] = "Something is missing…\nThe Big Key?"
    text['missing_magic'] = "Something is missing…\nMagic meter?"
    text['item_get_pegasus_boots'] = "Finally, it's bonking time!\nHold A to dash"
    text['talking_tree_info_start'] = "Whoa! I can talk again!"
    text['talking_tree_info_1'] = "Yank on the pitchfork in the center of town, ya heard it here."
    text['talking_tree_info_2'] = "Ganon is such a dingus, no one likes him, ya heard it here."
    # 80
    text['talking_tree_info_3'] = "There is a portal near the Lost Woods, ya heard it here."
    text['talking_tree_info_4'] = "Use bombs to quickly kill the Hinox, ya heard it here."
    text['talking_tree_other'] = "I can breathe!"
    text['item_get_pendant_power_alt'] = "We have the Pendant of Power! How robust!"
    text['item_get_pendant_wisdom_alt'] = "We have the Pendant of Wisdom! How astute!"
    text['game_shooting_choice'] = "20 rupees.\n5 arrows.\nWin rupees!\nWant to play?\n  ≥ yes\n    no\n{CHOICE}"
    text['game_shooting_yes'] = "Let's do this!"
    text['game_shooting_no'] = "Where are you going? Straight up!"
    text['game_shooting_continue'] = "Keep playing?\n  ≥ yes\n    no\n{CHOICE}"
    text['pond_of_wishing'] = "-Wishing Pond-\n\n On Vacation"
    text['pond_item_select'] = "Pick something\nto throw in.\n{ITEMSELECT}"
    text['pond_item_test'] = "You toss this?\n  ≥ yup\n    wrong\n{CHOICE}"
    text['pond_will_upgrade'] = "You're honest, so I'll give you a present."
    text['pond_item_test_no'] = "You sure?\n  ≥ oh yeah\n    um\n{CHOICE}"
    text['pond_item_test_no_no'] = "Well, I don't want it, so take it back."
    text['pond_item_boomerang'] = "I don't much like you, so have this worse Boomerang."
    # 90
    text['pond_item_shield'] = "I grant you the ability to block fireballs. Don't lose this to a pikit!"
    text['pond_item_silvers'] = "So, wouldn't it be nice to kill Ganon? These should help in the final phase."
    text['pond_item_bottle_filled'] = "Bottle Filled!\nMoney Saved!"
    text['pond_item_sword'] = "Thank you for the sword, here is a stick of butter."
    text['pond_of_wishing_happiness'] = "Happiness up!\nYou are now\nᚌᚋ happy!"
    text['pond_of_wishing_choice'] = "Your wish?\n  ≥more bombs\n   more arrows\n{CHOICE}"
    text['pond_of_wishing_bombs'] = "Woo-hoo!\nYou can now\ncarry ᚌᚋ bombs"
    text['pond_of_wishing_arrows'] = "Woo-hoo!\nYou can now\nhold ᚌᚋ arrows"
    text['pond_of_wishing_full_upgrades'] = "You have all I can give you, here are your rupees back."
    text['mountain_old_man_first'] = "Look out for holes, and monsters."
    text['mountain_old_man_deadend'] = "Oh, goody, hearts in jars! This place is creepy."
    text['mountain_old_man_turn_right'] = "Turn right. Let's get out of this place."
    text['mountain_old_man_lost_and_alone'] = "Hello. I can't see anything. Take me with you."
    text['mountain_old_man_drop_off'] = "Here's a thing to help you, good luck!"
    text['mountain_old_man_in_his_cave_pre_agahnim'] = "You need to beat the tower at the top of the mountain."
    text['mountain_old_man_in_his_cave'] = "You can find stuff in the tower at the top of this mountain.\nCome see me if you'd like to be healed."
    # A0
    text['mountain_old_man_in_his_cave_post_agahnim'] = "You should be heading to the castle… you have a portal there now.\nSay hi anytime you like."
    text['tavern_old_man_awake'] = "Life? Love? Happiness? The question you should really ask is: Was this generated by Stoops Alu or Stoops Jet?"
    text['tavern_old_man_unactivated_flute'] = "You should play that flute for the weathervane, cause reasons."
    text['tavern_old_man_know_tree_unactivated_flute'] = "You should play that flute for the weathervane, cause reasons."
    text['tavern_old_man_have_flute'] = "Life? Love? Happiness? The question you should really ask is: Was this generated by Stoops Alu or Stoops Jet?"
    text['chicken_hut_lady'] = "This is\nChristos' hut.\n\nHe's out, searching for a bow."
    text['running_man'] = "Catch me,\nIf you can!"
    text['game_race_sign'] = "Why are you reading this sign? Run!!!"
    text['sign_bumper_cave'] = "You need Cape, but not Hookshot"
    text['sign_catfish'] = "toss rocks\ntoss items\ntoss cookies"
    text['sign_north_village_of_outcasts'] = "↑ Skull Woods\n\n↓ Steve's Town"
    text['sign_south_of_bumper_cave'] = "\n→ Dark Sanctuary"
    text['sign_east_of_pyramid'] = "\n→ Dark Palace"
    text['sign_east_of_bomb_shop'] = "\n← Bomb Shoppe"
    text['sign_east_of_mire'] = "\n← Misery Mire\n no way in.\n no way out."
    text['sign_village_of_outcasts'] = "Have a Trulie Awesome Day!"
    # B0
    text['sign_before_wishing_pond'] = "waterfall\nup ahead\nmake wishes"
    text['sign_before_catfish_area'] = "→↑ Have you met Woeful Ike?"
    text['castle_wall_guard'] = "Looking for a Princess? Look downstairs."
    text['gate_guard'] = "No Lonks Allowed!"
    text['telepathic_tile_eastern_palace'] = "{NOBORDER}\nYou need a Bow to get past the red Eyegore. derpy"
    text['telepathic_tile_tower_of_hera_floor_4'] = "{NOBORDER}\nIf you find a shiny ball, you can be you in the Dark World."
    text['hylian_text_1'] = "%== %== %==\n ^ %==% ^\n%== ^%%^ ==^"
    text['mastersword_pedestal_translated'] = "A test of strength: If you have 3 pendants, I'm yours."
    text['telepathic_tile_spectacle_rock'] = "{NOBORDER}\n{NOBORDER}\nUse the Mirror, or the Hookshot and Hammer, to get to Tower of Hera!"
    text['telepathic_tile_swamp_entrance'] = "{NOBORDER}\nDrain the floodgate to raise the water here!"
    text['telepathic_tile_thieves_town_upstairs'] = "{NOBORDER}\nBlind hate's bright light."
    text['telepathic_tile_misery_mire'] = "{NOBORDER}\nLighting 4 torches will open your way forward!"
    text['hylian_text_2'] = "%%^= %==%\n ^ =%^=\n==%= ^^%^"
    text['desert_entry_translated'] = "Kneel before this stone, and magic will move around you."
    text['telepathic_tile_under_ganon'] = "Haha"
    text['telepathic_tile_palace_of_darkness'] = "{NOBORDER}\nThis is a funny looking Enemizer"
    # C0
    text['telepathic_tile_desert_bonk_torch_room'] = "{NOBORDER}\nThings can be knocked down, if you fancy yourself a dashing dude."
    text['telepathic_tile_castle_tower'] = "{NOBORDER}\nYou can reflect Agahnim's energy with Sword, Bug-net or Hammer."
    text['telepathic_tile_ice_large_room'] = "{NOBORDER}\nAll right stop collaborate and listen\nIce is back with my brand new invention"
    text['telepathic_tile_turtle_rock'] = "{NOBORDER}\nYou shall not pass… without the red cane"
    text['telepathic_tile_ice_entrance'] = "{NOBORDER}\nYou can use Fire Rod or Bombos to pass."
    text['telepathic_tile_ice_stalfos_knights_room'] = "{NOBORDER}\nKnock 'em down and then bomb them dead."
    text['telepathic_tile_tower_of_hera_entrance'] = "{NOBORDER}\nThis is a bad place, with a guy who will make you fall…\n\n\na lot."
    text['houlihan_room'] = "Have a Multiworld Tournament\nand we can list the winners here."
    text['caught_a_bee'] = "Caught a Bee\n  ≥ keep\n    release\n{CHOICE}"
    text['caught_a_fairy'] = "Caught Fairy!\n  ≥ keep\n    release\n{CHOICE}"
    text['no_empty_bottles'] = "Whoa, bucko!\nNo empty bottles."
    text['game_race_boy_time'] = "Your time was\nᚎᚍ min ᚌᚋ sec."
    text['game_race_girl'] = "You have 15 seconds,\nGo… Go… Go…"
    text['game_race_boy_success'] = "Nice!\nYou can have this trash!"
    text['game_race_boy_failure'] = "Too slow!\nI keep my\nprecious!"
    text['game_race_boy_already_won'] = "You already have your prize, dingus!"
    # D0
    text['game_race_boy_sneaky'] = "Thought you could sneak in, eh?"
    text['bottle_vendor_choice'] = "I gots bottles.\nYous gots 100 rupees?\n  ≥ I want\n    no way!"
    text['bottle_vendor_get'] = "Nice! Hold it up son! Show the world what you got!"
    text['bottle_vendor_no'] = "Fine! I didn't want your money anyway."
    text['bottle_vendor_already_collected'] = "Dude! You already have it."
    text['bottle_vendor_bee'] = "Cool! A bee! Here's 100 rupees."
    text['bottle_vendor_fish'] = "Whoa! A fish! You walked this all the way here?"
    text['hobo_item_get_bottle'] = "You think life is rough? I guess you can take my last item. Except this tent. That's MY tent!"
    text['blacksmiths_what_you_want'] = "Nice of you to come back!\nWould you like us mess with your sword?\n  ≥ Temper\n    It's fine\n{CHOICE}"
    text['blacksmiths_paywall'] = "It's 10 rupees\n  ≥ Easy\n    Hang on…\n{CHOICE}"
    text['blacksmiths_extra_okay'] = "Are you sure you're sure?\n  ≥ Ah, yup\n    Hang on…\n{CHOICE}"
    text['blacksmiths_tempered_already'] = "Whelp… We can't make this any better."
    text['blacksmiths_temper_no'] = "Oh, come by any time!"
    text['blacksmiths_bogart_sword'] = "We're going to have to take it to work on it."
    text['blacksmiths_get_sword'] = "Sword is done. Now, back to our bread!"
    text['blacksmiths_shop_before_saving'] = "I lost my friend. Help me find him!"
    # E0
    text['blacksmiths_shop_saving'] = "You found him! Colour me happy! Come back right away and we will bang on your sword."
    text['blacksmiths_collect_frog'] = "Ribbit! Ribbit! Let's find my partner. To the shop!"
    text['blacksmiths_still_working'] = "Something this precious takes time… Come back later."
    text['blacksmiths_saving_bows'] = "Thanks!\n\nThanks!"
    text['blacksmiths_hammer_anvil'] = "Dernt Take Er Jerbs!"
    text['dark_flute_boy_storytime'] = "Hi!\nI'm Stumpy\nI've been chillin' in this world for a while now, but I miss my flute. If I gave you a shovel, would you go digging for it?\n  ≥ sure\n    nahh\n{CHOICE}"
    text['dark_flute_boy_get_shovel'] = "Schaweet! Here you go. Happy digging!"
    text['dark_flute_boy_no_get_shovel'] = "Oh I see, not good enough for you… FINE!"
    text['dark_flute_boy_flute_not_found'] = "Still haven't found the item? Dig in the Light World around here, dingus!"
    text['dark_flute_boy_after_shovel_get'] = "So I gave you an item, and you're still here.\n\n\n\n\n\nI mean, we can sit here and stare at each other, if you like…\n\n\n\n\n\n\n\nFine, I guess you should just go."
    text['shop_fortune_teller_lw_hint_0'] = "{BOTTOM}\nBy the black cats, the book opens the desert"
    text['shop_fortune_teller_lw_hint_1'] = "{BOTTOM}\nBy the black cats, nothing doing"
    text['shop_fortune_teller_lw_hint_2'] = "{BOTTOM}\nBy the black cats, I'm cheap"
    text['shop_fortune_teller_lw_hint_3'] = "{BOTTOM}\nBy the black cats, am I cheap?"
    text['shop_fortune_teller_lw_hint_4'] = "{BOTTOM}\nBy the black cats, Zora lives at the end of the river"
    text['shop_fortune_teller_lw_hint_5'] = "{BOTTOM}\nBy the black cats, The Cape can pass through the barrier"
    text['shop_fortune_teller_lw_hint_6'] = "{BOTTOM}\nBy the black cats, Spin, Hammer, or Net to hurt Agahnim"
    text['shop_fortune_teller_lw_hint_7'] = "{BOTTOM}\nBy the black cats, You can jump in the well by the blacksmiths"
    text['shop_fortune_teller_lw_no_rupees'] = "{BOTTOM}\nThe black cats are hungry, come back with rupees"
    text['shop_fortune_teller_lw'] = "{BOTTOM}\nWelcome to the Fortune Shoppe!\nFancy a read?\n  ≥I must know\n   negative\n{CHOICE}"
    text['shop_fortune_teller_lw_post_hint'] = "{BOTTOM}\nFor ᚋᚌ rupees\nIt is done.\nBe gone!"
    text['shop_fortune_teller_lw_no'] = "{BOTTOM}\nWell then, why did you even come in here?"
    text['shop_fortune_teller_lw_hint_8'] = "{BOTTOM}\nBy the black cats, why you do?"
    text['shop_fortune_teller_lw_hint_9'] = "{BOTTOM}\nBy the black cats, panda crackers"
    text['shop_fortune_teller_lw_hint_10'] = "{BOTTOM}\nBy the black cats, the missing blacksmith is south of the Village of Outcasts"
    text['shop_fortune_teller_lw_hint_11'] = "{BOTTOM}\nBy the black cats, open chests to get stuff"
    text['shop_fortune_teller_lw_hint_12'] = "{BOTTOM}\nBy the black cats, you can buy a new bomb at the Bomb Shoppe"
    text['shop_fortune_teller_lw_hint_13'] = "{BOTTOM}\nBy the black cats, big bombs blow up cracked walls in pyramids"
    text['shop_fortune_teller_lw_hint_14'] = "{BOTTOM}\nBy the black cats, you need all the crystals to open Ganon's Tower"
    text['shop_fortune_teller_lw_hint_15'] = "{BOTTOM}\nBy the black cats, Silver Arrows will defeat Ganon in his final phase"
    text['dark_sanctuary'] = "For 20 rupees I'll tell you something?\nHow about it?\n  ≥ yes\n    no\n{CHOICE}"
    text['dark_sanctuary_hint_0'] = "I once was a tea kettle, but then I moved up in the world, and now you can see me as this. Makes you wonder. What I could be next time."
    # 100
    text['dark_sanctuary_no'] = "Then go away!"
    text['dark_sanctuary_hint_1'] = "There is a thief in the desert, he can open creepy chests that follow you. But now that we have that out of the way, Do you like my hair? I've spent eons getting it this way."
    text['dark_sanctuary_yes'] = "With Crystals 5&6, you can find a great fairy in the pyramid.\n\nFlomp Flomp, Whizzle Whomp"
    text['dark_sanctuary_hint_2'] = "All I can say is that my life is pretty plain,\nI like watchin' the puddles gather rain,\nAnd all I can do is just pour some tea for two,\nAnd speak my point of view but it's not sane,\nIt's not sane"
    text['sick_kid_no_bottle'] = "{BOTTOM}\nI'm sick! Show me a bottle, get something!"
    text['sick_kid_trade'] = "{BOTTOM}\nCool Bottle! Here's something for you."
    text['sick_kid_post_trade'] = "{BOTTOM}\nLeave me alone\nI'm sick. You have my item."
    text['desert_thief_sitting'] = "………………………"
    text['desert_thief_following'] = "why……………"
    text['desert_thief_question'] = "I was a thief, I open purple chests!\nKeep secret?\n  ≥ sure thing\n    never!\n{CHOICE}"
    text['desert_thief_question_yes'] = "Cool, bring me any purple chests you find."
    text['desert_thief_after_item_get'] = "You tell anyone and I will give you such a pinch!"
    text['desert_thief_reassure'] = "Bring chests. It's a secret to everyone."
    text['hylian_text_3'] = "^^ ^%=^= =%=\n=%% =%%=^\n==%^= %=^^%"
    text['tablet_ether_book'] = "Can you make things fall out of the sky? With the Master Sword, you can!"
    text['tablet_bombos_book'] = "Can you make things fall out of the sky? With the Master Sword, you can!"
    # 110
    text['magic_bat_wake'] = "You bum! I was sleeping! Where's my magic bolts?"
    text['magic_bat_give_half_magic'] = "How you like me now?"
    text['intro_main'] = "{INTRO}\n Episode  III\n{PAUSE3}\n A Link to\n   the Past\n{PAUSE3}\n  Randomizer\n{PAUSE3}\nAfter mostly disregarding what happened in the first two games.\n{PAUSE3}\nLink awakens to his uncle leaving the house.\n{PAUSE3}\nHe just runs out the door,\n{PAUSE3}\ninto the rainy night.\n{PAUSE3}\n{CHANGEPIC}\nGanon has moved around all the items in Hyrule.\n{PAUSE7}\nYou will have to find all the items necessary to beat Ganon.\n{PAUSE7}\nThis is your chance to be a hero.\n{PAUSE3}\n{CHANGEPIC}\nYou should probably beat Ganon.\n{PAUSE9}\n{CHANGEPIC}"
    text['intro_throne_room'] = "{IBOX}\nLook at this Stalfos on the throne."
    text['intro_zelda_cell'] = "{IBOX}\nIt is your time to shine!"
    text['intro_agahnim'] = "{IBOX}\nAlso, you need to defeat this guy!"
    text['pickup_purple_chest'] = "A curious box. Let's take it with us!"
    text['bomb_shop'] = "30 bombs for 100 rupees. Good deals all day!"
    text['bomb_shop_big_bomb'] = "30 bombs for 100 rupees, 100 rupees 1 BIG bomb. Good deals all day!"
    text['bomb_shop_big_bomb_buy'] = "Thanks!\nBoom goes the dynamite!"
    text['item_get_big_bomb'] = "YAY! press A to splode it!"
    text['kiki_second_extortion'] = "For 100 more, I'll open this place.\nHow about it?\n  ≥ open\n    nah\n{CHOICE}"
    text['kiki_second_extortion_no'] = "Heh, good luck getting in."
    text['kiki_second_extortion_yes'] = "Yay! Rupees!\nOkay, let's do this!"
    text['kiki_first_extortion'] = "I'm Kiki, I like rupees, may I have 10?\nHow about it?\n  ≥ yes\n    no\n{CHOICE}"
    text['kiki_first_extortion_yes'] = "Nice. I'll tag along with you for a bit."
    # 120
    text['kiki_first_extortion_no'] = "Pfft. I have no reason to hang. See ya!"
    text['kiki_leaving_screen'] = "No no no no no! We should play by my rules! Goodbye…"
    text['blind_in_the_cell'] = "You saved me!\nPlease get me out of here!"
    text['blind_by_the_light'] = "Aaaahhhh~!\nS-so bright~!"
    text['blind_not_that_way'] = "No! Don't go that way!"
    text['aginah_l1sword_no_book'] = "I once had a fish dinner. I still remember it to this day."
    text['aginah_l1sword_with_pendants'] = "Do you remember when I was young?\n\nI sure don't."
    text['aginah'] = "So, I've been living in this cave for years, and you think you can just come along and bomb open walls?"
    text['aginah_need_better_sword'] = "Once, I farted in this cave so bad all the jazz hands guys ran away and hid in the sand."
    text['aginah_have_better_sword'] = "Pandas are very vicious animals. Never forget…\n\n\n\n\nI never will"
    text['catfish'] = "You woke me from my nap! Take this, and get out!"
    text['catfish_after_item'] = "I don't have anything else for you!\nTake this!"
    # 12C
    text['lumberjack_right'] = "One of us always lies."
    text['lumberjack_left'] = "One of us always tells the truth."
    text['lumberjack_left_post_agahnim'] = "One of us likes peanut butter."
    text['fighting_brothers_right'] = "I walled off my brother Leo\n\nWhat a dingus.\n"
    # 130
    text['fighting_brothers_right_opened'] = "Now I should probably talk to him…"
    text['fighting_brothers_left'] = "Did you come from my brothers room?\n\nAre we cool?"
    text['maiden_crystal_1'] = "{SPEED2}\n{BOTTOM}\n{NOBORDER}\nI have a pretty red dress.\n{SPEED1}\nJust thought I would tell you."
    text['maiden_crystal_2'] = "{SPEED2}\n{BOTTOM}\n{NOBORDER}\nI have a pretty blue dress.\n{SPEED1}\nJust thought I would tell you."
    text['maiden_crystal_3'] = "{SPEED2}\n{BOTTOM}\n{NOBORDER}\nI have a pretty gold dress.\n{SPEED1}\nJust thought I would tell you."
    text['maiden_crystal_4'] = "{SPEED2}\n{BOTTOM}\n{NOBORDER}\nI have a pretty redder dress.\n{SPEED1}\nJust thought I would tell you."
    text['maiden_crystal_5'] = "{SPEED2}\n{BOTTOM}\n{NOBORDER}\nI have a pretty green dress.\n{SPEED1}\nJust thought I would tell you."
    text['maiden_crystal_6'] = "{SPEED2}\n{BOTTOM}\n{NOBORDER}\nI have a pretty green dress.\n{SPEED1}\nJust thought I would tell you."
    text['maiden_crystal_7'] = "{SPEED2}\n{BOTTOM}\n{NOBORDER}\nIt's about friggin time.\n{SPEED1}\nDo you know how long I've been waiting?"
    text['maiden_ending'] = "May the way of the hero lead to the Triforce"
    text['maiden_confirm_understood'] = "{SPEED2}\n{BOTTOM}\n{NOBORDER}\nCapisce?\n  ≥ Yes\n    No\n{CHOICE}"
    text['barrier_breaking'] = "What did the seven crystals say to Ganon's Tower?"
    text['maiden_crystal_7_again'] = "{SPEED2}\n{BOTTOM}\n{NOBORDER}\nIt's about friggin time.\n{SPEED1}\nDo you know how long I have been waiting?"
    text['agahnim_zelda_teleport'] = "I am a magician, and this is my act. Watch as I make this girl disappear"
    text['agahnim_magic_running_away'] = "And now, the end is near\nAnd so I face the final curtain\nMy friend, I'll say it clear\nI'll state my case, of which I'm certain\nI've lived a life that's full\nI've traveled each and every highway\nBut more, much more than this\nI did it my way"
    text['agahnim_hide_and_seek_found'] = "Peek-a-boo!"
    text['agahnim_defeated'] = "Arrrgggghhh. Well you're coming with me!"
    text['agahnim_final_meeting'] = "You have done well to come this far. Now, die!"
    # 142
    text['zora_meeting'] = "What do you want?\n  ≥ Flippers\n    Nothin'\n{CHOICE}"
    text['zora_tells_cost'] = "Fine! But they aren't cheap. You got 500 rupees?\n  ≥ Duh\n    Oh carp\n{CHOICE}"
    text['zora_get_flippers'] = "Here's some Flippers for you! Swim little fish, swim."
    text['zora_no_cash'] = "Fine!\nGo get some more money first."
    text['zora_no_buy_item'] = "Wah hoo! Well, whenever you want to see these gills, stop on by."
    text['kakariko_saharalasa_grandson'] = "My grandpa is over in the East. I'm bad with directions. I'll mark your map. Best of luck!\n{HARP}"
    text['kakariko_saharalasa_grandson_next'] = "Someday I'll be in a high school band!"
    text['dark_palace_tree_dude'] = "Did you know…\n\n\nA tree typically has many secondary branches supported clear of the ground by the trunk. This trunk typically contains woody tissue for strength, and vascular tissue to carry materials from one part of the tree to another."
    text['fairy_wishing_ponds'] = "\n-wishing pond-\n\nThrow item in?\n  ≥ Yesh\n    No\n{CHOICE}"
    text['fairy_wishing_ponds_no'] = "\n   stop it!"
    text['pond_of_wishing_no'] = "\n  fine then!"
    text['pond_of_wishing_return_item'] = "Okay. Here's your item back, cause I can't use it. I'm stuck in this fountain"
    text['pond_of_wishing_throw'] = "How many?\n  ≥ᚌᚋ rupees\n   ᚎᚍ rupees\n{CHOICE}"
    text['pond_pre_item_silvers'] = "I like you, so here's a thing you can use to beat up Ganon."
    # 150
    text['pond_of_wishing_great_luck'] = "\nis great luck"
    text['pond_of_wishing_good_luck'] = "\n is good luck"
    text['pond_of_wishing_meh_luck'] = "\n is meh luck"
    # Repurposed to no items in Randomizer
    text['pond_of_wishing_bad_luck'] = "Why you come in here and pretend like you have something this fountain wants? Come back with bottles!"
    text['pond_of_wishing_fortune'] = "by the way, your fortune,"
    text['item_get_14_heart'] = "3 more to go\n      ¼\nYay!"
    text['item_get_24_heart'] = "2 more to go\n      ½\nWhee!"
    text['item_get_34_heart'] = "1 more to go\n      ¾\nGood job!"
    text['item_get_whole_heart'] = "You got a whole ♥!!\nGo you!"
    text['item_get_sanc_heart'] = "You got a whole ♥!\nGo you!"
    text['fairy_fountain_refill'] = "Well done, lettuce have a cup of tea…"
    text['death_mountain_bullied_no_pearl'] = "The following license applies to the base patch for the randomizer.\n\nCopyright (c) 2017 LLCoolDave\n\nCopyright (c) 2020 Berserker66\n\nCopyright (c) 2020 CaitSith2\n\nCopyright 2016, 2017 Equilateral IT\n\n Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\", to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software."
    text['death_mountain_bullied_with_pearl'] = "The software is provided \"as is\", without warranty of any kind, express or implied, including but not limited to the warranties of\nmerchantability,\nfitness for a particular purpose and\nnoninfringement.\nIn no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Software or the use or other dealings in the software."
    text['death_mountain_bully_no_pearl'] = "Add garlic, ginger and apple and cook for 2 minutes. Add carrots, potatoes, garam masala and curry powder and stir well. Add tomato paste, stir well and slowly add red wine and bring to a boil. Add sugar, soy sauce and water, stir and bring to a boil again."
    text['death_mountain_bully_with_pearl'] = "I think I forgot how to smile…"
    text['shop_darkworld_enter'] = "It's dangerous outside, buy my crap for safety."
    # 160
    text['game_chest_village_of_outcasts'] = "Pay 30 rupees, open 2 chests. Are you lucky?\nSo, Play game?\n  ≥ play\n    never!\n{CHOICE}"
    text['game_chest_no_cash'] = "So, like, you need 30 rupees.\nSilly!"
    text['game_chest_not_played'] = "You want to play a game?\nTalk to me."
    text['game_chest_played'] = "You've opened the chests!\nTime to go."
    text['game_chest_village_of_outcasts_play'] = "Alright, brother!\nGo play!"
    text['shop_first_time'] = "Welcome to my shop! Select stuff with A.\nDO IT NOW!"
    text['shop_already_have'] = "So, like, you already have one of those."
    text['shop_buy_shield'] = "Thanks! Now you can block fire balls."
    text['shop_buy_red_potion'] = "Red goo, so good! It's like a fairy in a bottle, except you have to activate it yourself."
    text['shop_buy_arrows'] = "Arrows! Cause you were too lazy to look under some pots!"
    text['shop_buy_bombs'] = "You bought bombs. What, couldn't find any under bushes?"
    text['shop_buy_bee'] = "He's my best friend. Please take care of him, and never lose him."
    text['shop_buy_heart'] = "You really just bought this?"
    text['shop_first_no_bottle_buy'] = "Why does no one own bottles? Go find one first!"
    text['shop_buy_no_space'] = "You are carrying to much crap, go use some of it first!"
    text['ganon_fall_in'] = "You drove\naway my other\nself, Agahnim,\ntwo times…\nBut, I won't\ngive you the\nTriforce.\nI'll defeat\nyou!"
    # 170
    text['ganon_phase_3'] = "Can you beat\nmy darkness\ntechnique?"
    text['lost_woods_thief'] = "Did you just vent?"
    text['blinds_hut_dude'] = "I'm just some dude. This is Blind's hut."
    text['end_triforce'] = "{SPEED2}\n{MENU}\n{NOBORDER}\n     G G"
    text['toppi_fallen'] = "Ouch!\n\nYou Jerk!"
    text['kakariko_tavern_fisherman'] = "Don't argue\nwith a frozen\nDeadrock.\nHe'll never\nchange his\nposition!"
    text['thief_money'] = "It's a secret to everyone."
    text['thief_desert_rupee_cave'] = "So you, like, busted down my door, and are being a jerk by talking to me? Normally I would be angry and make you pay for it, but I bet you're just going to break all my pots and steal my 50 rupees."
    text['thief_ice_rupee_cave'] = "I'm a rupee pot farmer. One day I will take over the world with my skillz. Have you met my brother in the desert? He's way richer than I am."
    text['telepathic_tile_south_east_darkworld_cave'] = "~~ dev cave ~~\n  no farming\n   required"
    text['cukeman'] = "Hey mon!"
    text['cukeman_2'] = "You found Shabadoo, huh?\nNiiiiice."
    text['potion_shop_no_cash'] = "Yo! I'm not running a charity here."
    text['kakariko_powdered_chicken'] = "Smallhacker…\n\n\nWas hiding, you found me!\n\n\nOkay, you can leave now."
    text['game_chest_south_of_kakariko'] = "Pay 20 rupees, open 1 chest. Are you lucky?\nSo, Play game?\n  ≥ play\n    never!\n{CHOICE}"
    text['game_chest_play_yes'] = "Good luck then"
    # 180
    text['game_chest_play_no'] = "Well fine, I didn't want your rupees."
    text['game_chest_lost_woods'] = "Pay 100 rupees open 1 chest. Are you lucky?\nSo, Play game?\n  ≥ play\n    never!\n{CHOICE}"
    text['kakariko_flophouse_man_no_flippers'] = "I really hate mowing my yard.\nI moved my house and everyone else's to avoid it.\n{PAGEBREAK}\nI hope you don't mind."
    text['kakariko_flophouse_man'] = "I really hate mowing my yard.\nI moved my house and everyone else's to avoid it.\n{PAGEBREAK}\nI hope you don't mind."
    text['menu_start_2'] = "{MENU}\n{SPEED0}\n≥@'s house\n Sanctuary\n{CHOICE3}"
    text['menu_start_3'] = "{MENU}\n{SPEED0}\n≥@'s house\n Sanctuary\n Mountain Cave\n{CHOICE2}"
    text['menu_pause'] = "{SPEED0}\n≥continue\n save and quit\n{CHOICE3}"
    text['game_digging_choice'] = "Have 80 Rupees? Want to play digging game?\n  ≥yes\n   no\n{CHOICE}"
    text['game_digging_start'] = "Okay, use the shovel with Y!"
    text['game_digging_no_cash'] = "Shovel rental is 80 rupees.\nI have all day"
    text['game_digging_end_time'] = "Time's up!\nTime for you to go."
    text['game_digging_come_back_later'] = "Come back later, I have to bury things."
    text['game_digging_no_follower'] = "Something is following you. I don't like."
    text['menu_start_4'] = "{MENU}\n{SPEED0}\n≥@'s house\n Mountain Cave\n{CHOICE3}"
    # Start of new text data
    text['ganon_fall_in_alt'] = "You think you\nare ready to\nface me?\n\nI will not die\n\nunless you\ncomplete your\ngoals. Dingus!"
    text['ganon_phase_3_alt'] = "Got wax in\nyour ears?\nI cannot die!"
    # 190
    text['sign_east_death_mountain_bridge'] = "How did you get up here?"
    text['fish_money'] = "It's a secret to everyone."
    text['sign_ganons_tower'] = "You need all 7 crystals to enter."
    text['sign_ganon'] = "You need all 7 crystals to beat Ganon."
    text['ganon_phase_3_no_bow'] = "You have no bow. Dingus!"
    text['ganon_phase_3_no_silvers_alt'] = "You can't best me without silver arrows!"
    text['ganon_phase_3_no_silvers'] = "You can't best me without silver arrows!"
    text['ganon_phase_3_silvers'] = "Oh no! Silver! My one true weakness!"
    text['murahdahla'] = "Hello @. I\nam Murahdahla, brother of\nSahasrahla and Aginah. Behold the power of\ninvisibility.\n{PAUSE3}\n… … …\nWait! you can see me? I knew I should have\nhidden in  a hollow tree."
    return text

def defineTextTargets():
    textTargets = {
        'PROTECTED': [
            'intro_main',
            'intro_throne_room',
            'intro_zelda_cell',
            'intro_agahnim',
            'telepathic_reminder',
            'item_get_pendant_wisdom_alt',
            'item_get_pendant_power_alt',
            'pond_item_select',
            'maiden_crystal_1',
            'maiden_crystal_2',
            'maiden_crystal_3',
            'maiden_crystal_4',
            'maiden_crystal_5',
            'maiden_crystal_6',
            'maiden_crystal_7',
            'maiden_crystal_7_again',
            'death_mountain_bullied_no_pearl',
            'death_mountain_bullied_with_pearl',
            'death_mountain_bully_no_pearl',

            'end_triforce',

            'ganon_fall_in',
            'ganon_fall_in_alt',
            'ganon_phase_3_alt',
            'ganon_phase_3',
            'ganon_phase_3_no_bow',
            'ganon_phase_3_no_silvers_alt',
            'ganon_phase_3_no_silvers',
            'ganon_phase_3_silvers',

            'game_over_menu',
            'menu_pause',
            'menu_start_2',
            'menu_start_3',
            'menu_start_4',
            'sign_ganons_tower',
            'sign_ganon',
            'sahasrahla_bring_courage',
            'murahdahla',

            'item_get_big_key',
            'item_get_compass',
            'item_get_map',
            'item_get_bombs',
            'item_get_14_heart',
            'item_get_24_heart',
            'item_get_34_heart',

            'missing_magic',
            'zora_tells_cost',
            'bomb_shop'
        ],
        'CHOICES': [
            'kiki_second_extortion',
            'zelda_sanctuary_story',
            'zelda_save_repeat',
            'kakariko_saharalasa_wife_sword_story',
            'sahasrahla_quest_information',
            'game_shooting_choice',
            'game_shooting_continue',
            'pond_item_test',
            'pond_item_test_no',
            'pond_of_wishing_choice',
            'caught_a_bee',
            'caught_a_fairy',
            'bottle_vendor_choice',
            'blacksmiths_what_you_want',
            'blacksmiths_paywall',
            'blacksmiths_extra_okay',
            'shop_fortune_teller_lw',
            'dark_sanctuary',
            'desert_thief_question',
            'kiki_second_extortion',
            'kiki_first_extortion',
            'maiden_confirm_understood',
            'zora_meeting',
            'fairy_wishing_ponds',
            'pond_of_wishing_throw',
            'game_chest_village_of_outcasts',
            'game_chest_south_of_kakariko',
            'game_chest_lost_woods',
            'game_digging_choice',

            'zelda_go_to_throne',
            'zelda_push_throne',
            'zelda_switch_room_pull',
            'zelda_before_pendants',
            'zelda_after_pendants_before_master_sword',
            'zelda_sewers',
            'zelda_switch_room',

        ],
        'NOBORDER': [
            'telepathic_intro',
            'telepathic_zelda_right_after_master_sword',
            'telepathic_sahasrahla_beat_agahnim',
            'telepathic_sahasrahla_beat_agahnim_no_pearl'
        ],
        'BOOKREADS': [
            'mastersword_pedestal_translated',
            'tablet_ether_book',
            'tablet_bombos_book',
        ],
        'HINTTILES': [
            'telepathic_tile_eastern_palace',
            'telepathic_tile_tower_of_hera_floor_4',
            'telepathic_tile_spectacle_rock',
            'telepathic_tile_swamp_entrance',
            'telepathic_tile_thieves_town_upstairs',
            'telepathic_tile_misery_mire',
            'telepathic_tile_under_ganon',
            'telepathic_tile_palace_of_darkness',
            'telepathic_tile_desert_bonk_torch_room',
            'telepathic_tile_castle_tower',
            'telepathic_tile_ice_large_room',
            'telepathic_tile_turtle_rock',
            'telepathic_tile_ice_entrance',
            'telepathic_tile_ice_stalfos_knights_room',
            'telepathic_tile_tower_of_hera_entrance',
            'houlihan_room',
            'telepathic_tile_south_east_darkworld_cave'
        ],
        'SIGNS': [
            'sign_rain_north_of_links_house',
            'sign_north_of_links_house',
            'sign_path_to_death_mountain',
            'sign_lost_woods',
            'sign_zoras',
            'sign_outside_magic_shop',
            'sign_death_mountain_cave_back',
            'sign_east_of_links_house',
            'sign_south_of_lumberjacks',
            'sign_east_of_desert',
            'sign_east_of_sanctuary',
            'sign_east_of_castle',
            'sign_north_of_lake',
            'sign_desert_thief',
            'sign_lumberjacks_house',
            'sign_north_kakariko',
            'game_race_sign',
            'sign_bumper_cave',
            'sign_catfish',
            'sign_north_village_of_outcasts',
            'sign_south_of_bumper_cave',
            'sign_east_of_pyramid',
            'sign_east_of_bomb_shop',
            'sign_east_of_mire',
            'sign_village_of_outcasts',
            'sign_before_wishing_pond',
            'sign_before_catfish_area',
            'sign_east_death_mountain_bridge',
        ],
        'ITEMGET': [
            'item_get_lamp',
            'item_get_boomerang',
            'item_get_bow',
            'item_get_shovel',
            'item_get_magic_cape',
            'item_get_powder',
            'item_get_flippers',
            'item_get_power_gloves',
            'item_get_pendant_courage',
            'item_get_pendant_power',
            'item_get_pendant_wisdom',
            'item_get_mushroom',
            'item_get_book',
            'item_get_moonpearl',
            'item_get_ice_rod',
            'item_get_fire_rod',
            'item_get_ether',
            'item_get_bombos',
            'item_get_quake',
            'item_get_hammer',
            'item_get_flute',
            'item_get_cane_of_somaria',
            'item_get_hookshot',
            'item_get_bottle',
            'item_get_titans_mitts',
            'item_get_magic_mirror',
            'item_get_fake_mastersword',
            'post_item_get_mastersword',
            'item_get_red_potion',
            'item_get_green_potion',
            'item_get_blue_potion',
            'item_get_bug_net',
            'item_get_blue_mail',
            'item_get_red_mail',
            'item_get_temperedsword',
            'item_get_mirror_shield',
            'item_get_cane_of_byrna',
            'item_get_pegasus_boots',
            'item_get_whole_heart',
            'item_get_sanc_heart'
        ],
        'BOTTOMS': [
            'sick_kid_no_bottle',
            'sick_kid_trade',
            'sick_kid_post_trade',
            'shop_fortune_teller_lw_hint_0',
            'shop_fortune_teller_lw_hint_1',
            'shop_fortune_teller_lw_hint_2',
            'shop_fortune_teller_lw_hint_3',
            'shop_fortune_teller_lw_hint_4',
            'shop_fortune_teller_lw_hint_5',
            'shop_fortune_teller_lw_hint_6',
            'shop_fortune_teller_lw_hint_7',
            'shop_fortune_teller_lw_no_rupees',
            'shop_fortune_teller_lw_post_hint',
            'shop_fortune_teller_lw_no',
            'shop_fortune_teller_lw_hint_8',
            'shop_fortune_teller_lw_hint_9',
            'shop_fortune_teller_lw_hint_10',
            'shop_fortune_teller_lw_hint_11',
            'shop_fortune_teller_lw_hint_12',
            'shop_fortune_teller_lw_hint_13',
            'shop_fortune_teller_lw_hint_14',
            'shop_fortune_teller_lw_hint_15',
            'sahasrahla_quest_have_pendants',
            'sahasrahla_quest_have_master_sword',
            'sahasrahla_have_ice_rod',
            'sahasrahla_have_boots_no_icerod',
            'sahasrahla_have_courage',
            'sahasrahla_found'
        ],
        'OTHERS': [
            'follower_no_enter',
            'uncle_leaving_text',
            'uncle_dying_sewer',
            'tutorial_guard_1',
            'tutorial_guard_2',
            'tutorial_guard_3',
            'tutorial_guard_4',
            'tutorial_guard_5',
            'tutorial_guard_6',
            'tutorial_guard_7',
            'priest_sanctuary_before_leave',
            'sanctuary_enter',
            'priest_sanctuary_before_pendants',
            'priest_sanctuary_after_pendants_before_master_sword',
            'priest_sanctuary_dying',
            'priest_info',
            'zelda_sanctuary_before_leave',
            'zelda_save_lets_go',
            'zelda_save_sewers',
            'kakariko_saharalasa_wife',
            'kakariko_saharalasa_wife_closing',
            'kakariko_saharalasa_after_master_sword',
            'kakariko_alert_guards',
            'witch_bring_mushroom',
            'witch_brewing_the_item',
            'witch_assistant_no_bottle',
            'witch_assistant_no_empty_bottle',
            'witch_assistant_informational',
            'witch_assistant_no_bottle_buying',
            'potion_shop_no_empty_bottles',
            'missing_big_key',
            'talking_tree_info_start',
            'talking_tree_info_1',
            'talking_tree_info_2',
            'talking_tree_info_3',
            'talking_tree_info_4',
            'talking_tree_other',
            'game_shooting_yes',
            'game_shooting_no',
            'pond_of_wishing',
            'pond_will_upgrade',
            'pond_item_test_no_no',
            'pond_item_boomerang',
            'pond_item_shield',
            'pond_item_silvers',
            'pond_item_bottle_filled',
            'pond_item_sword',
            'pond_of_wishing_happiness',
            'pond_of_wishing_bombs',
            'pond_of_wishing_arrows',
            'pond_of_wishing_full_upgrades',
            'mountain_old_man_first',
            'mountain_old_man_deadend',
            'mountain_old_man_turn_right',
            'mountain_old_man_lost_and_alone',
            'mountain_old_man_drop_off',
            'mountain_old_man_in_his_cave_pre_agahnim',
            'mountain_old_man_in_his_cave',
            'mountain_old_man_in_his_cave_post_agahnim',
            'tavern_old_man_awake',
            'tavern_old_man_unactivated_flute',
            'tavern_old_man_know_tree_unactivated_flute',
            'tavern_old_man_have_flute',
            'chicken_hut_lady',
            'running_man',
            'castle_wall_guard',
            'gate_guard',
            'hylian_text_1',
            'hylian_text_2',
            'desert_entry_translated',
            'no_empty_bottles',
            'game_race_boy_time',
            'game_race_girl',
            'game_race_boy_success',
            'game_race_boy_failure',
            'game_race_boy_already_won',
            'game_race_boy_sneaky',
            'bottle_vendor_get',
            'bottle_vendor_no',
            'bottle_vendor_already_collected',
            'bottle_vendor_bee',
            'bottle_vendor_fish',
            'hobo_item_get_bottle',
            'blacksmiths_tempered_already',
            'blacksmiths_temper_no',
            'blacksmiths_bogart_sword',
            'blacksmiths_get_sword',
            'blacksmiths_shop_before_saving',
            'blacksmiths_shop_saving',
            'blacksmiths_collect_frog',
            'blacksmiths_still_working',
            'blacksmiths_saving_bows',
            'blacksmiths_hammer_anvil',
            'dark_flute_boy_storytime',
            'dark_flute_boy_get_shovel',
            'dark_flute_boy_no_get_shovel',
            'dark_flute_boy_flute_not_found',
            'dark_flute_boy_after_shovel_get',
            'dark_sanctuary_hint_0',
            'dark_sanctuary_no',
            'dark_sanctuary_hint_1',
            'dark_sanctuary_yes',
            'dark_sanctuary_hint_2',
            'desert_thief_sitting',
            'desert_thief_following',
            'desert_thief_question_yes',
            'desert_thief_after_item_get',
            'desert_thief_reassure',
            'hylian_text_3',
            'magic_bat_wake',
            'magic_bat_give_half_magic',
            'pickup_purple_chest',
            'bomb_shop_big_bomb',
            'bomb_shop_big_bomb_buy',
            'item_get_big_bomb',
            'kiki_second_extortion_no',
            'kiki_second_extortion_yes',
            'kiki_first_extortion_yes',
            'kiki_first_extortion_no',
            'kiki_leaving_screen',
            'blind_in_the_cell',
            'blind_by_the_light',
            'blind_not_that_way',
            'aginah_l1sword_no_book',
            'aginah_l1sword_with_pendants',
            'aginah',
            'aginah_need_better_sword',
            'aginah_have_better_sword',
            'catfish',
            'catfish_after_item',
            'lumberjack_right',
            'lumberjack_left',
            'lumberjack_left_post_agahnim',
            'fighting_brothers_right',
            'fighting_brothers_right_opened',
            'fighting_brothers_left',
            'maiden_ending',
            'barrier_breaking',
            'agahnim_zelda_teleport',
            'agahnim_magic_running_away',
            'agahnim_hide_and_seek_found',
            'agahnim_defeated',
            'agahnim_final_meeting',
            'zora_get_flippers',
            'zora_no_cash',
            'zora_no_buy_item',
            'kakariko_saharalasa_grandson',
            'kakariko_saharalasa_grandson_next',
            'dark_palace_tree_dude',
            'fairy_wishing_ponds_no',
            'pond_of_wishing_no',
            'pond_of_wishing_return_item',
            'pond_pre_item_silvers',
            'pond_of_wishing_great_luck',
            'pond_of_wishing_good_luck',
            'pond_of_wishing_meh_luck',
            'pond_of_wishing_bad_luck',
            'pond_of_wishing_fortune',
            'fairy_fountain_refill',
            'death_mountain_bully_with_pearl',
            'shop_darkworld_enter',
            'game_chest_no_cash',
            'game_chest_not_played',
            'game_chest_played',
            'game_chest_village_of_outcasts_play',
            'shop_first_time',
            'shop_already_have',
            'shop_buy_shield',
            'shop_buy_red_potion',
            'shop_buy_arrows',
            'shop_buy_bombs',
            'shop_buy_bee',
            'shop_buy_heart',
            'shop_first_no_bottle_buy',
            'shop_buy_no_space',
            'lost_woods_thief',
            'blinds_hut_dude',
            'toppi_fallen',
            'kakariko_tavern_fisherman',
            'thief_money',
            'thief_desert_rupee_cave',
            'thief_ice_rupee_cave',
            'cukeman',
            'cukeman_2',
            'potion_shop_no_cash',
            'kakariko_powdered_chicken',
            'game_chest_play_yes',
            'game_chest_play_no',
            'kakariko_flophouse_man_no_flippers',
            'kakariko_flophouse_man',
            'game_digging_start',
            'game_digging_no_cash',
            'game_digging_end_time',
            'game_digging_come_back_later',
            'game_digging_no_follower',
            'fish_money'
        ]
    }
    return textTargets

def fitsOnSign(text,signSize=3):
    linecount = 0
    lines = text.split('\n')
    for line in lines:
        if '{' not in line:
            linecount += 1
            try:
                words = line.split(' ')
                length = 0
                for word in words:
                    if (length + 1 + len(word)) >= 15:
                        linecount += 1
                        length = len(word)
                    else:
                        length += (1 + len(word))
            except:
                pass
    return (linecount <= signSize)

def constructChoice(textpool):
    question = random.sample(textpool['questions'],1)[0]
    if len(question) > 14:
        while True:
            testSentence = random.sample(textpool['other'],1)[0]
            if fitsOnSign(testSentence,signSize=1):
                question = testSentence + ' ' + question
                break
            else:
                pass
    answer1 = random.sample(textpool['choice_1s'],1)[0]
    answer2 = random.sample(textpool['choice_2s'],1)[0]
    sentence = '{}\n{}\n{}'.format(question,answer1,answer2)
    sentence += '\n{CHOICE}'
    return sentence

def constructDialogue(textpool,maxsize=3,options=['none']):
    sentence = random.sample(textpool,1)[0]
    while True:
        testSentence = '{} {}'.format(sentence,random.sample(textpool,1)[0])
        if fitsOnSign(testSentence,signSize=maxsize):
            sentence = testSentence
        else:
            break

    if len(sentence) < 13:
        sentence = '\n ' + sentence

    if 'none' not in options:
        for option in options:
            if option == 'bottom':
                sentence = '{BOTTOM}\n' + sentence
            elif option == 'noborder':
                sentence = '{NOBORDER}\n' + sentence

    return sentence    

def randomText(shuffleGroups,textPool,textTargets):
    newText = {}

    dialoguePool = textPool['ats'].union(textPool['other'])
    for group in shuffleGroups:
        if group == 'CHOICES':
            for target in textTargets[group]:
                newText[target] = constructChoice(textPool)

        elif group == 'ITEMGET' or group == 'SIGNS':
            for target in textTargets[group]:
                newText[target] = constructDialogue(dialoguePool,maxsize=3)
        
        elif group == 'NOBORDER':
            for target in textTargets[group]:
                newText[target] = constructDialogue(dialoguePool,maxsize=random.choice([3,4,5,6,7,8]),options=['noborder'])

        elif group == 'BOTTOMS':
            for target in textTargets[group]:
                newText[target] = constructDialogue(dialoguePool,maxsize=random.choice([3,4,5,6,7,8]),options=['bottom'])
        
        else:
            for target in textTargets[group]:
                newText[target] = constructDialogue(dialoguePool,maxsize=random.choice([3,4,5,6,7,8]))

    return newText

def textomizer(input_yamls,parameters):
    allowed_origins = ['Z3','OoT']
    if parameters['origins']:
        origins = [origin for origin in parameters['origins'] if origin in allowed_origins]
    else:
        origins = allowed_origins
    textPool = importText(origins)
    textTargets = defineTextTargets()

    pairs = {
        'choice-dialogue': ['CHOICES'], 
        'people': ['OTHERS', 'NOBORDER', 'BOTTOMS'],
        'signs': ['SIGNS'],
        'item_pickup': ['ITEMGET'],
        'hints': ['HINTTILES']
    }
    shuffleGroups = []
    for group in parameters['categories']:
        if group in pairs:
            shuffleGroups.extend(pairs[group])

    for player,settings in input_yamls.items():
        plandoTexts = randomText(shuffleGroups,textPool,textTargets)
#        if random.random() < 0.25:
#            plandoTexts['menu_pause'] = '{SPEED0}\n≥not save-quit\n not continue\n{CHOICE3}'
#            links = ['house', 'shack', 'den', 'hole', 'crib', 'cave', 'dump', 'shanty']
#            plandoTexts['menu_start_2'] = '{MENU}\n{SPEED0}\n≥@\'s ' + random.choice(links) + '\n Sanctuary\n{CHOICE3}'
#            plandoTexts['menu_start_3'] = '{MENU}\n{SPEED0}\n≥@\'s ' + random.choice(links) + '\n Dankuary\n Gary\'s Grotto\n{CHOICE2}'

        settings['plando_texts'] = []
        for target,entry in plandoTexts.items():
            settings['plando_texts'].append({'text': entry, 'at': target})

        input_yamls[player] = settings
