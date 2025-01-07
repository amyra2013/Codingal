file3=open('Codingal.txt', 'r')
file4=open('CodingalUpdated.txt', 'w')


for x in file3:
    if x.startswith('Coding'):
        pass
    else:
        print(x)
        file4.write(x)

file3.close()
file4.close()