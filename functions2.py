#def function(farg,*args,**kwargs)


# one asterisk num stors a variable-length argument list that
#contains several items

def addNumbers(*num):
    sum=0
    for i in num:
        sum+=i
    print(sum)

addNumbers(1,2,3,4)
addNumbers(10,11,12)


#keyworded variable length argument list
#
def printMemberAge(**age):
    for i,j in age.items():
        print('name={},age={}'.format(i,j))
printMemberAge(Peter=5,John=7)
printMemberAge(Peter=5,John=7,Yvonne=10)