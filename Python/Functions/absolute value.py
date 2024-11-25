number=int(input("Enter a positive or negative number"))
def absolute_value(num):
    if num>=0:
        return num
    else:
        return -num
    

print(absolute_value(number), "is the absolute value of this number.")
