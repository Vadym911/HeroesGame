# абілка - завдає удару всім ворогам одночасно на 50% потужності

from .Unit_module import Unit_class


class Knight_class(Unit_class):
    # Основні характеристики
    name = "Knight"

    # Спеціальні таланти
    ability_value = 0.5
    ability = f"Hit all enemy units by {int(ability_value*100)}% of attack"

    def use_ability(self, enemy, self_team, enemy_team):
        for unit in enemy_team.alive_team_in_arena:
            if self.check_magic_shield(enemy):
                if unit.defence_power() < self.ability_value * self.hit_power():
                    unit.health_in_arena = unit.health_in_arena + unit.defence_power() - self.ability_value * self.hit_power()
                    print(f"    {self.name} hits {unit.name} by {self.ability_value * self.hit_power()} points")
