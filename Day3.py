from asyncio.windows_events import NULL


MyData = open("C:\Code\Advent of Code 2022\Day3.txt").read()
#MyData = """vJrwpWtwJgWrhcsFMMfFFhFp
#jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#PmmdzqPrVvPwwTWBwg
#wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
#ttgJtRGJQctTZtZT
#CrZsJsPPZsGzwwsLwLmpwMDw"""

Rucksacks = MyData.split("\n")

Compartments = [[rucksack[:int(len(rucksack)/2)],rucksack[int(len(rucksack)/2):]] for rucksack in Rucksacks]

def CheckDupeChar(string1, string2):
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] is string2[j]:
                return string1[i]
    return NULL

def FindValues(character):
    if character.isupper():
        return ord(character) - 64 + 26
    elif not character.isupper():
        return ord(character) - 96

Items = []

for compartment in Compartments:
    Items.append(CheckDupeChar(compartment[0], compartment[1]))

Total = 0

for item in Items:
    Total += FindValues(item)

print(Total)

Badges = []
Total = 0

for i in range(int(len(Rucksacks)/3)):
    Check = True
    while Check:
        PotentialBadge = CheckDupeChar(Rucksacks[i*3],Rucksacks[i*3+1])
        if CheckDupeChar(PotentialBadge,Rucksacks[i*3+2]) == NULL:
            Rucksacks[i*3]=Rucksacks[i*3].replace(PotentialBadge,'')
        else:
            Badges.append(PotentialBadge)
            Check = False

for badge in Badges:
    Total += FindValues(badge)
    
print(Total)