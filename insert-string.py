# Suppose you have a bunch of markdown files in a root directory called RD1, 
# and you want to do the following things to all these files:
# - If the file contains a specific string S2, append string S3 to S2;
# - If the file does not contain S2, append string S4 to a specific string S5.

import os

# Walks files in a given folder (e.g. RD1) and get all files' paths and filenames.
for root, dirs, files in os.walk("<absolute-path-of-RD1>", topdown=True):
    for name in files:
        if '.md' in name:   # Check all markdown files
            full_filepath = os.path.join(root, name)

            file = open(full_filepath, "r" )
            content = file.read()
            file.close()

            find_S2 = '<S2>'
            insert_S3 = '<S3>'
            original_pos = content.find(find_S2)
            pos = original_pos + len(find_S2)

            # If the file contains a specific string S2, append S3 to S2.
            if original_pos != -1:
                # New content after insertion
                content = content[:pos] + insert_S3 + content[pos:]
                file = open(full_filepath, "w" )
                file.write( content )
                file.close()

            # If the file does not contain S2, append string S4 to S5.
            else:
                find_S5 = '<S5>'
                insert_S4 = '<S4>'
                original_pos = content.find(find_S5)
                pos = original_pos + len(find_S5)

                # New content after insertion
                content = content[:pos] + insert_S4 + content[pos:]
                file = open(full_filepath, "w" )
                file.write( content )
                file.close()
