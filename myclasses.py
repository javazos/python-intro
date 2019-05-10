class MethodDemo:
    a=1

    #cls is passed as the 1st parameter and used to access class variable
    @classmethod
    def classM(cls):
        print("Class method. cls.a=",cls.a)
    #static method: does not pass self or cls
    @staticmethod
    def staticM():
        print("Static method")


MethodDemo.classM()
md1 = MethodDemo()
md1.classM()

md1.staticM()


class OneClass:
    def __init__(self):
        print('OneClass')

    def __str__(self):
        return 'OneClass'

class AnotherClass:
    def __init__(self):
        print('AnotherClass')

    def __str__(self):
        return 'AnotherClass'