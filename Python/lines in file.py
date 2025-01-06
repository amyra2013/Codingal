linesInFile=open('/Users/amyrachavan/Desktop/Codingal/Python/Codingal.txt')
counter=0
content=linesInFile.read()

lines=content.split('\n')
for i in lines:
    if i :
        counter+=1

print('Number of lines in the file =', counter)