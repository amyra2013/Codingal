value=input("Enter a word ")

def palindrome(x):
    left = 0
    right= len(x)-1

    while right>=left:
        if x[left]==x[right]:
            left=left+1
            right=right-1
        else:
            return False
    return True
print("Check for palindrome: ")
print(palindrome(value))
    
    