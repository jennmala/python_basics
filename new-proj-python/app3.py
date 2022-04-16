# from enum import Enum


# class TrafficLights(Enum):
#     RED = 1
#     YELLOW = 2
#     GREEN = 3


# print(TrafficLights.RED)
# print(TrafficLights.RED.name)
# print(TrafficLights.RED.value)
# print(TrafficLights(1))
# print(TrafficLights['RED'])

# ______________________________

# from enum import IntEnum


# class Priority(IntEnum):
#     LOW = 1
#     NORMAL = 2
#     HIGH = 3


# print(Priority.LOW < Priority.NORMAL)

# ______________________________

# from enum import IntFlag


# class Color(IntFlag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4


# combination = Color.RED | Color.GREEN
# print(combination)
# print(Color(1))

# print(Color.RED in combination)

# ______________________________
