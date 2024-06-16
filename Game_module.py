import UNIT_CLASSES
import Texts_module
import Arena_module
from Team_module import Team_class
import Shop_module
import sqlite3
class Game_class():
    player_name = ""
    player_team_alive = []
    player_team_dead = []
    player_gold = 1000
    win_status = None
    all_arenas = 5
    arena_counter = 0

    def game_running(self):
        # Перевірка, чи не закінчились арени
        if self.arena_counter < 5:
            return True
        # Перевірка, чи не повна команда і чи вистачає грошей на її поповнення
        if len(self.player_team.alive_team) < 5:
            budget_needed = 0
            unit_needed = 5 - len(self.player_team.alive_team)
            db = sqlite3.connect("Db_shop.db")
            cursor = db.cursor()
            cursor.execute("SELECT unit_price FROM units")
            data = cursor.fetchall()
            all_prices = []
            for item in data:
                all_prices.append(item[0])
            min_price = min(all_prices)
            budget_needed = unit_needed * min_price
            if self.player_gold > budget_needed:
                return True
        return False


    def play(self):

        # Вітальний екран
        print(Texts_module.game_welcome_board())

        # Знайомство
        self.player_name = input(Texts_module.get_player_name())
        print(Texts_module.welcome_young_hero(self.player_name, self.player_gold, self.all_arenas))

        # Створення початкової команди
        self.player_team = Team_class()
        self.player_team.create_start_team_for_player(self.player_name)

        print(Texts_module.wow_you_have_a_squad(self.player_team.alive_team))

        # Основний цикл гри
        while self.game_running():
            # Ознайомлення з магазином
            shop = Shop_module.Shop(self.player_team, self.player_gold)
            shop.main()

            # створення арени, поміщення команди гравця в арену
            arena = Arena_module.Arena_class(self.player_team, self.arena_counter)
            arena.create_comp_team()
            arena.display_arena_board()
            arena.fight()

            # аналіз результатів
            arena_results = arena.arena_results()
            self.player_team.alive_team = arena_results[0]
            self.player_team.dead_team.append(arena_results[1])

            #revards за закінчення арени
            if len(self.player_team.alive_team) > 0:
                arena_revard = 1000
                self.player_gold += arena_revard
                print(Texts_module.arena_final_positive(self.arena_counter, arena_revard, self.player_gold))
                input()
                self.arena_counter += 1
            elif self.game_running():
                print(Texts_module.arena_final_negative())
                input()
            else:
                self.win_status = False
                break

        # Аналітика закінчення гри, фінальний екран
        if self.win_status == True:
            print(Texts_module.game_final_dashboard_winner(self.all_arenas))
        else:
            print(Texts_module.game_final_dashboard_looser())


        u_inp = ""
        while u_inp[0].lower() not in ["y", "n"]:
            u_inp = input("\n Do you wanna play one more time (yes/no) --->")
            if u_inp[0].lower() not in ["y", "n"]:
                print("Please, write correct answer.")

        if u_inp[0].lower() == "y":
            self.play()
        else:
            print("Thanks for playing. Goodbye")

game = Game_class()
game.play()