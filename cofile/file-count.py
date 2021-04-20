import os
a = 0

for root, dirs, files in os.walk("/Users/coco/Documents/GitHub/pingcap-upstream/docs-tidb-operator", topdown=True):
#for root, dirs, files in os.walk("/Users/coco/Documents/GitHub/python-side-projects/cofile", topdown=True):
    for name in files:
        if '.md' in name:   # Check all markdown files
        # if '.md' in name and name not in filter_list:   # Check all .md files except those in filter_list
            a = a + 1

print(a)

# as of 2021.1.5
# docs-cn: 649 md files on master/5.0, 290 on 2.1, 349 on 3.0, 375 on 3.1, 650 on 4.0,
# docs: 588 on master,
# docs-dm: 146 on master/2.0, 96 on 1.0
# docs-tidb-operator: 243 on master, 230 on 1.1, 121 on 1.0
# dbaas: 33
