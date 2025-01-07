file2=open('Codingal.txt')
print(file2.readline())
print(file2.readline())
print(file2.readline())
file2.close()

file2=open('Codingal.txt')
for x in file2:
    print(x)

file2.close()