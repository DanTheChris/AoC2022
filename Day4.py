import re

MyData = open("C:\Code\Advent of Code 2022\Day4.txt").read()
#MyData = """2-4,6-8
#2-3,4-5
#5-7,7-9
#2-8,3-7
#6-6,4-6
#2-6,4-8"""

PairsRaw = MyData.split("\n")

class Elf:
    def __init__(self, Low: int, High: int):
        self.Lower = int(Low)
        self.Higher = int(High)
        self.areas = range(self.Lower,self.Higher)
    
    def iswithin(self, otherelf):
        return all(area in otherelf.areas for area in self.areas)

class Pair:
    def __init__(self, pair: str):
        pairlist = re.split(",|-", pair)
        self.elf1 = Elf(pairlist[0],pairlist[1])
        self.elf2 = Elf(pairlist[2],pairlist[3])
    
    def hasCompleteOverlap(self):
        return self.elf1.iswithin(self.elf2) | self.elf2.iswithin(self.elf1)

Pairs = [Pair(pair) for pair in PairsRaw]

Total = 0

for pair in Pairs:
    if pair.hasCompleteOverlap():
        Total += 1

print(Total)