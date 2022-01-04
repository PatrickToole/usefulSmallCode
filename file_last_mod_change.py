''' 
this creates new copies of all files in a directory. 
resulting in last modified time being updated to current time
'''

import os

for dir in os.listdir('C:\\Users\\toolep\\Desktop\\testfile'):
    print(dir)
    for file in os.listdir(f'C:\\Users\\toolep\\Desktop\\testfile\\{dir}'):
        os.chdir(f'C:\\Users\\toolep\\Desktop\\testfile\\{dir}')
        command = f'copy /b "{file}" +,,'
        os.system(command)