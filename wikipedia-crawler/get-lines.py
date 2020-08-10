famous_people = []

with open("/Users/coco/Documents/GitHub/python-side-projects/wikipedia-crawler/year1902-2020.txt",'r') as foo:
    for line in foo.readlines():
        if '``' in line:
            famous_people.append(line)

with open("famous_people.txt", "a") as f:
    for person in famous_people:
            f.write(person)