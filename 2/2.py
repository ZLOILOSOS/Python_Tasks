string = list(input("Введите строку: "))
string = [element.lower() for element in string]

stringKey = list(set(string))
if stringKey.count(" "):
    stringKey.remove(" ")

stringDict = {stringKey[i]: string.count(stringKey[i]) for i in range(len(stringKey))}

print(stringDict)