__author__ = 'Francisco Calderon and Grant Merrill'
import sys
from random import randint

# TODO update familiar to be whether the person is authorized to enter through that door

help_message = "Usage: hold_the_door.py [blank] | [--someone_behind boolean (required)] [--distance : distance between person ft (required)] \n" \
               "[--speed : speed at which the person is walking ftps (required)] \n" \
               "[--attractiveness : person's attractiveness 1-10 scale] [--authorized : boolean]\n" \
               "[--carrying : boolean] [--weather : 0-1 (0 = very bad, 1 = very nice)]"

doorHoldingData = [
    {"distance": 4.5, "speed": 5, "attractiveness": 0, "authorized": None, "carrying": True, "weather": .9},
    {"distance": 7.5, "speed": 4, "attractiveness": 1, "authorized": True, "carrying": False,
     "weather": .6},
    {"distance": 4, "speed": 4, "attractiveness": 1, "authorized": False, "carrying": False, "weather": 1},
    {"distance": 6.5, "speed": 4.2, "attractiveness": 6, "authorized": True, "carrying": True,
     "weather": .25},
    {"distance": 3, "speed": 4.5, "attractiveness": 7, "authorized": None, "carrying": False, "weather": .5},
    {"distance": 7, "speed": 3, "attractiveness": 1, "authorized": False, "carrying": True, "weather": .3},
    {"distance": 3, "speed": 4.5, "attractiveness": 3, "authorized": False, "carrying": False, "weather": .7},
    {"distance": 15, "speed": 5, "attractiveness": 8, "authorized": True, "carrying": True, "weather": .6},
    {"distance": 3, "speed": 4.5, "attractiveness": 2, "authorized": False, "carrying": True, "weather": .7},
    {"distance": 20, "speed": 3, "attractiveness": 10, "authorized": True, "carrying": False, "weather": 1},
    {"distance": 25, "speed": 3, "attractiveness": 1, "authorized": None, "carrying": False,
     "weather": .6},
    {"distance": 20, "speed": 3, "attractiveness": 5, "authorized": True, "carrying": True, "weather": .5}
]

# Mean time it takes to fully open a door
TIME_TO_OPEN_DOOR = 1

# The general area everyone is entitled to
GENERAL_GRAY_AREA = 2

# The gray area added if someone is familiar
FAMILIARITY_GRAY_AREA = 4


def gray_area_size(_data):
    """
    Determines the size of the gray area given to a certain person
    :param _data
    :return: The gray area
    """
    attractiveness = _data["attractiveness"]
    _weather = _data["weather"]
    carrying = _data["carrying"]

    g_area = GENERAL_GRAY_AREA * _weather

    if carrying:
        g_area += 4

    if attractiveness < 6:
        return g_area

    return ((attractiveness - 6) * 1640) + g_area


def assessment(_data):
    """
    Returns a summary of why the door should (or not) be opened
    :param _data: the data dictionary
    :return:
    """
    if not _data["someone_behind"]:
        return "No one behind, why bother?"

    should = hold_door(True, _data)
    print_out = ""

    if should:
        print_out += "You should because:\n"
        if _data["weather"] < .6:
            print_out += "* The weather is very nasty\n"
        if 5 < _data["attractiveness"] < 8:
            print_out += "* The person is attractive\n"
        elif _data["attractiveness"] >= 8:
            print_out += "* The person is VERY attractive\n"
        if _data["authorized"]:
            print_out += "* This is probably or colleague (could be your boss)\n"
        if "carrying" in _data and _data["carrying"]:
            print_out += "* This person needs your help, you don't want to be rude\n"
        if data["distance"] <= 4.5:
            print_out += "* This person is within the acceptable distance\n"
        elif (data["distance"] - 4.5) < gray_area_size(data):
            print_out += "* This person is within the acceptable distance and gray area\n"
        elif (data["distance"] - 4.5) < data["speed"] - TIME_TO_OPEN_DOOR:
            print_out += "* This person is walking pretty fast and will be within the acceptable distance soon\n"
    else:
        print_out += "You shouldn't because:\n"
        if not _data["authorized"] and _data["authorized"] is not None:
            print_out += "* Person not authorized to enter, who knows what the intentions of this person are, " \
                         "DON't OPEN IT, let security handle it\n"
        if _data["weather"] < .6:
            print_out += "* Don't despite the weather is very nasty\n"
        if _data["attractiveness"] >= 8:
            print_out += "* You will anyways since this person is VERY attractive (you might get in trouble though)\n"
        if _data["carrying"]:
            print_out += "* This person needs your help, but you shouldn't provide it (sorry)\n"
        if (data["distance"] - 4.5) > gray_area_size(data):
            print_out += "* This person is too far\n"
        elif (data["distance"] - 4.5) > data["speed"] - TIME_TO_OPEN_DOOR:
            print_out += "* This person is too far, not walking fast enough\n"
    return print_out


def hold_door(is_someone_behind_you, _data=None):
    """
    Returns whether the door should be held
    :param is_someone_behind_you: whether there's a person for whom the door could be held for
    :param _data: the data to determine whether the hold should be held
    :return: True if the door should be held, False otherwise
    """
    if is_someone_behind_you and _data:
        if _data["authorized"] is not None:
            if not _data["authorized"]:
                return False
        if _data["distance"] <= 4.5:
            return True
        elif (_data["distance"] - 4.5) < gray_area_size(_data):
            return True
        elif (_data["distance"] - 4.5) < _data["speed"] - TIME_TO_OPEN_DOOR:
            return True

        return False
    elif is_someone_behind_you:
        raise NameError('If \'is_someone_behind_you\' is true then \'data\' must be provided')
    else:
        return True


def get_param(args, param_name):
    """
    Returns the given param if found in the list of args in its most convenient format (int, string, boolean)
    :param args: the list of args
    :param param_name: the name of the parameter to find
    :return: the value of the parameter if found, None otherwise
    """
    if param_name not in args:
        return None

    arg = args[args.index(param_name) + 1]
    if arg in ["true", "True", "t", "T"]:
        return True
    elif arg in ["false", "False", "f", "F"]:
        return False
    try:
        return float(arg)
    except ValueError:
        return arg


if __name__ == '__main__':
    if '-h' in sys.argv or '-help' in sys.argv:
        print(help_message)
        exit()
    data = {}
    if len(sys.argv) == 1:
        print("DEMOING")
        r = randint(0, len(doorHoldingData) - 1)
        data = doorHoldingData[r]
        data["someone_behind"] = True
    else:
        if '--someone_behind' not in sys.argv:
            print(help_message)
            exit()
        else:
            data["someone_behind"] = get_param(sys.argv, "--someone_behind")
        if data["someone_behind"] and ('--distance' not in sys.argv or '--speed' not in sys.argv):
            print(help_message)
            exit()

        data["distance"] = get_param(sys.argv, "--distance")
        data["speed"] = get_param(sys.argv, "--speed")
        data["attractiveness"] = get_param(sys.argv, "--attractiveness")
        data["weather"] = get_param(sys.argv, "--weather")
        data["authorized"] = get_param(sys.argv, "--authorized")
        data["carrying"] = get_param(sys.argv, "--carrying")
        attract = get_param(sys.argv, "--attractiveness")
        data["attractiveness"] = attract if attract is not None else 5
        weather = get_param(sys.argv, "--weather")
        data["weather"] = weather if weather else 1
        print(data)
        print(assessment(data))
        exit()
    print(data)
    print(assessment(data))
