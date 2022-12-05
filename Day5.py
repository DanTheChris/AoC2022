import re
import copy

#initialising data
MyData = open("C:\Code\Advent of Code 2022\Day5.txt").read()
#MyData = """    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 
#
#move 1 from 2 to 1
#move 3 from 1 to 3
#move 2 from 2 to 1
#move 1 from 1 to 2"""

DataSplit = MyData.split("\n\n")
Commands = DataSplit[1].split("\n")

DockRaw = DataSplit[0].split("\n")
Dock = []

#Stack class to track each column
class Stack:
    
    def __init__(self, a):
        self.a = a
        self.crates = []
    
    def UnloadCrate(self) -> str:
        return self.crates.pop()
    
    def LoadCrate(self, crate: str):
        self.crates.append(crate)

#Crate moving logics
def MoveCrates(command: str, dock):
    CurrentCrate = ''
    
    inputstr = re.findall('\d+', command)
    inputs = []
    
    for input in inputstr:
        inputs.append(int(input))
    
    for i in range(inputs[0]):
        CurrentCrate = dock[inputs[1] - 1].UnloadCrate()
        dock[inputs[2] - 1].LoadCrate(CurrentCrate)
    
    CurrentCrate = ''

def MoveMultiCrates(command: str, dock):
    CurrentCrates = []
    
    inputstr = re.findall('\d+', command)
    inputs = []

    for input in inputstr:
        inputs.append(int(input))
    
    for i in range(inputs[0]):
        CurrentCrates.append(dock[inputs[1] - 1].UnloadCrate())
    
    for i in range(len(CurrentCrates)):
        dock[inputs[2] - 1].LoadCrate(CurrentCrates.pop())
        
#Creating a list of stacks with the correct inputs, ignoring blank space
for i in range(9):
    Dock.append(Stack(i))

for i in range(len(DockRaw)-2, -1, -1):
    for j in range(9):
        if DockRaw[i][j*4+1] is not ' ':
            Dock[j].LoadCrate(DockRaw[i][j*4+1])

#Copying list of stacks for Part 2
Dock9001 = copy.deepcopy(Dock)

#Actually moving the crates
for command in Commands:
    MoveCrates(command, Dock)

#Finding and noting the top crates
TopCrates = ''
for stack in Dock:
    TopCrates = TopCrates + stack.crates[-1]

print(TopCrates)

#Actually moving the crates for part 2
for command in Commands:
    MoveMultiCrates(command, Dock9001)

#Finding and noting the top crates
Top9001Crates = ''
for stack in Dock9001:
    Top9001Crates = Top9001Crates + stack.crates[-1]

print(Top9001Crates)