from .Unit_module import Unit_class


class Barbarian_class(Unit_class):
    # Основні характеристики
    name = "Barbarian"

    # Спеціальні таланти
    ability = "Stun all enemy units for the next 1 move"

    def use_ability(self, enemy, self_team, enemy_team):
        for unit in enemy_team.alive_team_in_arena:
            if self.check_magic_shield(enemy):
                unit.stunned = True
                print(f"    {self.name} stune {unit.name} by 1 move")