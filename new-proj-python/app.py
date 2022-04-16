# rows = int(input('Enter the number of rows'))
# for x in range(rows):
#     print('*' * (x+1))

# _______________________

# limit = int(input('Enter the limit'))
# for x in range(limit+1):
#     if x % 2 == 0:
#         print(f'{x} is EVEN')
#     else:
#         print(f'{x} is ODD')

# _______________________

# limit = int(input('Enter the limit'))
# summ = 0
# for x in range(limit+1):
#     if x % 3 == 0 or x % 5 == 0:
#         summ += x
# print(summ)

# ------same

# limit = int(input('Enter the limit'))
# numbers = [n for n in range(limit+1) if n % 3 == 0 or n % 5 == 0]
# print(sum(numbers))

# _______________________

# first_list = [1, 2, 3, 4, 5]
# second_list = [11, 12, 13, 14, 15]

# first_odd = [n for n in first_list if n % 2 != 0]
# second_even = [n for n in second_list if n % 2 == 0]
# list = first_odd + second_even
# print(list)

# _______________________

# current_hand = [2, 3, 4, 10, 'Q', 5]
# current_hand2 = ['A', 3, 4, 10, 'J', 4]
# current_hand3 = [2, 7, 4, 9, 3, 5]

# sum = 0

# for x in current_hand:
#     if x in [2, 3, 4, 5, 6]:
#         sum += 1
#     elif x in [10, 'J', 'Q', 'K', 'A']:
#         sum += 4

# print(sum)

# ------same

# cards = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0,
#          9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
# sum = sum([cards[x] for x in current_hand])

# print(sum)

#  _______________________

# table_cards = ['A_S', 'J_H', '7_D', '8_D', '10_D']
# hand_cards = ['J_D', '3_D']

# cards = table_cards + hand_cards
# all_suits = [x[-1] for x in cards]

# ---
# if all_suits.count('S') >= 5 or all_suits.count('H') >= 5 or all_suits.count('D') >= 5 or all_suits.count('C') >= 5:
#     print('Flush!')
# else:
#     print('No Flush!')

# ---same
# flush = False
# for suit in 'CHSD':
#     if all_suits.count(suit) >= 5:
#         flush = True

# if flush:
#     print('Flush!')
# else:
#     print('No Flush!')

#  _______________________

# import random

# number = random.randint(1, 50)

# tries = 0
# while tries <= 5:
#     entered_number = int(input('GuessNumber'))
#     tries += 1
#     if entered_number == number:
#         print('yes!')
#         break
#     else:
#         print('no')

#  _______________________

# players = [('Carl', 2842), ('Caru', 2822), ('Mame', 2801), ('Ding', 2797)]

# print(all(rating > 2700 for _, rating in players))

#  _______________________

# letters = 'abcd'
# numbers = (10, 20, 30)

# zipped_list = list(zip(letters, numbers))
# zipped_dict = dict(zip(letters, numbers))

# print(zipped_list)
# print(zipped_dict)

#  _______________________

# def calc_taxes(*args):
#     for x in args:
#         print(x)
#     return sum(args) * 0.1


# print(calc_taxes(10, 20, 70))

#  _______________________

# def show_players(**kwargs):
#     for k, v in kwargs.items():
#         print(f'Player {k} has rating {v}')


# print(show_players(Carlsen=2800, Giri=2780))

#  _______________________


# def square(number):
#     return number*number


# numbers = [1, 2, 3, 4, 5]

# for x in map(square, numbers):
#     print(x)

# mapped_numbers = list(map(square, numbers))

# print(mapped_numbers)

#  _______________________

# ages = [13, 18, 12, 20, 35]

# print(list(filter(lambda age: age >= 18, ages)))

#  _______________________

# def log_decorator(func):
#     def wrap():
#         print(f'Calling func {func}')
#         func()
#         print(f'Func {func} finished its work')
#     return wrap


# @log_decorator
# def hello():
#     print('Hello world!')


# hello()

#  _______________________

# from timeit import default_timer as timer
# import math
# import time


# def measure_time(func):
#     def inner(*args, **kwargs):
#         start = timer()
#         func(*args, **kwargs)
#         end = timer()
#         print(end)
#         print(f'Function {func.__name__} took {end-start} for execution')
#     return inner


# @measure_time
# def factorial(num):
#     time.sleep(3)
#     print(math.factorial(num))


