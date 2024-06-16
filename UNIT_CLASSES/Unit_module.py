from abc import ABC, abstractmethod
from HEROES_GAME import Weapons_module
from HEROES_GAME import Armor_module
class Unit_class(ABC):
    # Основні характеристики
    name = ""
    health = 100
    health_in_arena = None
    attack = 20
    defence = 5
    status = True

    weapon = Weapons_module.Weapon()

    # Блок спеціальних можливостей
    ability = ""
    ability_value = 0
    ability_cooldown = 3
    ability_item = ""

    helmet = Armor_module.Helmet()
    bodyarmor = Armor_module.Bodyarmor()
    boots = Armor_module.Boots()
    shield = Armor_module.Shield()


    #Блок ефектів
    magic_shield = False
    stunned = False
    poisoned_moves = 0
    poisoned_value = 0

    def unit_info_shop(self):
        armor = ""
        for item in [self.helmet, self.bodyarmor, self.boots, self.shield]:
            if item.value > 0:
                armor += f"{item.name}({item.value}), "

        weapon = ""

        if self.weapon.value > 0:
            weapon = f"{self.weapon.name}({self.weapon.value} power) "
        return f"{self.name}, armor - {armor}, weapon - {weapon}, ability - "

    def unit_info(self):
        return f"Name - {self.name}, Health - {self.health_in_arena}, Attack - {self.attack}, Defence - {self.defence}, Ability cooldown - {self.ability_cooldown}"

    def player_check_ability(self):
        if self.ability_cooldown == 0 and self.status == True:
            print(f"{self.name} is ready to use his Ability ({self.ability})")

            u_inp = ""
            while len(u_inp) == 0 or u_inp[0].lower() not in ["y", "n"]:
                u_inp = input("Do you want to use ability? (Y/N) ---> ")

            if u_inp[0].lower() == "y":
                self.ability_cooldown = 4
                return True
            else:
                self.ability_cooldown = 1
                return False
        else:
            self.ability_cooldown -= 1
            return False

    def comp_check_ability(self):
        if self.ability_cooldown == 0 and self.status == True:
            self.ability_cooldown = 4
            return True
        else:
            self.ability_cooldown -= 1
            return False

    def hit_power(self):
        hit_power = self.attack
        return hit_power

    def defence_power(self):
        defence_power = self.defence
        return defence_power

    @abstractmethod
    def use_ability(self, enemy,
                    self_team,
                    enemy_team):
        pass

    def check_magic_shield(self,enemy):
        if enemy.magic_shield == False:
            return True
        else:
            print(f"    {enemy.name} has magic shield and it protects from {self.name} ability")
            enemy.magic_shield = False

    def is_stunned(self):
        if self.stunned == True:
            self.stunned = False
            print(f"    {self.name} is stunned and cannot act")
            return True
        else:
            return False