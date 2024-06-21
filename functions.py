from json import load as j_load, dump as j_dump

from rich.console import Console
from rich.prompt import Prompt


def pretty_print(message, color):
    """
    Print message to console using Console
    Possible colors are: green, yellow, red
    :param message:
    :param color:
    :return:
    """
    console = Console()
    console.print(message, style=color)


def get_class_list(file):
    """
    Get all classes from a json file
    :param file:
    :return:
    """
    with open(file, "r") as f:
        content = j_load(f)
        return content["classes"]


def get_class_powers(file, cls):
    """
    Get all powers for a specific class from a json file
    :param file:
    :param cls:
    :return:
    """
    with open(file, "r") as f:
        content = j_load(f)
        return content["powers"][cls]


def list_class_power_names(powers):
    """
    List all power names from the given powers list
    :param powers:
    :return:
    """
    names = []

    for power in powers:
        names.append(power["name"])

    return names


def get_damage_for_power_name(powers, name):
    """
    Get damage for a specific power using name
    :param powers:
    :param name:
    :return:
    """
    for power in powers:
        if power["name"] == name:
            return int(power["damage"])


def get_game_info(file):
    """
    Get all game info from a file
    :param file:
    :return:
    """
    with open(file, "r") as f:
        content = j_load(f)
        return content


def set_game_info(file, info):
    """
    Write all info about the game to the given file
    :param file:
    :param info:
    :return:
    """
    with open(file, "w") as f:
        j_dump(f, info)


def ask_for_choice(message, choices):
    """
    Ask user to choose an option
    :param message:
    :param choices:
    :return:
    """
    result = Prompt.ask(message, choices=choices)
    return str(result)