# factorial(3)

#  _______________________

# from functools import wraps


# def log_decorator(func):
#     @wraps(func)
#     def wrap(*args, **kwargs):
#         print(f'Calling func {func}')
#         func(*args, **kwargs)
#         print(f'Func {func} finished its work')
#     return wrap


# @log_decorator
# def hello():
#     print('Hello world!')


# help(hello)

#  _______________________

# def who_first(p1, p2):
#     p1_hit = len(p1.split("Bang!")[0])
#     p2_hit = len(p2.split("Bang!")[0])

#     if p1_hit < p2_hit:
#         print(f'p1 was faster')
#     elif p1_hit > p2_hit:
#         print(f'p2 was faster')
#     else:
#         print('tie')


# who_first("      Bang!   ", "    Bang!     ")

#  ------same

# def who_first(p1, p2):
#     diff = p1.find('B') - p2.find('B')
#     if diff < 0:
#         return 'p1'
#     elif diff > 0:
#         return 'p2'
#     else:
#         return 'tie'


# print(who_first("     Bang!    ",
#                 "  Bang!     "))

#  _______________________

# def calc_dice_scores(list):
#     sum = 0
#     for x, y in list:
#         if x == y:
#             sum = 0
#             return sum
#         sum += x+y
#     return sum


# print(calc_dice_scores([(1, 2), (2, 3), (5, 6)]))
# print(calc_dice_scores([(2, 2), (2, 3), (5, 6)]))
# print(calc_dice_scores([(1, 2), (2, 3), (5, 5)]))

#  ---same

# def calc_dice_scores(list):
#     return sum([a+b for a, b in list]) if not any([a == b for a, b in list]) else 0


# print(calc_dice_scores([(1, 2), (2, 3), (5, 6)]))
# print(calc_dice_scores([(2, 2), (2, 3), (5, 6)]))
# print(calc_dice_scores([(1, 2), (2, 3), (5, 5)]))

#  _______________________

# def any_duplicates(array):
#     all_numbers = [i for x in array for i in x]

#     return len(all_numbers) != len(set(all_numbers))

# print(any_duplicates([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

#  _______________________

# def get_int():
#     while True:
#         try:
#             reply = int(input('Enter a number'))
#             return reply
#         except:
#             print('Not a number! Try again.')
#             continue

# number = get_int()
# print(number)

#  _______________________

# import math


# def calc_square(ab, ac, bc):

#     if ab <= 0 or ac <= 0 or bc <= 0:
#         raise ValueError('One of the sides equal or less to 0.')

#     p = (ab + ac + bc) / 2
#     s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))
#     print(s)

#     return s


# try:
#     calc_square(-3, 4, 5)
# except ValueError as ex:
#     print(ex)

# -----same

# import math


# class InvalidTriangleError(Exception):
#     """Raised when a triangle has invalid sides"""


# def calc_square(ab, ac, bc):

#     if ab <= 0 or ac <= 0 or bc <= 0:
#         raise InvalidTriangleError('One of the sides equal or less to 0.')

#     p = (ab + ac + bc) / 2
#     s = math.sqrt(p * (p - ab) * (p - ac) * (p - bc))

#     return s


# try:
#     square = calc_square(-3, 4, 5)
# except InvalidTriangleError as ex:
#     print(ex)
# else:
#     print(square)

#  _______________________

# class Character():

#     MAX_SPEED = 100
#     DEAD_HEALTH = 0

#     def __init__(self, race, damage=10):
#         self.__race = race
#         self.damage = damage
#         self._health = 100
#         self._current_speed = 20

#     def hit(self, damage):
#         self._health -= damage

#     def is_dead(self):
#         return self._health == Character.DEAD_HEALTH

#     @property
#     def health(self):
#         return self._health

#     @property
#     def race(self):
#         return self.__race

#     @property
#     def current_speed(self):
#         return self._current_speed

#     @current_speed.setter
#     def current_speed(self, current_speed):
#         if current_speed < 0:
#             self._current_speed = 0
#         elif current_speed > 100:
#             self._current_speed = 100
#         else:
#             self._current_speed = current_speed


# unit = Character('Elf')
# unit.hit(10)

# print(unit._Character__race)
# print(Character.MAX_SPEED)
# print(unit._health)
# print(unit.is_dead())
# print(unit.race)

# unit.current_speed = 30
# print(unit.current_speed)

