with open('file1.txt') as f1:
    first=f1.readlines()
    
with open('file2.txt') as f2:
    second=f2.readlines()

result=[int(n) for n in first if n in second]


print(result)


