import myclasses

oneCls = myclasses.OneClass

print(oneCls)

md = myclasses.AnotherClass()
print(md)



from myclasses import MethodDemo
md = MethodDemo()
md.staticM()
md.classM()