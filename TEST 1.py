import sqlite3
import Team_module
import UNIT_CLASSES


class Shop():
    def __init__(self, init_player_team = None, init_gold = 0):
        self.player_team = init_player_team
        self.gold = init_gold

        self.gold = 1000
        self.player_team = Team_module.Team_class()
        self.player_team.create_start_team_for_player("Ivan")

    def unit_shop(self):
        db = sqlite3.connect("Db_shop.db")
        cursor = db.cursor()
        cursor.execute("SELECT unit_name, unit_price FROM units")
        data = cursor.fetchall()
        db.close()

        for x in range (len(data)):
            print(f"{x}. {data[x][0]} - {data[x][1]} gold")
        print(f"{len(data)}. Show your team with all unit's items to analise.")
        print(f"{len(data)+1}. Return to previous stage.")

        while True:
            answer = input("Input number here ---> ")
            try:
                answer = int(answer)
            except:
                continue
            if answer < 0 or answer > len(data)+1:
                continue
            if answer == len(data):
                self.player_team.team_info_shop2()
                continue
            break

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
            if unit.name.lower() == u_choice_name:
                if self.gold < u_choice_price:
                    print("You don't have enough money to buy this unit")
                    self.unit_shop()
                else:
                    self.player_team.alive_team.append(unit)
                    print(f"\n   You have bought {u_choice_name} for {u_choice_price} gold")
                    self.gold -= u_choice_price
                    self.main()
                break















    def armor_shop(self):
        pass

    def weapon_shop(self):
        pass

    def ability_shop(self):
        pass

    def item_categories(self):
        print(f'''
    ----------------
    ITEM CATEGORIES
    ----------------
    Gold = {self.gold}

        0. Buy unit.
        1. Buy armor.
        2. Buy weapon.
        3. Buy ability.
        4. Show your team with all unit's items to analize.
        5. Return to previous stage.''')

        while True:
            answer = input("Input number here ---> ")
            try:
                answer = int(answer)
            except:
                continue
            if answer < 0 or answer > 5:
                continue

            if answer == 4:
                self.player_team.team_info_shop2()
                continue

            if answer == 0:
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
        ------------------------------------------
                WELCOME TO THE GAME SHOP
        ------------------------------------------
        Gold = {self.gold}

    Please, choose, what would you like to do in the shop:
        0. See all item categories to buy.
        1. See your team with all unit's items to analise.
        2. Exit from the shop.''')

        while True:
            answer = input("Input number here ---> ")
            try:
                answer = int(answer)
            except:
                continue
            if answer < 0 or answer > 2:
                continue


            if answer == 1:
                self.player_team.team_info_shop2()
                continue
            break


        if answer == 0:
            self.item_categories()
        elif answer == 2:
            print("\n   See you next time, bye-bye!")
            return


shop = Shop()
shop.main()


