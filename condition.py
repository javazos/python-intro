# Equal: ==
# Not Euqal !=
# Greater than >
# less than <
#Greater or equal >=
#less or equal <=
#Object identity
# and
# or
# not

#False values:
    #False
    #None
    #Zero OF ANY NUMERIC TYPE
    #Any empty sequence. For example, '',(), []
    #Any empty mapping. For example, {}


# condition = False
# condition = None
# condition = 0
# condition = list()
# condition = set()
# condition=tuple()
# condition={}
# condition=''
condition=[]
if condition:
    print('True')
else:
    print('False')
language = 'Java'

if language == 'Python':
    print('Languae is Python')
elif language == 'Java':
    print('Lnaguage is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

user='Admin'
logged_in = True

if user == 'Admin' and logged_in :
    print('Admin page')
else:
    print('Bad creds')

if not logged_in:
    print('Please log in ')
else:
    print('Welcome')

