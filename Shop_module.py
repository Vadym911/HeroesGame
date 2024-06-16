import sqlite3
import Team_module
import UNIT_CLASSES
from HEROES_GAME import Armor_module
from HEROES_GAME import Weapons_module

class Shop():
    def __init__(self, init_player_team = None, init_gold = 0):
        self.player_team = init_player_team
        self.gold = init_gold

    def user_shosing_number(self, number):
        while True:
            answer = input("Input number here ---> ")

            try:
                answer = int(answer)
            except:
                continue

            if answer < 0 or answer > 2:
                continue


            if answer == 0:
                self.item_categories()
                break
            elif answer == 1:
                self.player_team.team_info_shop()

            elif answer == 2:
                print("\nSee you next time, bye-bye!")
                return

    def get_info_from_db(self, text):
        db = sqlite3.connect("Db_shop.db")
        cursor = db.cursor()
        cursor.execute(text)
        data = cursor.fetchall()
        db.close()
        return data

    def get_answer_from_user(self, data):
        while True:
            answer = input("Input number here ---> ")

            try:
                answer = int(answer)
            except:
                continue
            if answer < 0 or answer > len(data)+1:
                continue
            if answer == len(data):
                self.player_team.team_info_shop()
                continue
            return answer

    def unit_shop(self):
        print(f'''
        ----------------
            BUY UNITS
        ----------------
        Gold = {self.gold}''')

        data = self.get_info_from_db("SELECT unit_name, unit_price FROM units")

        for x in range(len(data)):
            print(f"{x}. {data[x][0]} - {data[x][1]} gold")
        print(f"{len(data)}. Show your team with all unit's items to analize")
        print(f"{len(data)+1}. Return to previous stage")

        answer = self.get_answer_from_user(data)

        if answer == len(data)+1:
            self.item_categories()
            return

        u_choice_name = data[answer][0]
        u_choice_price = data[answer][1]

        library = [UNIT_CLASSES.Archer_class(),
                    UNIT_CLASSES.Barbarian_class(),
                    UNIT_CLASSES.Healer_class(),
                    UNIT_CLASSES.Knight_class(),
                    UNIT_CLASSES.Witch_class(),
                    UNIT_CLASSES.Wizard_class()]
        for unit in library:
            if unit.name == u_choice_name:
                if self.gold < u_choice_price:
                    print("YOUR DON'T HAVE MONEY")
                    self.unit_shop()
                else:
                    self.player_team.alive_team.append(unit)
                    print(f"\n   You have bought {u_choice_name} for {u_choice_price} gold")
                    self.gold -= u_choice_price
                    self.main()
                break

    def armor_shop(self):
        print(f'''
            ----------------
                BUY ARMOR
            ----------------
            Gold = {self.gold}''')

        armor_categories = self.get_info_from_db("SELECT armor_type_name FROM armor_types")
        for x in range(len(armor_categories)):
            print(f"    {x}. {armor_categories[x][0]}")
        print(f"    {len(armor_categories)}. Show your team with all unit's items to analize")
        print(f"    {len(armor_categories) + 1}. Return to previous stage")

        answer = self.get_answer_from_user(armor_categories)
        if answer == len(armor_categories) + 1:
            self.item_categories()
            return

        armor_type_name = armor_categories[answer][0]
        armor_type_id = self.get_info_from_db(f"SELECT armor_type_id FROM armor_types WHERE armor_type_name = '{armor_type_name}' ")
        armor_type_id = armor_type_id[0][0]

        data = self.get_info_from_db(f"SELECT armor_name, value, price FROM armor WHERE armor_type_id = '{armor_type_id}' ")

        for x in range(len(data)):
            print(f"    {x}. {data[x][0]}({data[x][1]} power) - {data[x][2]} gold")
        print(f"    {len(data)}. Show your team with all unit's items to analize")
        print(f"    {len(data) + 1}. Return to previous stage")

        answer = self.get_answer_from_user(data)


        armor_choice_name = data[answer][0]
        armor_choice_value = data[answer][1]
        armor_choice_price = data[answer][2]

        if armor_choice_price > self.gold:
            print(" You have no enough gold!")
            self.armor_shop()
            return

        print("\n   Which unit will get this armor?")
        self.player_team.team_info_shop()

        answer = self.get_answer_from_user(self.player_team.alive_team)
        unit = self.player_team.alive_team[answer]

        if armor_type_name == "helmet":
            unit.helmet = Armor_module.Helmet(armor_choice_name, armor_choice_value)
        elif armor_type_name == "bodyarmor":
            unit.bodyarmor = Armor_module.Bodyarmor(armor_choice_name, armor_choice_value)
        elif armor_type_name == "boots":
            unit.boots = Armor_module.Boots(armor_choice_name, armor_choice_value)
        elif armor_type_name == "shield":
            unit.shield = Armor_module.Shield(armor_choice_name, armor_choice_value)

        self.gold -= armor_choice_price

        print(f"You have bought {armor_choice_name}({armor_choice_value} power) for {unit.name} for {armor_choice_price} gold!")
        self.main()
    def weapon_shop(self):
        print(f'''
    ----------------
       BUY WEAPON
    ----------------
    Gold = {self.gold}''')

        print("\n   Which unit will get this weapon?")
        self.player_team.team_info_shop()
        answer = self.get_answer_from_user(self.player_team.alive_team)
        unit = self.player_team.alive_team[answer]
        unit_id = self.get_info_from_db(f"SELECT unit_id FROM units WHERE unit_name = '{unit.name}' ")
        unit_id = unit_id[0][0]

        data = self.get_info_from_db(f"SELECT weapon_name, value, price FROM weapons WHERE usable_for_unit = '{unit_id}' ")

        for x in range(len(data)):
            print(f"    {x}. {data[x][0]}")
        print(f"    {len(data)}. Show your team with all unit's items to analize")
        print(f"    {len(data) + 1}. Return to previous stage")

        answer = self.get_answer_from_user(data)
        if answer == len(data) + 1:
            self.item_categories()
            return

        weapon_name = data[answer][0]
        weapon_value = data[answer][1]
        weapon_price = data[answer][2]

        if weapon_price > self.gold:
            print(" You have no enough gold!")
            self.armor_shop()
            return

        unit.weapon = Weapons_module.Weapon(weapon_name, weapon_value)

        self.gold -= weapon_price
        print(f"You have bought {weapon_name}({weapon_value} power) for {unit.name} for {weapon_price} gold!")
        print(unit.weapon.name)
        print(unit.weapon.name)

        self.main()






    def ability_shop(self):
        print(f'''
            ----------------
               BUY ABILITY
            ----------------
            Gold = {self.gold}''')

        print("\n   Which unit will get this ability?")
        self.player_team.team_info_shop()
        answer = self.get_answer_from_user(self.player_team.alive_team)
        unit = self.player_team.alive_team[answer]
        unit_id = self.get_info_from_db(f"SELECT unit_id FROM units WHERE unit_name = '{unit.name}' ")
        unit_id = unit_id[0][0]

        data = self.get_info_from_db(f"SELECT ability_name, value, price FROM abilities WHERE usable_for_unit = '{unit_id}' ")

        for x in range(len(data)):
            print(f"    {x}. {data[x][0]}")
        print(f"    {len(data)}. Show your team with all unit's items to analize")
        print(f"    {len(data) + 1}. Return to previous stage")

        answer = self.get_answer_from_user(data)
        if answer == len(data) + 1:
            self.item_categories()
            return

        ability_name = data[answer][0]
        ability_value = data[answer][1]
        ability_price = data[answer][2]

        if ability_price > self.gold:
            print(" You have no enough gold!")
            self.armor_shop()
            return
        unit.ability_item = ability_name
        unit.ability_value = ability_value

        unit.weapon = Weapons_module.Weapon(ability_name, ability_value)

        self.gold -= ability_price
        print(f"You have bought {ability_name}({ability_value} power) for {unit.name} for {ability_price} gold!")
        print(unit.ability_item)
        print(unit.ability_value)

        self.main()


    def item_categories(self):
        print(f'''
    ---------------
    ITEM CATEGORIES
    ---------------
    Gold = {self.gold}
    
        0. Buy unit.
        1. Buy armor.
        2. Buy weapon.
        3. Buy ability.
        4. Show your team with all unit's items to analize.
        5. Return to previous stage''')

        while True:
            answer = input("Input number here ---> ")
            try:
                answer = int(answer)
            except:
                continue
            if answer < 0 or answer > 5:
                continue

            if answer == 4:
                self.player_team.team_info_shop()
                continue



            if answer == 0:
                print(len(self.player_team.alive_team))
                if len(self.player_team.alive_team) < 5:
                    self.unit_shop()
                else:
                    print("You already have full team.")
                    continue

            if answer == 1:
                self.armor_shop()
            if answer == 2:
                self.weapon_shop()
            if answer == 3:
                self.ability_shop()
            if answer == 5:
                self.main()

            break
    def main(self):
        print(f'''
        -------------------------------------------------------
                        WELCOME TO THE GAME SHOP
        -------------------------------------------------------
        Gold = {self.gold}    

    Please, choose, what would you like to do in the shop:
        0. See all item categories to buy.
        1. See your team with all unit's items to analise.
        2. Exit from the shop.''')

        number = self.user_shosing_number(2)





