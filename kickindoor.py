"""
Program: kickindoor.py
Author: Andy Volesky
Last date modified: 12/14/2021

The purpose of this program:

Make a dungeon crawl style game.

"""

from random import randint
import random

char = dict(lvl=1, hp=50, atk=5, defense = 0)
char_inv = {}
equipped_wep = {}
equipped_armor = {}


i_lvl1 = {'+1 sword': 1, '+1 helm': 1, '+1 boots': 1, '+1 chest': 1, '+1 shield': 1, 'Healing Potion': 20}
i_lvl2 = {'+2 sword': 2, '+2 helm': 2, '+2 boots': 2, '+2 chest': 2, '+2 shield': 2, 'Healing Potion': 20}
i_lvl3 = {'+3 sword': 3, '+3 helm': 3, '+3 boots': 3, '+3 chest': 3, '+3 shield': 3, 'Healing Potion': 20}
i_lvl4 = {'+4 sword': 4, '+4 helm': 4, '+4 boots': 4, '+4 chest': 4, '+4 shield': 4, 'Healing Potion': 20}

#tier 1 monster dictionary
m_lvl1 = [{'name':'Goblin', 'atk': 2, 'defense': 1, 'hp': 10},
          {'name':'Giant Rat', 'atk': 2, 'defense': 1, 'hp': 10},
          {'name':'Gremlin', 'atk': 2, 'defense': 1, 'hp': 10},
          {'name':'Kobold', 'atk': 2, 'defense': 1, 'hp': 10}]
#tier 2 monster dictionary
m_lvl2 = [{'name':'Worg', 'atk': 4, 'defense': 2, 'hp': 15},
          {'name':'Skeleton Warrior', 'atk': 4, 'defense': 2, 'hp': 18},
          {'name':'Gnoll', 'atk': 3, 'defense': 3, 'hp': 10},
          {'name':'Xorn', 'atk': 3, 'defense': 2, 'hp': 15}]
#tier 3 monster dictionary
m_lvl3 = [{'name':'Mummy', 'atk': 6, 'defense': 3, 'hp': 20},
          {'name':'Slaad', 'atk': 5, 'defense': 3, 'hp': 20},
          {'name':'Gelatinous Cube', 'atk': 3, 'defense': 4, 'hp': 21},
          {'name':'Doppelganger', 'atk': 5 , 'defense': 3, 'hp': 20}]
#tier 4 monster dictionary
m_lvl4 = [{'name':'Mind Flayer', 'atk': 7, 'defense': 5, 'hp': 25},
          {'name':'Gorgon', 'atk': 6, 'defense': 6, 'hp': 30},
          {'name':'Orc Knight', 'atk': 7, 'defense': 6, 'hp': 20},
          {'name':'Dire Bear', 'atk': 6, 'defense': 3, 'hp': 50}]

char['name'] = input("Enter char name: ")


#function for choosing a random action for the monster
def rand_action():
    actions = ['Attack', 'Parry', 'Block']
    action = random.choice(actions)
    return action

#function for choosing which loot table to use based on char level and adding the item to character inventory
def loot():
    if char['lvl'] == 2 or char['lvl'] == 3:
        print(i_lvl1)
        item_choice = input('Choose loot: ')
        if item_choice != '+1 sword' and item_choice != '+1 helm' and item_choice != '+1 boots' and item_choice != '+1 chest' and item_choice != '+1 shield' and item_choice != 'Healing Potion' and item_choice != '+2 sword' and item_choice != '+2 helm' and item_choice != '+2 boots' and item_choice != '+2 chest' and item_choice != '+2 shield' and item_choice != '+3 sword' and item_choice != '+3 helm' and item_choice != '+3 boots' and item_choice != '+3 chest' and item_choice != '+3 shield' and item_choice != '+4 sword' and item_choice != '+4 helm' and item_choice != '+4 boots' and item_choice != '+4 chest' and item_choice != '+4 shield':
            item_choice = input('Choose loot: ')
        char_inv[item_choice] = i_lvl1[item_choice]
        print(f'Your inventory contains {char_inv}')
    elif char['lvl'] == 4 or char['lvl'] == 5 or char['lvl'] == 6:
        print(i_lvl2)
        item_choice = input('Choose loot: ')
        if item_choice != '+1 sword' and item_choice != '+1 helm' and item_choice != '+1 boots' and item_choice != '+1 chest' and item_choice != '+1 shield' and item_choice != 'Healing Potion' and item_choice != '+2 sword' and item_choice != '+2 helm' and item_choice != '+2 boots' and item_choice != '+2 chest' and item_choice != '+2 shield' and item_choice != '+3 sword' and item_choice != '+3 helm' and item_choice != '+3 boots' and item_choice != '+3 chest' and item_choice != '+3 shield' and item_choice != '+4 sword' and item_choice != '+4 helm' and item_choice != '+4 boots' and item_choice != '+4 chest' and item_choice != '+4 shield':
            item_choice = input('Choose loot: ')
        char_inv[item_choice] = i_lvl2[item_choice]
        print(f'Your inventory contains {char_inv}')
    elif char['lvl'] == 7 or char['lvl'] == 8 or char['lvl'] == 9:
        print(i_lvl3)
        item_choice = input('Choose loot: ')
        if item_choice != '+1 sword' and item_choice != '+1 helm' and item_choice != '+1 boots' and item_choice != '+1 chest' and item_choice != '+1 shield' and item_choice != 'Healing Potion' and item_choice != '+2 sword' and item_choice != '+2 helm' and item_choice != '+2 boots' and item_choice != '+2 chest' and item_choice != '+2 shield' and item_choice != '+3 sword' and item_choice != '+3 helm' and item_choice != '+3 boots' and item_choice != '+3 chest' and item_choice != '+3 shield' and item_choice != '+4 sword' and item_choice != '+4 helm' and item_choice != '+4 boots' and item_choice != '+4 chest' and item_choice != '+4 shield':
            item_choice = input('Choose loot: ')
        char_inv[item_choice] = i_lvl3[item_choice]
        print(f'Your inventory contains {char_inv}')
    elif char['lvl'] == 10 or char['lvl'] == 11 or char['lvl'] == 12:
        print(i_lvl4)
        item_choice = input('Choose loot: ')
        if item_choice != '+1 sword' and item_choice != '+1 helm' and item_choice != '+1 boots' and item_choice != '+1 chest' and item_choice != '+1 shield' and item_choice != 'Healing Potion' and item_choice != '+2 sword' and item_choice != '+2 helm' and item_choice != '+2 boots' and item_choice != '+2 chest' and item_choice != '+2 shield' and item_choice != '+3 sword' and item_choice != '+3 helm' and item_choice != '+3 boots' and item_choice != '+3 chest' and item_choice != '+3 shield' and item_choice != '+4 sword' and item_choice != '+4 helm' and item_choice != '+4 boots' and item_choice != '+4 chest' and item_choice != '+4 shield':
            item_choice = input('Choose loot: ')
        char_inv[item_choice] = i_lvl4[item_choice]
        print(f'Your inventory contains {char_inv}')

