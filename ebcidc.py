import codecs
hex_str = 'E388854083969497A4A38599408881A2409985829696A38584408699969440814082A48783888583924B'
output = []
ddf=[4,9,4,9,5,2,9]
distance = 0

#This braeaks my hex string into chunks based off the list  'DDF'

for x in ddf:
    output.append(hex_str[distance:x*2+distance])
    distance +=x*2


#This prints out the list of hex strings
for x in output:
    print(x)


#This prints out the vyte objects in the list
for x in output:
    x=codecs.decode(x,"hex")
    # x = codecs.decode(x, "cp500")
    print(x)

# #The next line print the correct text
# hex = codecs.decode(hex_str, "hex")
# print(codecs.decode(hex_str, 'cp1140'))

my_bytes = bytearray.fromhex(hex_str)
print(my_bytes)

my_str = my_bytes.decode('cp500')
# my_str = my_bytes.decode('cp37')
print(my_str)
