import os
import os.path

print(os.getcwd())

os.chdir('C:\\Users\\cxu')

print(os.getcwd())
os.mkdir('OS-DEMO-2')
os.makedirs('OS-DEMO-3\\SUB-OS-DEMO-3')
print(os.listdir())
print(os.path.exists('OS-DEMO-2'))

os.rmdir('OS-DEMO-2')
os.removedirs('OS-DEMO-3\\SUB-OS-DEMO-3')
print(os.path.exists('OS-DEMO-3\\sub-os-demo-3'))
print(os.getcwd())
os.chdir('C:\\Users\\cxu\\PycharmProjects\\PRACTICE')
os.rename('car.py','car1.py')
os.rename('car1.py','car.py')
mod_time = os.stat('car.py').st_mtime
c_time = os.stat('car.py').st_ctime

from datetime import datetime
print('file maintained last time at {}.'.format(datetime.fromtimestamp(mod_time)))
print('file created at {}.'.format(datetime.fromtimestamp(c_time)))

#traverse
print(type(os.walk("c:\\users\\cxu")))   #<class 'generator'>

for dirpath,dirnames,filenames in os.walk("c:\\users\\cxu\\PycharmProjects"):
    print('Current Path:' , dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

