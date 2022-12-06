MyData = open("C:\Code\Advent of Code 2022\Day6.txt").read()
#MyData = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

def checkIfDuplicate(mylist: list) -> bool:
    myset = set(mylist)
    return len(mylist) is not len(myset)

def mainfun(mystring, nounique):
    counter = 0
    markerList = []

    for i in range(len(mystring)):
        markerList.append(mystring[i])
        counter += 1
        if len(markerList) == nounique:
            if checkIfDuplicate(markerList):
                del markerList[0]
            else:
                break

    print(counter)

mainfun(MyData,4)
mainfun(MyData,14)