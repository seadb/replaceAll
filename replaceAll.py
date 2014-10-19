""" Replace All

    A lightweight python script that reads a list of files, 
    a word to find, and a word to replace.  Outputs the result in the
    intial 
"""

__author__ = "Chelsea Bridson (bridsonc@msu.edu)"
__version__ = "$Revision: 0.2 $"
__date__ = "$Date: 2014/10/18$"
__copyright__ = "Copyright (c) 2014 Chelsea Bridson"
__license__ = "MIT"

# Format:       replaceAll filename wordToFind wordToReplace[ suffix]
# Example:      replaceAll files name mName _new
#
# Example file
# ------------
# program.cpp
# program.h 

import sys

inputf = open(sys.argv[1], 'r')
old = sys.argv[2]
new = sys.argv[3]
suffix = ""
if(len(sys.argv) == 5):
    suffix = sys.argv[4]

outFiles = []
outStrings = []
for line in inputf:
    line = line.strip()
    inFile = open(line, 'r')
    inStr = inFile.read()
    outStr=inStr.replace(old, new)
    outStrings.append(outStr)
    inFile.close()
    #outFile = open(line, 'w')
    outFiles.append(line+suffix)


for i in range(0, len(outStrings)):
    outFile = open(outFiles[i], 'w')
    outFile.write(outStrings[i])
    outFile.close()
