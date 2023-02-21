from random import randint as rand

def treasureHunt():
    print("\"Пошук Скарбів\"")
    name = input("введіть ім'я гравця: ")
    choosenDifficulty = input("виберіть складність: \n1 легко, \n2 середньо, \n3 складно \n(вводьте лише цифри)\n")
    waterCount = 2
    movements = 5
    dii = ["go", "dig", "search"]
    def stats(self):
        if self.choosenDifficulty == 1:
            waterCount = 2
            beastCount = 0
            keyCount = 0
            showelCountMax = 0
            yMax = 5
            xMax = yMax
        elif self.choosenDifficulty == 2:
            waterCount = 2
            beastCount = 1
            keyCount = 0
            showelCountMax = 1
            yMax = 10
            xMax = yMax
        elif self.choosenDifficulty == 3:
            waterCount = 2
            beastCount = 2
            keyCount = 1
            showelCountMax = 1
            yMax = 20
            xMax = 20
        return waterCount, beastCount, keyCount, showelCountMax, xMax, yMax
    MAP = []
    def game(yMax, xMax):
        for i in yMax:
            MAP.append([])
        y = rand(0, yMax-1)
        x = rand(0, xMax-1)
        return MAP
    def coordinates(yMax, xMax):
        y = rand(0, yMax-1)
        x = rand(0, xMax-1)
        return x, y
    player = {"name": name,
    "haveShovel": bool(False)
    }