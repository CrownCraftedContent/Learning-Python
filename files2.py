# import shutil

# FILE COPYING
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
# ^ all take the same arguments

# shutil.copyfile()  # src, dst
# shutil.copyfile("C:\\Users\\thepm\\Desktop\\TextForPython.txt", 'copy.txt')  # just a name copies to project path


import os
import shutil

# FILE MOVING
print("\nFILE MOVING")
source = "test.txt"
destination = "C:\\Users\\thepm\\OneDrive\\Desktop\\test.txt"

try:
    if os.path.exists(destination):  # <-- prevents overwriting on accident
        print("There is a file here!")
    else:
        os.replace(source, destination)  # moves files and directories
        print(source + " was moved to " + destination)
except FileNotFoundError:
    print(source + " was not found.")


# FILE DELETION
# os used for files and empty directories
# shutil to remove a directory containing files
path = 'test.txt'  # if within project
# os.remove(path)

path2 = 'folder'
# to be careful v
try:
    #os.remove(path)  # delete files
    os.rmdir(path2)  # delete EMPTY directories only
    #shutil.rmtree(path2)  # delete dir's containing files. considered dangerous because removes all contents
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:  # thrown when trying to remove an empty folder (directory)
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path2 + " was deleted")
