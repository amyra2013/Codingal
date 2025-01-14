fl=open('newsample.txt', 'x')
fl.close()

import os
if os.path.exists('sample.txt'):
    os.remove('sample.txt')
else:
    print('File does not exist')

with open('sample.txt', 'w') as newfile:
    newfile.write('This is a sample file.')

os.remove('Codingal.py')
os.remove('/Users/amyrachavan/Desktop/Codingal/Python/sample-folder/sample file.html')
os.rmdir('sample-folder')
os.remove('/Users/amyrachavan/Desktop/Codingal/Python/sample-folder')
os.remove('newsample.txt')