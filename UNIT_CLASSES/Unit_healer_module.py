from .Unit_module import Unit_class


class Healer_class(Unit_class):
    # Основні характеристики
    name = "Healer"

    # Спеціальні таланти
    ability_value = 50
    ability = f"Heal all teammates by {ability_value}hp"

    def use_ability(self, enemy,
                    self_team,
                    enemy_team):
        for unit in self_team.alive_team_in_arena:
            unit.health_in_arena += self.ability_value
            if unit.health_in_arena > unit.health:
                unit.health_in_arena = unit.health
            print(f"        {self.name} heels {unit.name} by {self.ability_value} points")

