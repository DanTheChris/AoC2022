MyData = open("C:\Code\Advent of Code 2022\Day7.txt").read()
#MyData = """$ cd /
#$ ls
#dir a
#14848514 b.txt
#8504156 c.dat
#dir d
#$ cd a
#$ ls
#dir e
#29116 f
#2557 g
#62596 h.lst
#$ cd e
#$ ls
#584 i
#$ cd ..
#$ cd ..
#$ cd d
#$ ls
#4060174 j
#8033020 d.log
#5626152 d.ext
#7214296 k"""

Commands = MyData.split('\n')
FlatDir = []

class Dir:
    def __init__(self, name, original_dir = None):
        if original_dir == None:
            self.up_dir = self
        else:
            self.up_dir = original_dir
        self.name = name
        self.contents = []
        self.space = 0
    
    def input_contents(self, content: str):
        splitcontent = content.split(' ')
        if splitcontent[0] == 'dir':
            self.contents.append(Dir(splitcontent[1], self))
        else:
            self.contents.append(File(content))
    
    def findSpaceUsed(self) -> int:
        self.space = 0
        for thing in self.contents:
            if isinstance(thing, Dir):
                self.space += thing.findSpaceUsed()
            elif isinstance(thing, File):
                self.space += thing.space
        
        if self.name != '/':
            FlatDir.append(self)
        return self.space

class File:
    def __init__(self, string: str):
        components = string.split(" ")
        self.space = int(components[0])
        self.name = components[1]

MyPC = Dir('/')
CurrentDir = MyPC

for commandstr in Commands:
    command = commandstr.split(' ')
    if command[0] == "$" and command[1] == 'cd':
        match(command[2]):
            case '/':
                CurrentDir = MyPC
            case '..':
                CurrentDir = CurrentDir.up_dir
            case _:
                CurrentDir = next((folder for folder in CurrentDir.contents if (folder.name == command[2] and isinstance(folder, Dir))), None)
    elif command[0] != '$':
        CurrentDir.input_contents(commandstr)

MyPC.findSpaceUsed()

TotalSpace = 0
for directory in FlatDir:
    if directory.space <= 100000:
        TotalSpace += directory.space

print(TotalSpace)
print(MyPC.space-40000000)

print(min(folder.space for folder in FlatDir if (folder.space >= MyPC.space-40000000)))