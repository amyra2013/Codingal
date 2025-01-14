with open('Codingal.txt','w') as f:
    f.write('My name is Amyra. I am 11 years old.')

with open('Codingal.txt', 'r') as file:
    linesread=file.readlines()
    print('Words in the file are:')
    for x in linesread:
        word=x.split()
        print(word)

