import csv
#READ
f=open('data.csv','r')
content=csv.reader(f)
for  row in content:
    print(row)
f.close()


#write

f=open('book.csv','w')
content=[['title','auther','place'],
         ['book1','jhon','ekm'],
         ['book2','sam','tvm']]
writer=csv.writer(f)
writer.writerows(content)
f.close()