'''
Name: David Patton, Josh Earley, Matt Lamb, Aria Nielsen
email: pattondk@mail.uc.edu, earleyja@mail.uc.edu, lambmj@mail.uc.edu, nielseai@mail.uc.edu, ehrlicmh@mail.uc.edu
Assignment: Calloway_FinalProject
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Decrypted a file and found our location presented a picture
Citations: https://stackoverflow.com/questions/66171273/return-keys-of-dictionary-if-values-match-with-a-given-list
https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
https://stackoverflow.com/questions/41476636/how-to-read-a-json-file-and-return-as-dictionary-in-python
Anything else that's relevant: This was a group project and it was fun! :)
'''
from DecryptionPackage.Decryption import *
from PIL import Image


jsonIndex('EncryptedGroupHints.json')

myJsonIndex = (jsonIndex('EncryptedGroupHints.json'))
myEnglishIndex = (englishIndex('english.txt'))

myEnglishIndex = dict(myEnglishIndex)


list(myJsonIndex)
callowayNum = (myJsonIndex['Calloway'])

callowayNum = [eval(i) for i in callowayNum]

decodedLoc = {}
for ele in callowayNum:
    decodedLoc[ele] = []
    for key in myEnglishIndex.keys():
        if ele in myEnglishIndex[key]:
            decodedLoc[ele].append(key)


print(decodedLoc.values())

Neil = Image.open("Neil.jpg")
Neil.show()
