# import json
#
# #READ
#
# f=open("data.json","r")
# content=json.load(f)
# print(content)
# print(content[0]['name'],content[0]['age'])
# print(content[1]['name'], content[1]['age'])
# f.close()


#WRITE
import json

content=[{'tittle':'book1','auther':'jhon','price':200},
         {'tittle':'book2','auther':'sam','price':300}]
f=open('book.json','w')
json.dump(content,f)
f.close()