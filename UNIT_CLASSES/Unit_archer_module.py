from .Unit_module import Unit_class


class Archer_class(Unit_class):
    # Основні характеристики
    name = "Archer"

    # Спеціальні таланти
    ability = "Triple hit to 1 enemy unit"



    def use_ability(self, enemy, self_team, enemy_team):
        if self.check_magic_shield(enemy):
            enemy.health_in_arena = enemy.health_in_arena + enemy.defence_power() - 3 * self.hit_power()
            print(f" \n***{self.name} hits {enemy.name} by {3 * self.hit_power()} points***")


