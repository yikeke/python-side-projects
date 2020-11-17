import sys

# python3 /Users/coco/Documents/GitHub/python-side-projects/cofile/blog-title.py '<title>'
# print(sys.argv[1:])
for title in sys.argv[1:]:
    title = title.lower()
    title = title.replace(' ','-')

print(title)