#function for equiping items
def equip():
    print(f'You have {char_inv} in your inventory and are wearing {equipped_wep} {equipped_armor}')
    to_equip = input("Enter an item to equip: ")
    if to_equip != '+1 sword' and  to_equip != '+1 helm' and to_equip != '+1 boots' and to_equip != '+1 chest' and to_equip != '+1 shield' and to_equip != 'Healing Potion' and to_equip != '+2 sword' and  to_equip != '+2 helm' and to_equip != '+2 boots' and to_equip != '+2 chest' and to_equip != '+2 shield' and to_equip != '+3 sword' and  to_equip != '+3 helm' and to_equip != '+3 boots' and to_equip != '+3 chest' and to_equip != '+3 shield' and to_equip != '+4 sword' and  to_equip != '+4 helm' and to_equip != '+4 boots' and to_equip != '+4 chest' and to_equip != '+4 shield':
        to_equip = input("Enter an item to equip: ")
    if to_equip in char_inv.keys() and 'sword' in to_equip:
        equipped_wep[to_equip] = char_inv[to_equip]
        char_inv.pop(to_equip)
    else:
        equipped_armor[to_equip] = char_inv[to_equip]
        char_inv.pop(to_equip)
    print(f'You have {char_inv} in your inventory and are wearing {equipped_wep} {equipped_armor}')
    #5 is base character attack
    #0 is base character defense
    char['atk'] = 5
    char['defense'] = 0
    for value in equipped_wep.values():
        char['atk'] += value
    for value in equipped_armor.values():
        char['defense'] += value

#consumes healing potion and restors 20 hp
def use_potion():
    if 'Healing Potion' in char_inv.keys():
        char['hp'] = char['hp']+20
        char_inv.pop('Healing Potion')

#checks character HP and exits the game if less than 1
def game_over():
    if char['hp'] < 1:
        print(f'{char["name"]} has been slain!  Better luck next time!')
        exit()

def inventory():
    print(char_inv)

