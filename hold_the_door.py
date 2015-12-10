__author__ = 'Francisco Calderon and Grant Merrill'

# TODO Update attractiveness to be a number between 0 and 10
# TODO update familiar to be whether the person is authorized to enter through that door


doorHoldingData = [
    {"distance": 4.5, "speed": 5, "attractiveness": 0, "familiar": False, "carrying": True, "weather": .9},
    {"distance": 7.5, "speed": 4, "attractiveness": 1, "familiar": False, "carrying": False,
     "weather": "scatter clouds, cold"},
    {"distance": 4, "speed": 4, "attractiveness": 1, "familiar": False, "carrying": False, "weather": 1},
    {"distance": 6.5, "speed": 4.2, "attractiveness": 6, "familiar": True, "carrying": True,
     "weather": "snowing, very cold, icy"},
    {"distance": 3, "speed": 4.5, "attractiveness": 7, "familiar": False, "carrying": False, "weather": .5},
    {"distance": 7, "speed": 3, "attractiveness": 1, "familiar": False, "carrying": True, "weather": .3},
    {"distance": 3, "speed": 4.5, "attractiveness": 3, "familiar": False, "carrying": False, "weather": .7},
    {"distance": 15, "speed": 5, "attractiveness": 8, "familiar": False, "carrying": True, "weather": .6},
    {"distance": 3, "speed": 4.5, "attractiveness": 2, "familiar": False, "carrying": True, "weather": .7},
    {"distance": 20, "speed": 3, "attractiveness": 10, "familiar": True, "carrying": False, "weather": 1},
    {"distance": 25, "speed": 3, "attractiveness": 1, "familiar": False, "carrying": False,
     "weather": .6},
    {"distance": 20, "speed": 3, "attractiveness": 5, "familiar": True, "carrying": True, "weather": .5}
]

# Mean time it takes to fully open a door
TIME_TO_OPEN_DOOR = 1

# The general area everyone is entitled to
GENERAL_GRAY_AREA = 2

# The gray area added if someone is familiar
FAMILIARITY_GRAY_AREA = 4


def gray_area_size(attractiveness, weather=1, carrying=False):
    """
    Determines the size of the gray area given to a certain person
    :param attractiveness: Number between 0 and 10 describing the attractiveness of a person
    :param weather: what the weather is between 0 (very bad) and 1 (very nice or indoor)
    :param carrying: whether the person is holding something
    :return: The gray area
    """
    g_area = GENERAL_GRAY_AREA * weather
    if carrying:
        g_area += 4

    if attractiveness < 6:
        return g_area

    return ((attractiveness - 6) * 1640) + g_area


def hold_door(is_someone_behind_you, data=None):
    """
    Returns whether the door should be held
    :param is_someone_behind_you: whether there's a person for whom the door could be held for
    :param data: the data to determine whether the hold should be held
    :return: True if the door should be held, False otherwise
    """
    if is_someone_behind_you and data:
        if data["distance"] <= 4.5:
            return True
        elif (data["distance"] - 4.5) < gray_area_size(data["attractiveness"]):
            return True
        elif (data["distance"] - 4.5) < data["speed"] - TIME_TO_OPEN_DOOR:
            return True

        return False
    elif is_someone_behind_you:
        raise NameError('If \'is_someone_behind_you\' is true then \'data\' must be provided')
    else:
        return True

if __name__ == '__main__':
    print("Should hold door: (yes)", hold_door(True, doorHoldingData[0]))
    print("Should hold door: (no)", hold_door(True, doorHoldingData[1]))

