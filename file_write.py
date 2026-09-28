f=open('k.txt','w') # if file exist it will erase thr file content and returns

# f.write('hello\n')
# f.write('python\n')

f.writelines(['hello\n','python\n'])
f.close()