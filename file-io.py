s = "Noman is a very good boy"

#  writing a file
'''with open("file-io-practice.txt", "w") as f:
    f.write(s)
'''
'''
# second process to write a file ::: ei khaan e amader alada kore close kore dite hoy
fileOpen = open("test.txt", "w")
fileOpen.write(s)
fileOpen.close()
'''

#  Read a file
with open("file-io-practice.txt", "r") as f:
    text = f.read()
    print(text)

#   appending to a file
with open("file-io-practice.txt", "a") as boo:
    boo.write(
        "The cow is a domestic animal. ")  # this means, how much time we will run our program that much time the writing command will run and write the text to the file.
