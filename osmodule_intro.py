import os


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

from datetime_intro import datetime_intro
print('file maintained last time at {}.'.format(datetime_intro.fromtimestamp(mod_time)))
print('file created at {}.'.format(datetime_intro.fromtimestamp(c_time)))

#traverse
print(type(os.walk("c:\\users\\cxu")))   #<class 'generator'>

for dirpath,dirnames,filenames in os.walk("c:\\users\\cxu\\PycharmProjects"):
    print('Current Path:' , dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

print(os.environ)
print(os.environ.get('PATH'))

home_path = os.environ.get('HOMEPATH')
file_path = os.path.join(home_path, 'test.txt')
print(file_path)

#working with files
with open(file_path,'w') as f:
    f.write('xxx')
#basename- grab file name  basename
print(os.path.basename('c:\\users\cxu\\test.txt'))
#diritory name
print(os.path.dirname('c:\\users\cxu\\test.txt'))
#both name
print(os.path.split('c:\\users\cxu\\test.txt'))
#existing
print(os.path.exists('c:\\users\cxu\\test.txt'))
#is
print(os.path.isdir('c:\\users\cxu'))
print(os.path.isfile('c:\\users\cxu'))
#split ext
print(os.path.splitext('c:\\users\cxu\\test.txt'))
#split drv
print(os.path.splitdrive('c:\\users\cxu\\test.txt'))


#how to use os.path
print(dir(os.path))