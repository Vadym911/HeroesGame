from .Unit_module import Unit_class


class Wizard_class(Unit_class):
    # Основні характеристики
    name = "Wizard"

    # Спеціальні таланти
    ability = "Defend all teammates by magic shield for 1 move"


    def use_ability(self, enemy, self_team, enemy_team):
        for unit in self_team.alive_team_in_arena:
            unit.magic_shield = True
            print(f"        {self.name} gives magic shield for {unit.name}")