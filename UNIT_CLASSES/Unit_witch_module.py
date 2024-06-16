# абілка - завдає удару всім ворогам одночасно на 50% потужності

from .Unit_module import Unit_class


class Witch_class(Unit_class):
    # Основні характеристики
    name = "Witch"

    # Спеціальні таланти
    ability_value = 10
    default_poison_moves = 3
    ability = f"Poison 1 enemy unit by {ability_value} for 3 next moves"



    def use_ability(self, enemy, self_team, enemy_team):
        for unit in enemy_team.alive_team_in_arena:
            if self.check_magic_shield(enemy):
                unit.poisoned_moves = 3
                unit.poisoned_value = self.ability_value
                print(f"    {self.name} poison {unit.name} for {self.default_poison_moves} move")