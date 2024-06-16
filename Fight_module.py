
import Texts_module

class Fight_class():
    def __init__(self, init_player_unit, init_comp_unit, init_fight_counter, init_player_team, init_comp_team):
        self.player_unit = init_player_unit
        self.comp_unit = init_comp_unit
        self.fight_counter = init_fight_counter
        self.player_team = init_player_team
        self.comp_team = init_comp_team


    def use_ability(self):
        pass

    def hit(self, attacker, defender):
        attacker_hit_power = attacker.hit_power()
        attacker_defence_power = attacker.defence_power()

        defender_hit_power = defender.hit_power()
        defender_defence_power = defender.defence_power()


        if defender.magic_shield == False:
            if attacker_hit_power > defender_defence_power:
                defender.health_in_arena = defender.health_in_arena + defender_defence_power - attacker_hit_power
            print(f"{attacker.name} hit {defender.name} by {attacker.hit_power()} points")

        else:
            print(f"    {defender.name} has magic shield and avoid any attack for this fight!")
            defender.magic_shield = False

        if defender_hit_power > attacker_defence_power:
            attacker.health_in_arena = attacker.health_in_arena + attacker_defence_power - defender_hit_power


    def fight(self):
        if self.fight_counter % 2 != 0 and not self.player_unit.is_stunned():
            #хід гравця
            print(Texts_module.display_fight_board(self.fight_counter,
                                                   attacker = self.player_unit,
                                                   defender = self.comp_unit))

            if self.player_unit.player_check_ability():
                self.player_unit.use_ability(enemy = self.comp_unit,
                                             self_team = self.player_team,
                                             enemy_team = self.comp_team)
            else:
                self.hit(attacker = self.player_unit,
                         defender = self.comp_unit)
        elif self.fight_counter % 2 == 0 and not self.comp_unit.is_stunned():
            # хід компа
            print(Texts_module.display_fight_board(self.fight_counter,
                                                   attacker = self.comp_unit,
                                                   defender = self.player_unit))

            if self.comp_unit.comp_check_ability():
                self.comp_unit.use_ability(enemy = self.player_unit,
                                             self_team = self.comp_team,
                                             enemy_team = self.player_team)
            else:
                print("------>>>> 1")
                self.hit(attacker = self.comp_unit,
                         defender = self.player_unit)

        for unit in [self.player_unit, self.comp_unit]:
            if unit.health_in_arena < 0:
                unit.health_in_arena = 0

        print(Texts_module.fight_result_board(self.player_unit, self.comp_unit))

        print("\n---- POISON BOARD -----")
        for team in [self.player_team, self.comp_team]:
            print(f"\n {team.name}")
            for unit in team.alive_team_in_arena:
                if unit.poisoned_moves > 0:
                    unit.health_in_arena -= unit.poisoned_value
                    unit.poisoned_moves -= 1
                    print(f"{unit.name} is poisoned by {unit.poisoned_value} hp")
