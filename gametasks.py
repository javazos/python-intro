# contains 3 functions
class GamesTasks:
    def __init__(self, instruction,username):
        self.instruction = instruction
        self.username = username
        print(self.instruction, self.username)


    def printinstruction(self):
        print(self.instruction)

    def getusername(self):
        return self.username

    def readfile(self):
        namescores={}

        with open('scorefile.txt','r') as f:
            for line in f:
                # line = f.readline()
                print(line)
                name,score = line.split(',')
                namescores[name] =score

        print(namescores)


        for name,score in namescores.items():
            if name == self.getusername():
                print(score)
                return score
if __name__ == '__main__':
    gTasks = GamesTasks("tests",'cx')
    gTasks.readfile()