#  _______________________

# class StaticTest:
#     x = 1


# t1 = StaticTest()

# t1.x = 2
# StaticTest.x = 3

# print(f'via instance: {t1.x}')
# print(f'via class: {StaticTest.x}')

#  _______________________

# class Date:
#     def __init__(self, month, day, year):
#         self.month = month
#         self.day = day
#         self.year = year

#     def display(self):
#         return f'{self.month}-{self.day}-{self.year}'

#     @classmethod
#     def millenium_c(cls, month, day):
#         return cls(month, day, 2000)

#     @staticmethod
#     def millenium_s(month, day):
#         return Date(month, day, 2000)


# d1 = Date.millenium_c(6, 9)
# d2 = Date.millenium_s(6, 9)


# class DateTime(Date):
#     def display(self):
#         # return super().display():
#         return f'{self.month}-{self.day}-{self.year} - 00:00:00'


# dt1 = DateTime(10, 10, 1990)
# dt3 = DateTime.millenium_c(10, 10)
# dt2 = DateTime.millenium_s(10, 10)

# print(isinstance(dt1, DateTime))
# print(isinstance(dt3, DateTime))
# print(isinstance(dt2, DateTime))


# print(dt1.display())
# print(dt3.display())
# print(dt2.display())

#  _______________________

# class Shape:
#     def __init__(self):
#         print('Shape created')

#     def draw(self):
#         print('Drawing a shape')

#     def area(self):
#         print('Calc area')

#     def perimeter(self):
#         print('Drawing perimeter')


# shape = Shape()


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         Shape.__init__(self)

#         self.width = width
#         self.height = height

#         print('Rectangle created')

#         Shape.area(self)

#     def draw(self):
#         print('Drawing rectangle {self.width} x {self.height}')

#     def area(self):
#         print(self.width * self.height)
#         return self.width * self.height

#     def perimeter(self):
#         print(2*(self.width+self.height))
#         return 2*(self.width+self.height)


# rectangle = Rectangle(10, 20)

# rectangle.area()

#  _______________________

# class Shape:
#     def __init__(self):
#         print('Shape cteated')

#     def draw(self):
#         raise NotImplementedError("Can't instantiate an abstract class")

#     def area(self):
#         raise NotImplementedError("Can't instantiate an abstract class")

#     def perimeter(self):
#         raise NotImplementedError("Can't instantiate an abstract class")

#  _______________________

# class Animal:

#     def __init__(self):
#         self.health = 100

#     def hit(self, damage):
#         self.health -= damage


# class Carnivour(Animal):

#     def __init__(self):
#         super().__init__()
#         self.legs = 4


# c = Carnivour()
# c.hit(20)

# print(c.health)

#  _______________________

# from abc import ABC, abstractmethod
# import math


# class Shape(ABC):

#     def __init__(self):
#         super().__init__()

#     @abstractmethod
#     def draw(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         print('calc perimeter')

#     def drag(self):
#         print('basic functionality')


# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         super().__init__()
#         self.a = a
#         self.b = b
#         self.c = c

#     def draw(self):
#         print(f'sides {self.a} {self.b} {self.c}')

#     def area(self):
#         s = (self.a + self.b + self.c) / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

#     def perimeter(self):
#         return self.a + self.b + self.c

#     def drag(self):
#         super().drag()
#         print('additional actions')


# t = Triangle(10, 10, 20)
# t.drag()

#  _______________________


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_state(state):
    for i, n in enumerate(state):
        if (i+1) % 3 == 0:
            print(n)
        else:
            print(f'{n}|', end='')


winning_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                       (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def get_winner(state, combinations):
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == '0'):
            return state[x]
    return ''


def play_game(board):
    current_sign = 'X'
    while(get_winner(board, winning_combination) == ''):
        index = int(input(f'where do you want to draw {current_sign}?'))
        if (index < 0 or index > 8):
            print(f"cell number can be from 0 to 8")
            continue

        elif board[index] != ' ':
            print(f'this cell already has a value, choose another')
            continue

        else:
            board[index] = current_sign

        print_state(board)
        winner_sign = get_winner(board, winning_combination)
        if winner_sign != '':
            print(f'Sigh {current_sign} is win')
            break

        if not (' ' in board):
            print('game over')
            break

        current_sign = '0' if current_sign == 'X' else 'X'


play_game(board)

#  _______________________
