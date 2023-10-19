import pandas as pd

df = pd.read_excel('통합 문서1.xlsx')
targets = df['1열']
print(targets)
objects = df['2열']
print(objects)

lst = []

for object in objects:
    for target in targets:
        if target in object:
            continue
        else:
            lst.append(target)
re = {}
re['3열'] = lst
re= pd.DataFrame(re)
re.to_excel('수정본.xlsx')