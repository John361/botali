from functions import *

# Global variables
class_info_file_name = "classes_info.json"
game_info_file_name = "game_info.json"


# Welcome message
pretty_print("BOTALI - I plaisante pas ek :poop: !", "blue")


# Load file and classes
all_classes = get_class_list(class_info_file_name)


# Ask user for his class
player_class = ask_for_choice("Choose a player class:", all_classes)
user_powers_list = get_class_powers(class_info_file_name, player_class)
user_power_names = list_class_power_names(user_powers_list)


# Ask user for his enemy class
bot_class = ask_for_choice("Choose an bot class:", all_classes)
bot_powers_list = get_class_powers(class_info_file_name, bot_class)
bot_power_names = list_class_power_names(bot_powers_list)


# Initialize game
game_info = get_game_info(game_info_file_name)


# Fight begin message
pretty_print("-----", "blue")
pretty_print("--- Player VS Bot --- ", "blue")
pretty_print(f"--- {player_class.capitalize()} VS {bot_class.capitalize()} ---", "blue")
pretty_print("-----\n", "blue")


# Start game logic
is_game_finished = False
player_life = int(game_info["player"]["life"])
bot_life = int(game_info["bot"]["life"])


while not is_game_finished:
    pretty_print(f"Player life: {player_life}", "blue")
    pretty_print(f"Bot life: {bot_life}\n", "blue")

    user_attack_choice = ask_for_choice("Choose your attack:", user_power_names)
    user_damage = get_damage_for_power_name(user_powers_list, user_attack_choice)
    bot_life = bot_life - user_damage

    if bot_life <= 0:
        bot_life = 0
        pretty_print(f"Bot life: {bot_life}", "green")
        pretty_print("You win!", "green")
        is_game_finished = True
        break

    pretty_print(f"You did {user_damage} damages to the bot and now his life is {bot_life}", "green")

    bot_attack_choice = ask_for_choice("Choose bot attack:", bot_power_names)
    bot_damage = get_damage_for_power_name(bot_powers_list, bot_attack_choice)
    player_life = player_life - bot_damage

    if player_life <= 0:
        player_life = 0
        pretty_print(f"Player life: {player_life}", "red")
        pretty_print("You lost!", "red")
        is_game_finished = True
        break

    pretty_print(f"Bot did {bot_damage} damages to you and now your life is {player_life}", "red")
