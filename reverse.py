def reverce(string):

    finalString = ""

    strLen = len(string)

    finalStrLen = len(finalString)

    char = strLen

    while finalStrLen != strLen:
        char = char - 1
        finalString = finalString + string[char]
        finalStrLen = finalStrLen + 1
    return finalString
print(reverce("Testing1234567890"))
