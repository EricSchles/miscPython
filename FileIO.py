import os #used later in the program..

#basic file IO
#writing to a file
test = open("test.txt","w")
test.write("testing...\n")
test.close()

#reading from a file
test = open("test.txt","r")
print test.read()
test.close()

#Note - if you open file with "w" for write it will create the file if it does not already exist.  However, it will delete the contents of the file.

test = open("test.txt","a")
test.write("even more testing...\n")
test.close()

test = open("test.txt","r")
print test.read()
test.close()

#finally, reading and writing to a file object at once.

test = open("test.txt", "r+")
test.write("well there\n")
test.seek(0)
print test.read()
test.close()

#Advanced usage: Opening and closing a file within a context

with open("test.txt","w") as f:
    f.write("") #overwriting the file
    f.close()

# uncomment the following code to get an error:
#f.write("anything")

os.remove("test.txt") # removing the file