#combat function: entering the dungeon starts combat
def combat():
    if char['lvl'] == 1 or char['lvl'] == 2 or char['lvl'] == 3:
        rand_monster = randint(0, len(m_lvl1) - 1)
        monster = m_lvl1[rand_monster]
        m_lvl1.pop(rand_monster)
    elif char['lvl'] == 4 or char['lvl'] == 5 or char['lvl'] == 6:
        rand_monster = randint(0, len(m_lvl2) - 1)
        monster = m_lvl2[rand_monster]
        m_lvl2.pop(rand_monster)
    elif char['lvl'] == 7 or char['lvl'] == 8 or char['lvl'] == 9:
        rand_monster = randint(0, len(m_lvl3) - 1)
        monster = m_lvl3[rand_monster]
        m_lvl3.pop(rand_monster)
    elif char['lvl'] == 10 or char['lvl'] == 11 or char['lvl'] == 12:
        rand_monster = randint(0, len(m_lvl4) - 1)
        monster = m_lvl4[rand_monster]
        m_lvl4.pop(rand_monster)
    print(f'You kick in the door and see a {monster["name"]}. Prepare to fight!')
    while monster['hp'] > 0:
        combat_choice = input('What would you like to do? Available actions are: Attack, Block, Parry: ')
        # input validation
        if combat_choice != 'Attack' and combat_choice != 'Block' and combat_choice != 'Parry':
            combat_choice = input('What would you like to do? Available actions are: Attack, Block, Parry: ')
        print(combat_choice)
        if combat_choice == 'Attack' and rand_action() == 'Attack':
            char['hp'] = char['hp'] - (monster['atk'] - char['defense'])
            monster['hp'] = monster['hp'] - (char['atk'] - monster['defense'])
            print(f'{monster["name"]} and {char["name"]} both attack')
            print(f'{monster["name"]} loses {char["atk"]} HP')
            print(f'{char["name"]} loses {monster["atk"]} HP')
            print(f'{char["name"]} HP is {char["hp"]}')
            print(f'{monster["name"]} HP is {monster["hp"]}')
            game_over()
        elif combat_choice == 'Attack' and rand_action() == 'Parry':
            char['hp'] = char['hp'] - int((monster['atk']*2) - char['defense'])
            print(f'{monster["name"]} parries the attack and deals 2x damage back!')
            print(f'{char["name"]} loses {int((monster["atk"]*2))} HP')
            print(f'{char["name"]} HP is {char["hp"]}')
            print(f'{monster["name"]} HP is {monster["hp"]}')
        elif combat_choice == 'Attack' and rand_action() == 'Block':
            monster['hp'] = monster['hp'] - int((char['atk']/2) - monster['defense'])
            print(f'{char["name"]} attacks and {monster["name"]} blocks dealing half damage')
            print(f'{monster["name"]} loses {int((char["atk"]/2))} HP')
            print(f'{char["name"]} HP is {char["hp"]}')
            print(f'{monster["name"]} HP is {monster["hp"]}')
        elif combat_choice == 'Parry' and rand_action() == 'Attack':
            monster['hp'] = monster['hp'] - int((char['atk']*2) - monster['defense'])
            print(f'{char["name"]} parries the attack and deals 2x damage back!')
            print(f'{monster["name"]} loses {int(char["atk"]*2)} HP')
            print(f'{char["name"]} HP is {char["hp"]}')
            print(f'{monster["name"]} HP is {monster["hp"]}')
        elif combat_choice == 'Parry' and rand_action() == 'Block':
            char['hp'] = char['hp'] - int((monster['atk']*2) - char['defense'])
            print(f'{char["name"]} parries and {monster["name"]} slams {char["name"]} for double damage!')
            print(f'{char["name"]} loses {int((monster["atk"]*2))} HP')
            print(f'{char["name"]} HP is {char["hp"]}')
            print(f'{monster["name"]} HP is {monster["hp"]}')
        elif combat_choice == 'Parry' and rand_action() == 'Parry':
            print(f'{char["name"]} and {monster["name"]} are both cowards and do nothing...')
        elif combat_choice == 'Block' and rand_action() == 'Block':
            print(f'{char["name"]} and {monster["name"]} are both cowards and do nothing...')
        elif combat_choice == 'Block' and rand_action() == 'Attack':
            char['hp'] = char['hp'] - int((monster['atk']/2) - char['defense'])
            print(f'{monster["name"]} attacks and {char["name"]} blocks dealing half damage')
            print(f'{char["name"]} loses {int((monster["atk"]/2))} HP')
            print(f'{char["name"]} HP is {char["hp"]}')
            print(f'{monster["name"]} HP is {monster["hp"]}')
        elif combat_choice == 'Block' and rand_action() == 'Parry':
            monster['hp'] = monster['hp'] - int((char['atk']*2) - monster['defense'])
            print(f'{monster["name"]} parries and {char["name"]} slams {monster["name"]} for double damage!')
            print(f'{monster["name"]} loses {int((char["atk"]*2))} HP')
            print(f'{char["name"]} HP is {char["hp"]}')
            print(f'{monster["name"]} HP is {monster["hp"]}')

    char['lvl'] += 1
    if char['lvl'] == 13:
        print(f'{char["name"]} has bravely bested the dungeon!  Congratulations!  Time well spent I am sure.')
        exit()
    print(f'{char["name"]} slayed the {monster["name"]}. {char["name"]} advances to level {char["lvl"]}  Claim your reward!')
    loot()
    enter_command()

#while not in combat the player can enter combat, view inventory, equip items, or use a potion
def enter_command():
    command = ''
    while command != 'Kick in Door':
        command = input('What would you like to do? Available actions are: Inventory, Equip, Use Potion, Stats, Kick in Door: ')
        #input validation
        if command != 'Inventory' and command != 'Equip' and command != 'Use Potion' and command != 'Stats' and command != 'Kick in Door':
            command = input('What would you like to do? Available actions are: Inventory, Equip, Use Potion, Stats, Kick in Door: ')
        if command == 'Inventory':
            print(char_inv)
        elif command == 'Equip':
            equip()
        elif command == 'Use Potion':
            use_potion()
        elif command == 'Stats':
            print(char)
    combat()

if __name__ == "__main__":
    print("Welcome to the dungeon please enter a command,")
    enter_command()
