class A:
    def __init__(self):
        self.__x=5
        self._y=6


varA = A()
print(varA._y)
print(varA._A__x)



print(varA.__x)
