# Suppose you have a bunch of markdown files in a root directory called RD1, 
# and you list all these file links in another file called F2, now
# you want to check whether all the files in RD1 are listed in F2.

import os

# Use this filter_list when you want to skip checking some files
# filter_list = ['<file-name1.xx>','<file-name2.xx>',...]

# Walks files in a given folder (e.g. RD1) and get all files' paths and filenames.
for root, dirs, files in os.walk("<absolute-path-of-RD1>", topdown=True):
    for name in files:
        if '.md' in name:   # Check all markdown files
        # if '.md' in name and name not in filter_list:   # Check all .md files except those in filter_list 
            pin = 0         # Use a marker to differentiate file names
            # Find if the name string is in F2
            with open("<absolute-path-of-F2>",'r') as foo:
                for line in foo.readlines():
                    if name in line:
                        pin = 1
            if pin == 0:
                # Print the names of all files that are not in F2
                print(name, "not in F2")
