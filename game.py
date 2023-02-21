# import random 
 
# name = input("введіть ваше ім'я") 
# players = set(name) 
 
# print("Гра \"Пошук Скарбів\"") 
# def level(): 
#     print("вибери складність") 
 
# def Map(): 
#     map = [] 
#     for i in size: 
#         pass 
 
# class Game(): 
#     def easy(): 
#         size = 3 
#         Map(size) 
 
#     def medium(): 
#         size = 5 
#         Map(size) 
#     def difficult(): 
#         size = 10 
#         Map(size) 
     
# difficulty = input("1 - Легкий \n2 - Середній\n3 - Складний") 
 
 
# game = Game() 
 
# if difficulty == 1 or difficulty == "Легкий": 
#     game.easy() 
# elif difficulty == 2 or difficulty == "Середній": 
#     game.medium() 
# elif difficulty == 3 or difficulty == "Складний": 
#     game.difficult() 
# else: 
#     print("це не рівень складності") 
#     level()

# def diggingGame():
#     class Game():
#         def __init__(self, difficulty):
#             self.difficulty = str(difficulty)


# diggingGame().Game()

# import random

# # Створюємо клас гри
# class TreasureHunt:
#     def __init__(self, width, height, username):
#         self.width = width
#         self.height = height
#         self.username = username
#         self.treasure_x = random.randint(0, width-1)
#         self.treasure_y = random.randint(0, height-1)

#     def play(self):
#         print(f"Вітаю, {self.username}! Вирушаємо на пошуки скарбів! Координати нашого скарбу - ({self.treasure_x}, {self.treasure_y})")
#         attempts = 0
#         while True:
#             guess_x = int(input("Введіть координату x: "))
#             guess_y = int(input("Введіть координату y: "))
#             attempts += 1
#             if guess_x == self.treasure_x and guess_y == self.treasure_y:
#                 print(f"Вітаю, ви знайшли скарб за {attempts} спроб!")
#                 break
#             else:
#                 print("Ви не знайшли скарб, спробуйте знову")

# # Створюємо меню вибору складності та нікнейму користувача
# print("Вітаю в грі Пошук скарбів!")
# username = input("Введіть ваш нікнейм: ")
# difficulty = input("Оберіть складність (легкий, середній, складний): ")
# if difficulty == "легкий":
#     game = TreasureHunt(5, 5, username)
# elif difficulty == "середній":
#     game = TreasureHunt(10, 10, username)
# elif difficulty == "складний":
#     game = TreasureHunt(20, 20, username)
# else:
#     print("Невірна складність, гра завершена")
#     exit()

# game.play()
import random
class Game:
    def __init__(self, width, height, name):
        self.width = int(width)
        self.height = int(height)
        self.name = str(name)
        self.treasure_x = random.randint(0, width-1)
        self.treasure_y = random.randint(0, height-1)
        self.trapX
    
    def game(self):
        print(f"Вітаю, {self.name}! Час знайти скарби!")
        attempts = 0
        while True:
            guessableX =  int(input("Виберіть координату x: "))
            guessable_y = int(input("Виберіть координату y: "))
            attempts+=1
            if guessableX == self.treasure_x and guessable_y == self.treasure_y:
                print(f"Вітаю, ви перемогли за {attempts} ходів")
            elif guessableX == self.trapX and guessable_y == self.trpaY:
                print("Ви попали в пастку((. Щасти наступного разу!")
            else: 
                print("нічого........")