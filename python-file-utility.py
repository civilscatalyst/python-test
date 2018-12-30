import os 

# writing to a file
fw = open("D:\Sudhanshu\my_files\development\python-test\myfiles\myfile.txt", "a")
# 'w' for writing (truncating the file if it already exists), 
# 'x' for creating and writing to a new file, and 
# 'a' for appending (which on some Unix systems, means that all writes append to the end of the file regardless of the current seek position).
fw.write("New Text !")
fw.write("\n") # writes new line to the file

# closing the file
if not fw.closed:
    fw.close()

# opening a file in read mode
fo = open("D:\Sudhanshu\my_files\development\python-test\myfiles\myfile.txt", "r")

# reading first n characters from file
print(fo.read(5))
# reading lines from a file, ex - calling fo.readline() twice prints first 2 lines
print(fo.readline())

# loops through the file line by line
for x in fo: # note: since the file is already open and being read, the read pointer has moved to next lines/text 
    print(x)

if not fo.closed:
    fo.close()
    print('File closed')
    
# check whether file exists, import os module for this
if os.path.exists("D:\Sudhanshu\my_files\development\python-test\myfiles\myfile.txt"):
    print("file exists")
    # os.remove("D:\Sudhanshu\my_files\development\python-test\myfiles\myfile.txt") # deletes the file
else:
    print("file doesnt exist")

# To delete an entire folder, use os.rmdir()
# renaming a file, os.rename(f_old, f_new)