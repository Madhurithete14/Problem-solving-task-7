# The function will take the name of take file and display the content of the file into console.
# write data in a file.
file1 = open("myfile.txt", "w")
L = ["Apple is red in colour \n", "Orange is orange in colour \n", "Banana is yellow in colour \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Namaste \n")
file1.writelines(L)
file1.close() # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()
