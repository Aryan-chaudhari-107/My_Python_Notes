
''' To delete a file, you must import the OS module, and run its os.remove() function: '''

import os
# os.remove("demofile2.txt")


''' Check if file exists, then delete it: '''\

if os.path.exists("demofile2.txt"):
  os.remove("demofile2.txt")
else:
  print("The file does not exist")



# >>>>> DELETE FOLDER <<<<< # :
os.rmdir("myfolder")