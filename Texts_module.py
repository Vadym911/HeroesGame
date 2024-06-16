import UNIT_CLASSES

def game_welcome_board():
    return '''
    ----------------------------------------------------------------------------------------------------------------
    
                                    **********   GAME OF HEROES   **********
    
                                        -- The game by Vadym Ryzhkov --
    
    ----------------------------------------------------------------------------------------------------------------
    '''

def get_player_name():
    return "Hello Hero! What is your name? --->"

def welcome_young_hero(player_name, player_gold, all_arenas):
    return f'''
        Welcome, my young hero {player_name}!
        Here is some money({player_gold}), you need to create your own squad and fight in {all_arenas} arenas.
        Let's play the Game!
        '''

def wow_you_have_a_squad(player_team):
    text = '''
        Wow! You have a squad from 4 heroes!
        '''
    for unit in player_team:
        text += "\n" + unit.unit_info()

    text += "\n" + "-"*50

    return text

def arena_final_positive(arena_counter, arena_revard, player_gold):
    return f'''\n\n
    You get {arena_revard} gold for succesful battle in Arena {arena_counter}
    Now you have {player_gold} gold!
    Are you ready to prepare for the next Arena?
    let's go shopping to buy new items and units!
    \n\n
    Press ENTER to continue -->
    '''

def arena_final_negative():
    return '''
        You loose in this arena. You should buy a new squad.
            
            Are you ready to prepare for this Arena one more time?
            Let's go shopping to buy new units and items!
            
        Press ENTER to continue -->
        '''

def game_final_dashboard_winner(all_arenas):
    return f'''
        -------------------------------------------------------
                    ******** GAME OVER ******** 
                    You win the game
        -------------------------------------------------------
                You have won in all {all_arenas} Arenas
        '''

def game_final_dashboard_looser():
    return'''
        -------------------------------------------------------
                    ******** GAME OVER ******** 
                    You loose the game
        -------------------------------------------------------
                You have no money to buy full squad
            '''


def display_arena_board(counter_arena, player_team, comp_team):
    input("                 --- press ENTER to continue ---")
    return f'''
            -------------------------------------------------------
                ******** ARENA #{counter_arena} BOARD ********
            -------------------------------------------------------
                        Welcome to the Arena!
            {player_team.name}             VS           {comp_team.name}            

        '''

def choose_unit(fight_counter):
    input("                 --- press ENTER to continue ---")
    return f'''
    -------------------------------------------------------
          CHOOSE UNITS TO THE FIGHT #{fight_counter}!
    -------------------------------------------------------
    '''

def display_fight_board(fight_counter, attacker, defender):
    return f'''
            ---------------------------------
            ******** FIGHT #{fight_counter} BOARD ********
            ---------------------------------
            Attacker     VS          Defender
            {attacker.name}                   {defender.name}

            Attacker - {attacker.unit_info()}
            Defender - {defender.unit_info()}

            LET'S THE FIGHT BEGIN
            '''
def dead_or_alife(unit):
    if unit.status == True:
        return "Alive"
    else:
        return "Dead"

def fight_result_board(player_unit, comp_unit):
    return f'''

        {player_unit.name} status - {dead_or_alife(player_unit)}, health: {player_unit.health_in_arena}
        {comp_unit.name} status - {dead_or_alife(comp_unit)}, health: {comp_unit.health_in_arena}

        -------------------------------
        '''