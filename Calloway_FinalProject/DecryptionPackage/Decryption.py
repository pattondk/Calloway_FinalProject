'''
Name: David Patton and Josh Earley
email: pattondk@mail.uc.edu, earleyja@mail.uc.edu, 
Assignment: Calloway_FinalProject
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Decrypted a file and found our location presented a picture
Citations: 
Anything else that's relevant: This was a group project and it was fun! :)
'''
#This reads the text file
with open('english.txt') as f:
    lines = f.readlines()

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

print(englishIndex('english.txt'))

englishIndex('english.txt')