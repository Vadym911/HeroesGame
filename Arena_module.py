import Texts_module
import Team_module
import Fight_module
class Arena_class():
    def __init__(self, init_player_team, init_arena_counter):
        self.player_team = init_player_team
        self.player_team.alive_team_in_arena = self.player_team.alive_team
        self.fight_counter = 0
        self.arena_counter = init_arena_counter

    def create_comp_team(self):
        self.comp_team = Team_module.Team_class()
        self.comp_team.create_comp_team_for_arena()


    def display_arena_board(self):
        print(Texts_module.display_arena_board(self.arena_counter, self.player_team, self.comp_team))
        print(f"\n {self.player_team.name}'s team")
        print(self.player_team.team_info())

        print(f"\n {self.comp_team.name}'s team")
        print(self.comp_team.team_info())

    def fight(self):
        for team in [self.player_team, self.comp_team]:
            for unit in team.alive_team_in_arena:
                unit.health_in_arena = unit.health

        while self.player_team.check_alive() and self.comp_team.check_alive():
            self.fight_counter += 1
            print(Texts_module.choose_unit(self.fight_counter))
            if self.fight_counter%2 != 0:
                print("Player choose self unit")
                player_unit = self.player_team.player_choose_unit()
                print("Player choose enemy unit")
                comp_unit = self.comp_team.player_choose_unit()
            else:
                print("Computer choose his unit")
                comp_unit = self.comp_team.comp_choose_unit()
                print("Computer choose player unit")
                player_unit = self.player_team.comp_choose_unit()

            fight = Fight_module.Fight_class(player_unit, comp_unit, self.fight_counter, self.player_team, self.comp_team)
            fight.fight()


    def arena_results(self):
        result = [[], []]
        return result
