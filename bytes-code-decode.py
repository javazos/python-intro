chinesestr="这是一个字符串"
print(chinesestr, len(chinesestr))
data = chinesestr.encode('utf-8')
print(data, len(data))
chinesestr2=data.decode("utf-8")
print(chinesestr2)

if chinesestr == chinesestr2:
    print(True)

chstr="串"
print(chstr, len(chstr))
data2 = chstr.encode('utf-8')
print(data2, len(data2))
chstr2=data2.decode("utf-8")
print(chstr2)


aB = b'some bytes'
print(aB.split())
