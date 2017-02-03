#! Insert the current directory path to Python Path
import sys
import os
cwd = os.getcwd() # current working directory

sys.path.append(cwd)
#print(sys.path)

#Test the module: generate_list
from generate_list import printIt
printIt()