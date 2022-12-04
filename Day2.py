from decimal import Rounded

MyData = open("C:\Code\Advent of Code 2022\Day2.txt").read()
#MyData = """A Y
#B X
#C Z"""

Rounds = MyData.split("\n")
RoundsSplit = [round.split(" ") for round in Rounds]

def decrypt(play):
    match(play):
        case "A" | "X":
            return int(1)
        case "B" | "Y":
            return int(2)
        case "C" | "Z":
            return int(3)

DecodedRounds = []

for round in RoundsSplit:
    DecodedRounds.append([decrypt(play) for play in round])

TotalScore = 0

def CalcScore(MyMove, OpponentMove):
    if abs(MyMove - OpponentMove) == 2:
        return ((MyMove - OpponentMove)/-2 + 1) * 3 + MyMove
    else:
        return (MyMove - OpponentMove + 1) * 3 + MyMove

for round in DecodedRounds:
    TotalScore += CalcScore(round[1], round[0])

print(TotalScore)

def CalcScore2(Result, OpponentMove):
    if Result - 2 + OpponentMove == 0:
        return (Result - 1) * 3 + 3
    elif Result - 2 + OpponentMove == 4:
        return (Result - 1) * 3 + 1
    else:
        return (Result - 1) * 3 + Result - 2 + OpponentMove
    
TotalScore = 0

for round in DecodedRounds:
    TotalScore += CalcScore2(round[1], round[0])

print(TotalScore)