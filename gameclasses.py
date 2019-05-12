class game:
    def __init__(self, noofquestions=0):
        self._noofquestions = noofquestions
    @property
    def noofquestions(self):
        return self._noofquestions
    @noofquestions.setter
    def noofquestions(self,value):
        if value < 1:
            self._noofquestions = 1
            print('Question number is 1 now')
        elif value > 10:
            self._noofquestions =10
            print('Question number is 10 now')
        else :
            self._noofquestions =value


class binarygame(game):
    def generatequestions(self):
        from random import randint
        score=0
        for i in range(self.noofquestions):
            base10=randint(1,100)
            messge="Enter binary for number: %d" %(base10)
            userresult = input(messge)
            while 1==1:
                try:
                    answer=int(userresult,base = 2)
                    if base10 == answer:
                        print('right')
                        score+=1
                        break
                    else:
                        print('wrong,the correct answer is {:b}.'.format(base10))
                        break
                except:

                    userresult=input("wrong format, please enter a binary for number: %d"  %(base10))

        return score

if __name__=='__main__':
    bgame=binarygame()
    bgame.noofquestions = 5
    print('score is %d' %(bgame.generatequestions()))