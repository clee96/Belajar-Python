def palindrome(text):
    test = []
    result = []
    for i in range(0,(len(text))):
        test.append(text[i])
    for i in range(1,(len(text)+1)):
        result.append(text[-i])
    for i in range(0,len(result)):
        if test[i] == result[i]:
            return True
        else:
            return False
print(palindrome("kodok"))
