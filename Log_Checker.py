"""
This program looks through a log file and returns all lines that match the keyword.
"""
import os

def logcheck(keyword,
            filepath='/var/log/syslog',
            outpath='/root/Desktop/logoutput'):
    """
    keyword:
        Enter a word to search in the log.
    filepath:
        Enter the path to the log file; it can be absolute or relative.
    outpath:
        Enter the path to the output file.
    """

    # Open the log file and read the lines, then make a list to write to the new file
    file = open(filepath,'r').readlines()
    write = []
    # Take each line and see if the keyword is in it; if so, then write the line to the text file.
    for i in file:
        if keyword in i:
            write.append(i)

    fileb = open(outpath, 'w')
    fileb.writelines(write)
    # Close the text file and return a message that states that the process is over.
    fileb.close()
    print('All done.')

# call the function with 'USB' as the keyword.
logcheck('usb', filepath='x', outpath='y')
