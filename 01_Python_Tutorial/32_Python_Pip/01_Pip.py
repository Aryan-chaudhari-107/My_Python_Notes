
# >>>>> WHAT IS PIP? <<<<< # :
''' PIP is a package manager for Python packages, or modules if you like. '''
''' Note: If you have Python version 3.4 or later, PIP is included by default. '''



# >>>>> WHAT IS PACKAGE? <<<<< # :
''' A package contains all the files you need for a module. '''
''' Modules are Python code libraries you can include in your project. '''



# >>>> DOWNLOAD A PACKAGE <<<<< # :
''' Downloading a package is very easy.
Open the command line interface and tell PIP to download the package you want. '''
        # pip install camelcase



# >>>>> USING A PACKAGE <<<<< # :
import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt)) # Output: Hello World
  


# >>>>> FIND PACKAGE <<<<< # :
'''Find more packages at https://pypi.org/. '''



# >>>>> REMOVE PACKAGE <<<<< # :
''' Use the uninstall command to remove a package: '''
    # pip uninstall camelcase

''' The PIP Package Manager will ask you to confirm that 
you want to remove the camelcase package: '''
   
#    Uninstalling camelcase-02.1:
#   Would remove:
#     c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase-0.2-py3.6.egg-info
#     c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camelcase\*
# Proceed (y/n)?

''' press y to uninstall '''



# >>>>> LIST PACKAGE <<<<< # :
''' Use the list command to list all the packages installed on your system: '''
    # pip list

# Result:
''' 
Package Version
------- -------
pip     25.1.1
tzdata  2025.2
'''