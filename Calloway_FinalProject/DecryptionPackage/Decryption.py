    '''
    Name: David Patton, Josh Earley, Matt Lamb, Aria Nielsen, Maxwell Ehrlich 
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
