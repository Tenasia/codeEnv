def isPalindrome(oldString):
    
    oldString = oldString.lower()
    newStr = ''

    for char in oldString:
        newStr = char + newStr
    
    if newStr == oldString:
        return True
    else:
        return False


a = isPalindrome('Mom')
print(a)