import sys

# 把一个首字母大写的标题转换成小写 -
# python3 /Users/coco/Documents/GitHub/python-side-projects/cofile/blog-title.py '<title>'
# print(sys.argv[1:])
for title in sys.argv[1:]:
    title = title.lower()
    title = title.replace(' ','-')
    title = title.replace('.','')

print(title)