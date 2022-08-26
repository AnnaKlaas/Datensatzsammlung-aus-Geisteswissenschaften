import re

filename = input("enter file name\n")
minDegree = int(input("enter the minimum degree\n"))
maxDegree = int(input("enter the maximum degree\n"))
lines = []
elements = []
resMap = {}
result = '' 
with open(filename) as f:
    fileRead = f.read()
    lines = fileRead.split('\n') 
    elements = re.split('[\\t\\n]', fileRead)
elementsMap = {}
for element in elements:
    value = elementsMap.get(element, 0)
    value += 1
    elementsMap[element] = value

for line in lines:
    if '\t' in line:
        left, right = line.replace('\n', '').split('\t')
        leftcount, rightcount = (elementsMap.get(left, 0), elementsMap.get(right, 0))
        if ((leftcount > minDegree and leftcount < maxDegree) and ((rightcount > minDegree and  rightcount < maxDegree) or rightcount == 1)):
            value = resMap.get(left, [])
            value += [right]
            resMap[left] = value

result += 'graph\n[\n'
for key, values in resMap.items():
    if len(values) > 1:
        result += 'node [ id ' + key + ' label ' + values[0].replace('*', '"') + ' ]\n'
for key, values in resMap.items():
    if len(values) > 1:
        for value in values[1:]:
            result += 'edge [ source ' + key + ' target ' + value + ' ]\n'
result += ']'

f = open(filename.replace('txt', 'gml'), "w")
f.writelines(result)
f.close