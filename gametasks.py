# contains 3 functions
from os import remove,rename
class GamesTasks:
    def __init__(self, instruction):
        self.instruction = instruction
        self.printinstruction()




    def printinstruction(self):
        print(self.instruction)



    def getuserscore(self,username_in):
        namescores={}
        try:
            with open('scorefile.txt','r') as f:
                for line in f:

                    # print(line)
                    name,score = line.split(',')
                    namescores[name] =score

        except IOError as ioe:
            with open('scorefile.txt','w') as f:
                print('create file')
        finally:
            f.close()


        for name,score in namescores.items():
            if name == username_in:
                return score
        return -1

    def updateUserScore(self,newuser,username,newscore):
        # newuser append score
        contents = {}
        if newuser:
            with open('scorefile.txt','a') as f:
                newline =  username+ ','+ str(newscore)
                f.write(newline)
                f.close()
        # existing user , update the score
        else:
            with open('scorefile.txt', 'r') as fread:
                for line in fread:
                    name, score = line.split(',')
                    contents[name] = score
                print(contents)
            fread.close()

            with open('scorefile.tmp', 'a') as fwrite:
                for name,score in contents.items():
                    if name == username:
                        oldline =  username+ ','+ str(newscore) +'\n'
                    else:
                        oldline = name + ',' + str(score)
                    print(oldline)
                    fwrite.write(oldline)
            fwrite.close()
            remove('scorefile.txt')
            print('rename')
            rename('scorefile.tmp', 'scorefile.txt')




if __name__ == '__main__':
    gTasks = GamesTasks("tests")
    print(gTasks.getuserscore('cx'))
    # gTasks.updateUserScore(False,'cx',999)
    # gTasks.updateUserScore(True,'Bryan',1000)
    # gTasks.updateUserScore(False, 'Bryan', 899)
    # gTasks.updateUserScore(True, 'Yini', 600)