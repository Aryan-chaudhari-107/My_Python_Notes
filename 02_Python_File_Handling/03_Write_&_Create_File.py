# # # >>>>> WRITE TO AN EXITING FILE <<<<< # :
# # ''' 
# # "a" - Append - will append to the end of the file

# # "w" - Write - will overwrite any existing content 
# # '''

# # with open ("demofile.txt", "a") as f:
# #     f.write("\nNow the file has more content!")

# # with open("demofile.txt") as f:
# #   print(f.read())
# # # Output: Hello! Welcome to demofile.txt
# # #         This file is for testing purposes.
# # #         Good Luck!
# # #         Now the file has more content!



# # >>>>> OVERWRITE EXISTING CONTENT <<<<< # :
# ''' This function delete existing content and overwrite a new content. '''

# with open("demofile.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# #open and read the file after the overwriting:
# with open("demofile.txt") as f:
#   print(f.read())
# # Output: Woops! I have deleted the content!



# >>>>> CREATE A NEW FILE <<<<< # :
'''
"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists
'''

f = open("demofile2.txt", "x")
f.write("New file created and added this text.")

f = open("demofile2.txt")
print(f.read())