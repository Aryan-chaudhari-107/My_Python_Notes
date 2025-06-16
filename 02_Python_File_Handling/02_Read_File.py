
# # >>>>>> OPEN A FILE ON THE SERVER <<<<< # :
# ''' 
# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for 
# reading the content of the file:
# '''

# f = open("demofile.txt", 'r') # OR you can also write open("demofile.txt")
# print(f.read())
# # Output: Hello! Welcome to demofile.txt
# #         This file is for testing purposes.
# #         Good Luck!



# ''' If the file is located in a different location, you will have to 
# specify the file path, like this: '''
# f = open("D:\\myfiles\welcome.txt")
# print(f.read())



# # >>>>> USING WITH STATEMENT <<<<< # :
# with open("demofile.txt") as f:
#   print(f.read())
# # Output: Hello! Welcome to demofile.txt
# #         This file is for testing purposes.
# #         Good Luck!



# # >>>>> CLOSE FILE <<<<< # :
# ''' If you are not using the with statement, you must write a close 
# statement in order to close the file: '''

# f = open("demofile.txt")
# print(f.read())
# f.close()



# # >>>>> READ ONLY PARTS OF THE FILE <<<<< # :
# ''' By default the read() method returns the whole text, but you can also 
# specify how many characters you want to return: '''

# f = open("demofile.txt")
# print(f.read(5)) # Output: Hello



# # >>>>> READ LINES <<<<< # :
# with open("demofile.txt") as f:
#   print(f.readline()) # Output: print 1st line


with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

