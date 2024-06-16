import random
import UNIT_CLASSES

class Team_class():
    alive_team = []
    alive_team_in_arena = []
    dead_team = []
    dead_team_in_arena = []
    name = ""
    def create_start_team_for_player(self, player_name):
        self.name = f"{player_name}'s team"
        self.alive_team = [UNIT_CLASSES.Knight_class(),
                    UNIT_CLASSES.Archer_class(),
                    UNIT_CLASSES.Witch_class(),
                    UNIT_CLASSES.Wizard_class()]


    def create_comp_team_for_arena(self):
        name_list = ["Monster's squad",
                     "Crocodiles",
                     "Superman",
                     "WoW warious",
                     "BlaBla squad",
                     "Pink ponys"]
        self.name = random.choice(name_list)

        list = [UNIT_CLASSES.Knight_class(),
                UNIT_CLASSES.Archer_class(),
                UNIT_CLASSES.Witch_class(),
                UNIT_CLASSES.Wizard_class(),
                UNIT_CLASSES.Healer_class(),
                UNIT_CLASSES.Barbarian_class()]
        for i in range(5):
            rand_index = random.randint(0,len(list)-1)
            herro_to_add = list.pop(rand_index)
            self.alive_team_in_arena.append(herro_to_add)

    def team_info_shop(self):
        x = 0
        for unit in self.alive_team:
            print(f"{x}. {unit.unit_info_shop()}")
            x += 1


    def team_info(self):
        text = ''''''
        num = 0

        for unit in self.alive_team_in_arena:
            text += "\n" + str(num) + ") " + unit.unit_info()
            num += 1

        return text

    def check_alive(self):
        for unit in self.alive_team_in_arena:
            if unit.status == True:
                return True
            return False

    def comp_choose_unit(self):
        comp_unit = None
        while True:
            unit = random.choice(self.alive_team_in_arena)
            if unit.status == False:
                continue
            return unit

    def player_choose_unit(self):
        self.team_info()
        while True:
            answer = input("Choose your unit to attack ---> ")
            if len(answer) == 0:
                continue

            try:
                answer = int(answer)
            except:
                continue

            try:
                unit = self.alive_team_in_arena[answer]
            except:
                continue

            if unit.status == False:
                continue

            return unit