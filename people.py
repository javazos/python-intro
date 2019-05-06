import memory_profiler
import random
import time


names=['John','Corey','Adam','Steve','Rick','Thomas']
majors=['Math','Engineering','CompSci','Arts','Business']

print ('Memory(Before):{}Mb'.format(memory_profiler.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        yield person
t1=time.process_time()
people = people_list(1000000)
t2=time.process_time()
print ('Memory(After):{}Mb'.format(memory_profiler.memory_usage()))
print('Took {} seconds'.format(t2-t1))

# t3=time.process_time()
# people = people_generator(1000000)
# t4=time.process_time()
#
# print ('Memory(After):{}Mb'.format(memory_profiler.memory_usage()))
# print('Took {} seconds'.format(t4-t3))