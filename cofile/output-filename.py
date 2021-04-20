import os

for root, dirs, files in os.walk("/Users/coco/Documents/GitHub/pingcap-upstream/docs-cn", topdown=True):
#for root, dirs, files in os.walk("/Users/coco/Documents/GitHub/python-side-projects/cofile", topdown=True):
    for name in files:
        if '.md' in name:   # Check all markdown files
            filepath = os.path.join(root, name)
        # if '.md' in name and name not in filter_list:   # Check all .md files except those in filter_list
            print(filepath)

