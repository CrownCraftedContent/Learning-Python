import os  # included in standard Python library

# FILE DETECTION
path = "C:\\Users\\thepm\\Desktop\\TextForPython.txt"  # change backslash from single (\) to double (\\)
# path = "C:\\Users\\thepm\\Desktop\\Folder"  # for directories
# NOTE: \n \t \etc. means we can't use single \'s in paths

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):  #
        print("That is a directory!")
else:
    print("That location doesn't exist.")


# READ / WRITE
#   open function
#       designed to handle resource management tasks like opening and closing files
#       ensures that resources are properly managed, even when errors occur within the block
#   refer using file name if in-project, probably need to use file path otherwise

try:
    with open("C:\\Users\\thepm\\Desktop\\TextForPython.txt") as file:  # closes files automatically after opening them
        print(file.read())
except FileNotFoundError as e:
    print("File not found. (" + str(e) + ")")

print(file.closed)  # file closed automatically by using "with open"


# FILE WRITING
#   open(file, mode)
#       'r' = read (default), 'w' = write, 'a' = append

text = "\nThis text will overwrite anything in the file"
with open('C:\\Users\\thepm\\Desktop\\TextForPython.txt', 'a') as file:
    file.write(text)

