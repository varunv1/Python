#list = []
#with open('vsearch.log') as log:
#    allData = (''.join(log.read())).split('|')
#    for i in allData:
#        list.append(i)
#print(list)
from flask import  escape
content = []
with open('vsearch.log') as log:
    for i in log:
        content.append([])
        for item in i.split('|'):
            content[-1].append(escape(item))
