'''
Name: David Patton and Josh Earley
email: pattondk@mail.uc.edu, earleyja@mail.uc.edu, lambmj@mail.uc.edu, nielseai@mail.uc.edu, ehrlicmh@mail.uc.edu
Assignment: Calloway_FinalProject
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Decrypted a file and found our location presented a picture
Citations: 
Anything else that's relevant: This was a group project and it was fun! :)
'''
from PIL import Image # This will allow us to use pillow 
import json

#This reads the text file
with open('english.txt') as f:
    lines = f.readlines()
with open('EncryptedGroupHints.json') as g:
    lines = g.readlines()
#This function turns the text file into a dictionary that is indexed    
def englishIndex(fileName):
    d = {}
    with open(fileName, 'r') as f:       
        content = f.readlines()
        lnc = 0
        result = {}
        for line in content:
            line = line.rstrip()
            words = line.split(" ")
            for word in words:
                tmp = result.get(word)
                if tmp is None:
                    result[word] = []
                if lnc not in result[word]:
                    result[word].append(lnc)

            lnc = lnc + 1

        return result

#print(englishIndex('english.txt'))

#englishIndex('english.txt')

def show_picture(filename):
    
    Neilpicture = Image.open(filename)
    angle = 90
    out = Neilpicture.rotate(angle)
    out.load()
     
    
    return out


def jsonIndex(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)

if __name__ == "__main__":
    my_data = jsonIndex('EncryptedGroupHints.json')
    print(my_data)

'''jsonIndex('EncryptedGroupHints.json')

myJsonIndex = (jsonIndex('EncryptedGroupHints.json'))
myEnglishIndex = (englishIndex('english.txt'))

myEnglishIndex = dict(myEnglishIndex)


list(myJsonIndex)
callowayNum = (myJsonIndex['Calloway'])

#print(callowayNum)
callowayNum = [eval(i) for i in callowayNum]
#print(callowayNum)'''

'''result_dict = {}
for ele in callowayNum:
    result_dict[ele] = []
    for key in myEnglishIndex.keys():
        if ele in myEnglishIndex[key]:
            result_dict[ele].append(key)

print(result_dict)'''







