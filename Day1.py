from operator import attrgetter

MyData = open("C:\Code\Advent of Code 2022\Day1.txt").read()
print(MyData)

class Elf:
    def __init__(self, BackpackStr):
        self.Backpack = BackpackStr.split('\n')
        self.Calories = 0
        for item in self.Backpack:
            if can_convert_to_int(item):
                self.Calories += int(item)
            else:
                continue
                

def can_convert_to_int(string):
    try:
        int(string)

        return True
    except ValueError:
        return False

ElvesStr = MyData.split('\n\n')
Elves = []

for elf in ElvesStr:
    Elves.append(Elf(elf))

FattestElf = max(Elves, key = attrgetter('Calories'))
print(FattestElf.Calories)

TotalCal = 0

for i in range(3):
    FattestElf = max(Elves, key = attrgetter('Calories'))
    TotalCal += FattestElf.Calories
    Elves.remove(FattestElf)

print(TotalCal)