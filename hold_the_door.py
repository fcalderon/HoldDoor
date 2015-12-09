__author__ = 'Francisco Calderon and Grant Merrill'

#TODO Update weather to be a number between 0 and 1

doorHoldingData = [
    {"distance": 4.5, "speed": 5, "attractiveness": 0, "familiarity": 0, "carrying": True, "weather": .9},
    {"distance": 7.5, "speed": 4, "attractiveness": 1, "familiarity": 0, "carrying": False,
     "weather": "scatter clouds, cold"},
    {"distance": 4, "speed": 4, "attractiveness": 1, "familiarity": 0, "carrying": False, "weather": .3},
    {"distance": 6.5, "speed": 4.2, "attractiveness": 3, "familiarity": 0, "carrying": True,
     "weather": "snowing, very cold, icy"},
    {"distance": 3, "speed": 4.5, "attractiveness": 0, "familiarity": 0, "carrying": False, "weather": "raining, warm"},
    {"distance": 7, "speed": 3, "attractiveness": 0, "familiarity": 0, "carrying": True, "weather": "snowing"},
    {"distance": 3, "speed": 4.5, "attractiveness": 0, "familiarity": 0, "carrying": False, "weather": "sunny, very cold"},
    {"distance": 15, "speed": 5, "attractiveness": 3, "familiarity": 0, "carrying": True, "weather": "cloudy, warm"},
    {"distance": 3, "speed": 4.5, "attractiveness": 0, "familiarity": 0, "carrying": True, "weather": "cloudy, cold"},
    {"distance": 20, "speed": 3, "attractiveness": 0, "familiarity": 1, "carrying": False, "weather": "sunny, warm"},
    {"distance": 25, "speed": 3, "attractiveness": 0, "familiarity": 0, "carrying": False,
     "weather": "raining, thunderstorm, warm"},
    {"distance": 20, "speed": 3, "attractiveness": 0, "familiarity": 0, "carrying": True, "weather": "raining, cold"}
]

TIME_TO_OPEN_DOOR = 1
GENERAL_GRAY_AREA = 2

WEATHER_STATES = ['COLD', 'VERY COLD', 'RAINING', 'SNOWING', ]


def gray_area_size(attractiveness, weather=1, carrying=False):
    """
    Determines the size of the gray area given to a certain person
    :param attractiveness: Number between 0 and 10 describing the attractiveness of a person
    :param weather: what the weather is between 0 (very bad) and 1 (very nice)
    :param carrying: whether the person is holding something
    :return:
    """
    g_area = GENERAL_GRAY_AREA * weather
    if carrying:
        g_area += 4

    if attractiveness < 6:
        return g_area

    return ((attractiveness - 6) * 1640) + g_area


def hold_door(is_someone_behind_you, data=None):
    """

    :param is_someone_behind_you: whether there's a person for whom the door could be held for
    :param data: the data
    :return:
    """

    if is_someone_behind_you and data:
        if data["distance"] <= 4.5:
            return True
        elif (data["distance"] - 4.5) < gray_area_size(data["attractiveness"]):
            return True
        elif (data["distance"] - 4.5) < data["speed"] - TIME_TO_OPEN_DOOR:
            return True

    return False

