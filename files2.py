import shutil

# FILE COPYING
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)
# ^ all take the same arguments

# shutil.copyfile()  # src, dst
shutil.copyfile("C:\\Users\\thepm\\Desktop\\TextForPython.txt", 'copy.txt')  # just a name copies to project path
