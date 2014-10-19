# Replace All

A lightweight python script that reads a list of files, a word to find, and a word to replace.  Outputs the result in the same file, unless the output suffix is specified in the last optional keyword. The output suffix will be appended onto each filename in the list so as not to overwrite the original files.

*Format*:

    python replaceAll.py filename wordToFind wordToReplace[ suffix]

*Example*:

    python replaceAll files.txt name mName _new


#### Example files.txt
----------------
     program.cpp
     program.h 

